"""Export the four editable review documents; do not invent missing observations."""
from pathlib import Path
import argparse,csv,html,re
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,Image,Table,TableStyle
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from PIL import Image as PILImage
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parent.parent
WIDTH=A4[0]-80
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Body',fontName='Helvetica',fontSize=9.3,leading=12.3,spaceAfter=7))
styles.add(ParagraphStyle(name='Note',fontName='Helvetica',fontSize=7.5,leading=9.4,spaceAfter=6,textColor=colors.HexColor('#475569')))
styles.add(ParagraphStyle(name='Cell',fontName='Helvetica',fontSize=7.2,leading=9))
styles['Heading1'].fontSize=19;styles['Heading1'].leading=22;styles['Heading1'].textColor=colors.HexColor('#312e81')
styles['Heading2'].fontSize=11.5;styles['Heading2'].leading=14

def inline(text):
    text=text.replace('\u2013','-').replace('\u2014','-').replace('\u2011','-').replace('\u2192','->')
    escaped=html.escape(text,quote=False)
    escaped=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',escaped)
    escaped=re.sub(r'`([^`]+)`',r'<font name="Courier">\1</font>',escaped)
    return escaped

def para(text,style='Body'):
    return Paragraph(inline(text),styles[style])

def make_table(rows,widths=None):
    data=[[para(c,'Cell') for c in row] for row in rows]
    widths=widths or [WIDTH/len(rows[0])]*len(rows[0])
    widths=[w*WIDTH/sum(widths) for w in widths]
    table=Table(data,colWidths=widths,repeatRows=1,hAlign='LEFT')
    table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#ede9fe')),('VALIGN',(0,0),(-1,-1),'TOP'),('LINEBELOW',(0,0),(-1,0),.5,colors.HexColor('#a5b4fc')),('BOTTOMPADDING',(0,0),(-1,-1),5),('TOPPADDING',(0,0),(-1,-1),5),('LINEBELOW',(0,1),(-1,-1),.25,colors.HexColor('#e2e8f0'))]))
    return table

def evidence_appendix():
    with (ROOT/'review/evidence-log.csv').open(encoding='utf-8-sig',newline='') as f: rows=list(csv.DictReader(f))
    content=[para('Appendix - Evidence log','Heading1'),para('One row per retained evidence file. Unknown screenshot capture times have not been reconstructed from filesystem dates or server headers. HTML audit fetchTime values are separately identified. Cropped details rely on associated full-page evidence and the student inspection account.','Note')]
    data=[['ID','File','What it shows','Time and date','Page address']]
    for row in rows:
        data.append([row['ID'],row['File'],row['What it shows'],row['Time and date'],row['Page address']])
    content.append(make_table(data,[30,106,155,89,135]))
    return content

def parse(path,evidence_root):
    lines=path.read_text(encoding='utf-8-sig').splitlines();story=[];i=0;next_style='Body';widths=None;image_size=None
    while i<len(lines):
        line=lines[i].strip()
        if not line:i+=1;continue
        if line=='<!-- pagebreak -->':story.append(PageBreak());i+=1;continue
        if line=='<!-- note -->':next_style='Note';i+=1;continue
        if line=='<!-- evidence-log -->':story.extend(evidence_appendix());i+=1;continue
        if line.startswith('<!-- widths:'):
            widths=[float(v.strip()) for v in line.split(':',1)[1].replace('-->','').split(',')];i+=1;continue
        if line.startswith('<!-- image-size:'):
            image_size=[float(v.strip()) for v in line.split(':',1)[1].replace('-->','').split(',')];i+=1;continue
        if line.startswith('<!-- image-pair:'):
            names=[name.strip() for name in line.split(':',1)[1].replace('-->','').split(',')]
            cell_width=WIDTH/len(names);pictures=[]
            for name in names:
                picture=evidence_root/name
                with PILImage.open(picture) as im:iw,ih=im.size
                scale=(cell_width-8)/iw
                pictures.append(Image(str(picture),width=iw*scale,height=ih*scale))
            pair=Table([pictures],colWidths=[cell_width]*len(names))
            pair.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('ALIGN',(0,0),(-1,-1),'CENTER'),('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4)]))
            story.append(pair);i+=1;continue
        if line.startswith('<!--'):i+=1;continue
        if line.startswith('# '):story.append(para(line[2:],'Heading1'));i+=1;continue
        if line.startswith('## '):story.append(para(line[3:],'Heading2'));i+=1;continue
        if line.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].strip().startswith('|'):
                cells=[x.strip().replace('\\|','|') for x in re.split(r'(?<!\\)\|',lines[i].strip().strip('|'))]
                if not all(re.fullmatch(r':?-+:?',c) for c in cells):rows.append(cells)
                i+=1
            if rows:story.append(make_table(rows,widths))
            widths=None;continue
        match=re.match(r'!\[([^]]*)\]\(([^)]+)\)',line)
        if match:
            picture=evidence_root/Path(match.group(2)).name
            if not picture.is_file():raise FileNotFoundError(picture)
            if image_size:story.append(Image(str(picture),width=image_size[0],height=image_size[1],kind='proportional'))
            else:story.append(Image(str(picture),width=WIDTH,height=200,kind='proportional'))
            story.append(Spacer(1,4));image_size=None;i+=1;continue
        paragraph=[line];i+=1
        while i<len(lines) and lines[i].strip() and not lines[i].lstrip().startswith(('#','<!--','|','![')):
            paragraph.append(lines[i].strip());i+=1
        story.append(para(' '.join(paragraph),next_style));next_style='Body'
    return story

def footer(canvas,doc):
    canvas.setStrokeColor(colors.HexColor('#cbd5e1'));canvas.line(40,37,A4[0]-40,37)
    canvas.setFillColor(colors.HexColor('#475569'));canvas.setFont('Helvetica',7)
    canvas.drawString(40,25,'Coacheey field study | Course submission review | 10 November 2026')
    canvas.drawRightString(A4[0]-40,25,str(doc.page))

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir',type=Path,help='Default: overwrite the four submission PDFs in this project.')
    parser.add_argument('--evidence-root',type=Path,default=ROOT/'evidence')
    args=parser.parse_args()
    destinations={'report':Path('report.pdf'),'owner-summary':Path('owner-summary.pdf'),'benchmark':Path('stretch/benchmark.pdf'),'usability-test':Path('stretch/usability-test.pdf')}
    for name,relative in destinations.items():
        target=(args.output_dir or ROOT)/relative;target.parent.mkdir(parents=True,exist_ok=True)
        document=SimpleDocTemplate(str(target),pagesize=A4,leftMargin=40,rightMargin=40,topMargin=36,bottomMargin=48,title=name,author='Haytam CHARAFI; AI-assisted review copy')
        document.build(parse(ROOT/'review'/f'{name}.md',args.evidence_root),onFirstPage=footer,onLaterPages=footer)
        pdf=PdfReader(target);print(f'{relative}: {len(pdf.pages)} page(s)')
        if name=='report':
            main_pages=next((n for n,p in enumerate(pdf.pages) if 'Appendix - Evidence log' in p.extract_text()),len(pdf.pages))
            if main_pages>6:raise ValueError(f'Main report is {main_pages} pages; shorten review/report.md to at most 6 before submitting.')
            print(f'  Main report: {main_pages} pages; appendix: {len(pdf.pages)-main_pages}')
        if name=='owner-summary' and len(pdf.pages)!=1:raise ValueError('Owner summary must be exactly one page; shorten its source.')

if __name__=='__main__':main()

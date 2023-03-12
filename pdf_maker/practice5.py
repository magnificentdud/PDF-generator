from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def drawString(pdf, component):
    color = component['color']
    location = component['location']
    message = component['message']

    pdf.setFillColorRGB(*color)
    pdf.drawString(*location, message)
    return pdf

pdf = canvas.Canvas('test.pdf', pagesize = A4)
for elem in json_data['text']:
    pdf.drawString(pdf, elem)

pdf.showPage()
pdf.save


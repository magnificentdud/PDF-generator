from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

text_components = [
  { #first text component
    'text' :'Aaward Gold',
    'location' : (100,100),
    'color' : (0,0,0),
    'fontScale' : 20
    
  },
  {
    'text' :'Anabelle',
    'location' : (300,400),
    'color' : (255,0,0),
    'fontScale' : 10
  },
  {
    'text' :'2023-2-10',
    'location' : (400,100),
    'color' : (0,0,255),
    'fontScale' : 15
  }
  
]

pdfmetrics.registerFont(TTFont('DarkGardenMK', 'DarkGardenMK.ttf'))

def drawString(pdf, component):
    x,y = component['location']
    message = component['text']
    r,g,b = component['color']

    pdf.setFillColorRGB(r,g,b)
    pdf.drawString(x,y,message)
    return pdf
pdf = canvas.Canvas('test.pdf',pagesize = A4)

for elem in text_components:
    pdf = drawString(pdf, elem)
pdf.showPage()
pdf.save()

def main():
    pdf = canvas.Canvas('my_first_pdf.pdf',pagesize = A4)
    #set color
    # pdf.setFillColorRGB(255,0,0)
    #setfont,scale
    # pdf.setFont('DarkGardenMK',30)
    #textwrite , text
    # pdf.drawString(100,50,'Woochan')

    # put image
    # pdf.drawImage('skl_logo.jpeg',480,720,width =100,height=100)

    pdf.showPage()
    pdf.save()

if __name__ == '__main__':
    main()
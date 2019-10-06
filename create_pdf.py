from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from reportlab.graphics.shapes import *
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.graphics.charts.piecharts import Pie
from PIL import Image

img=Image.open(r"images.png")
c=canvas.Canvas("name.pdf",pagesize=A4,bottomup=0)
img=img.rotate(180)
img = img.transpose(Image.FLIP_LEFT_RIGHT)
width,height=A4

c.showOutline()


# background format]
im1 = Image.open(r"pdf+format.jpg")
im1=im1.rotate(180)
im1 = im1.transpose(Image.FLIP_LEFT_RIGHT)
c.drawInlineImage(im1,0,-11.2*inch,width,11.2*inch)


# LOGO
c.drawInlineImage(img, width/2+(0.1*inch), -.80*inch, 2*inch, 1*inch)
c.line(width/2,.20*inch,width/2,inch*1.25)

# Address
gali = "573,Manas Enclave"
colony = "Indra Nagar"
city = "Lucknow"
state = "Uttar Pradesh"
c.setFont("Courier-BoldOblique", 14)
c.drawRightString(width/2-(0.1*inch),.40*inch,gali)
c.drawRightString(width/2-(0.1*inch),.65*inch,colony)
c.drawRightString(width/2-(0.1*inch),.90*inch,city)
c.drawRightString(width/2-(0.1*inch),1.15*inch,state)



# Rectangle SIDE WALA
# c.setFillColorRGB(1,0.5,.6)
# c.rect((width/2)+(width/5),(height/6),(4*width)/5,(5*height)/6, fill=1)

c.setFillColorRGB(0,0,0)
# c.drawCentredString(1*inch,1*inch,"Skills Set")
# c.setFont("Courier-Bold", 20)
# c.drawCentredString((width/2)+(width/3)+.2*inch,(height/6)+.5*inch,"Skills Set")

# c.line((width/2)+(width/5),(height/6)+(0.75*inch),width,(height/6)+(0.75*inch))
c.setFont("Courier", 16)
c.drawString((width/2)+(width/6)+0.5*inch,(height/3)-0.1*inch,"Personality")
c.drawString((width/2)+(width/6)+0.5*inch,(height/3)+0.2*inch,"Team Work")
c.drawString((width/2)+(width/6)+0.5*inch,(height/3)+0.5*inch,"Listening")

# c.setFont("Courier-Bold", 20)
# c.drawCentredString((width/2)+(width/3)+.2*inch,(height/3)+.5*inch,"Work On")

# c.line((width/2)+(width/5),(height/3)+(0.75*inch),width,(height/3)+(0.75*inch))
c.setFont("Courier", 18)
c.drawString((width/2)+(width/6)+0.5*inch,(height/3)+1.6*inch,"Personality")
c.drawString((width/2)+(width/6)+0.5*inch,(height/3)+1.9*inch,"Team Work")
c.drawString((width/2)+(width/6)+0.5*inch,(height/3)+2.2*inch,"Listening")


# Draw pie chart
d = Drawing(200, 100)
pc = Pie()
pc.x = 65
pc.y = 15
pc.width = 2*inch
pc.height = 2*inch
pc.data = [10,20,30,40,50,60]
pc.labels = ['a','b','c','d','e','f']
# pc.slices.strokeWidth=0.5
# pc.slices[3].popout = 10
# pc.slices[3].strokeWidth = 2
# pc.slices[3].strokeDashArray = [2,2]
# pc.slices[3].labelRadius = 1.75
# pc.slices[3].fontColor = colors.red
d.add(pc)
d.drawOn(c,1.5*inch,4.5*inch)


# personality type
c.setFont("Courier-Bold", 15)
c.drawString(width/6,(height/5)-0.15*inch,"YOUR PERSONALITY TYPE IS : ")
wid = stringWidth("YOUR PERSONALITY TYPE IS : ","Courier-Bold", 15)
c.setFont("Courier-Oblique", 14)
c.drawCentredString(width/3+0.1*inch,(height/5)+0.1*inch,"ab;sroiujfdsklzc")


# Personal Details
name="Aniket Panwar"
class2="XII"
roll="11710548"
c.setFont("Courier-Oblique", 14)
c.drawString(width/6-0.1*inch,(height/5)-0.55*inch,name)
c.drawString(width-1.5*inch,(height/5)-0.55*inch,class2)
c.drawString(width-1.2*inch,(height/5)-0.08 * inch,roll)

# c.rect(c.rect((width/2)+(width/5),(height/6),(4*width)/5,(5*height)/6, fill=1))


# Paragraph
paragraph = "nodslxmeodjflkjcxvnjdfrgsfknvsfbgfdkncvjslkfdbgjnvc,m sdfjbghvljkdfnvd;cklxv dsjkdf a.dnf;lkas dn;lskn;l kasdlkf kma lkasdlf kasldkf a;dlfkj lkdjlkjmdlkfj"
x=0
p=0.5
n=len(paragraph)
for i in range (0,n):
	if stringWidth(paragraph[x:i],"Courier", 14)<4*inch:
		continue
	else:
		c.setFont("Courier",14)
		c.drawString(width/7,(height/5)+p*inch,paragraph[x:i])
		x=i;
		p=p+0.3
	
if x!=n-1:
	c.drawString(width/7,(height/5)+p*inch,paragraph[x:n-1])

# zingy logo
img=Image.open(r"zing.jpg")
img=img.rotate(180)
img = img.transpose(Image.FLIP_LEFT_RIGHT)

c.drawInlineImage(img,width-2*inch,10*inch,width/5,0.75*inch)

c.showPage()
c.save()
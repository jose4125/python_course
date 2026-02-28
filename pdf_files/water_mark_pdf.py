from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import Color
from pypdf import PdfReader, PdfWriter

c = canvas.Canvas('watermark.pdf', pagesize=letter)
width, height = letter

c.setFont("Helvetica-Bold", 60)

# Color RGB con canal alpha (0.3 = 30% opaco)
c.setFillColor(Color(0.5, 0.5, 0.5, alpha=0.3))

c.saveState()
c.translate(width/2, height/2)
c.rotate(45)
c.drawCentredString(0, 0, 'CONFIDENCIAL')
c.restoreState()

c.save()
print('✅ Watermark con transparencia real')



reader = PdfReader('./Working_Business_Proposal.pdf')
watermark_reader = PdfReader('watermark.pdf')
writer = PdfWriter()

watermark_page = watermark_reader.pages[0]

for page in reader.pages:
    page.merge_page(watermark_page)
    writer.add_page(page)

with open('Some_watermarked_pdf.pdf', 'wb') as new_pdf:
    writer.write(new_pdf)

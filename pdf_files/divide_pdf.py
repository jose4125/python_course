from pypdf import PdfReader, PdfWriter

reader = PdfReader('./Working_Business_Proposal.pdf')
writer = PdfWriter()

for page_index in range(3):
    page = reader.get_page(page_index)

    writer.add_page(page)

with open('Some_pages.pdf', 'wb') as new_pdf:
    writer.write(new_pdf)
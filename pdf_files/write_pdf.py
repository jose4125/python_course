from pypdf import PdfReader, PdfWriter

reader = PdfReader('./Working_Business_Proposal.pdf')
writer = PdfWriter()

first_page = reader.get_page(0)

writer.add_page(first_page)

with open('Some_BrandNew_doc.pdf', 'wb') as new_pdf:
    writer.write(new_pdf)
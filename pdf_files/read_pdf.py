from pypdf import PdfReader

reader = PdfReader('./Working_Business_Proposal.pdf')
print('=== file type:', type(reader))
print('=== reader:', reader)
print('=== number of pages:', len(reader.pages))

page_one = reader.pages[0]
page_one_text = page_one.extract_text()
print('=== page one text:', page_one_text)

metadata = reader.metadata
print('=== metadata:', metadata)
print('=== title', metadata.title)
print('=== author', metadata.author)
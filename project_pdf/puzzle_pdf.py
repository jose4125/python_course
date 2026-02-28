import csv
import re

import requests
from pypdf import PdfReader

def get_file_url ():
    with open('find_the_link.csv', 'r') as csv_file:
        csv_data = csv.reader(csv_file)
        data_lines = list(csv_data)
        print(data_lines)
        url_list = [data_row[index] for index, data_row in enumerate(data_lines)]

        return ''.join(url_list)

def download_file(file_id, output_path):
    url = f'https://drive.google.com/uc?export=download&id={file_id}'
    response = requests.get(url, stream=True)

    with open(output_path, 'wb') as new_pdf:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                new_pdf.write(chunk)

print(get_file_url())
file_url = get_file_url()
file_id = file_url.split('=')[1]
print(file_id)

pdf_name = 'downloaded_file.pdf'

download_file(file_id, pdf_name)


reader = PdfReader(pdf_name)
phone_regex = r'\d{3}[\s.-]\d{3}[\s.-]\d{4}'
result = []

for page in reader.pages:
   page_text = page.extract_text()
   phone_matches = re.findall(phone_regex, page_text)

   if len(phone_matches):
       result.append(phone_matches[0])

print('=== result:', result)



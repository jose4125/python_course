txt_file = None

try:
    txt_file = open('text_file.txt', 'w', encoding='utf-8') #encoding para caracteres especiales
    txt_file.write('Hello World!')
    txt_file.write('\nbye world!')
    txt_file.write('\nnueva información')
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    txt_file.close()
    print('File has been closed.')
from urllib.request import urlopen

with urlopen('https://globalmentoring.com.mx/recursos/GlobalMentoring.txt') as content:
    content_str = content.read().decode('utf-8')
    print(content_str)

# count repetitions of the word 'GlobalMentoring'
word = 'GlobalMentoring'
print(f'\nTotal repetitions of {word}: {content_str.count(word)}')

with open('text_file.txt', 'w', encoding = 'utf8') as file:
    file.write(content_str)



# check if the word 'python' is in the content
print('python' in content_str)
print('Python is part of the content: ', 'python'.lower() in content_str.lower())

# startswith
print('the content starts with "En GlobalMentoring": ', content_str.startswith('En GlobalMentoring') )

# endswith
print('the content ends with "GlobalMentoring.com.mx": ', content_str.lower().endswith('globalmentoring.com.mx'.lower()))

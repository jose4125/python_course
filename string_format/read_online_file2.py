from urllib.request import urlopen

total_words = []
with urlopen('https://globalmentoring.com.mx/recursos/GlobalMentoring.txt') as content:

    for line in content:
        content_str = line.decode('utf-8').split()

        for word in content_str:
            total_words.append(word)

print(total_words)
print(f'Total words: {len(total_words)}')



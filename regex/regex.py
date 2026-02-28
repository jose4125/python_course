import re

text1 = "the agent's phone number is 408-555-1234. Call soon!"
text2 = 'my phone once, my phone twice'
pattern1 = 'phone'

match = re.search(pattern1, text1)
print('matches', match)
print('matches span', match.span())
print('matches text', match.group())

# search only return the first match
matches2 = re.search(pattern1, text2)
print('matches2', matches2)

# to return more than one match use findall
matches3 = re.findall(pattern1, text2)
print('matches3', matches3)

# iterate the text to find matches
for match4 in re.finditer(pattern1, text2):
    print('match4', match4)
    print('match4 text', match4.group())

pattern2 = r'\d{3}-\d{3}-\d{4}'
match5 = re.search(pattern2, text1)
print('matches5', match5)
print('matches5 text', match5.group())

pattern3 = r'(\d{3})-(\d{3})-(\d{4})'
match6 = re.search(pattern3, text1)
print('matches6', match6)
print('matches6 text', match6.group())
print('matches6 text', match6.groups())
print('matches6 groups', match6.group(1))

txt = "Please try to reach me out at 123-58-789-00 or 432-54-879-12"
match7 = re.findall(r'\d{3}(?=-\d{2}-\d{3}-\d{2})', txt)
print('matches7', match7)

# exclude digits o numbers
text3 = 'there are 3 numbers 34 inside 5 this sentences'
pattern4 = r'[^\d]'
match8 = re.findall(pattern4, text3)
print('matches8', match8)

# to dont split the words
pattern5 = r'[^\d]+'
match9 = re.findall(pattern5, text3)
print('matches9', match9)

# exclude punctuation
text4 = 'this is a string! But it has punctuation. How can we remove it?'
pattern6 = r'[^!.?]+'
match10 = re.findall(pattern6, text4)
print('matches10', match10)

# count words
pattern7 = r'[^!.?\s]+'
match11 = re.findall(pattern7, text4)
print('matches11', match11)

# include
text5 = 'Only find the hyphen-words in this sentence. But you do not know how long-ish they are'
pattern8 = r'[\w]+-[\w]+'
match12 = re.findall(pattern8, text5)
print('matches12', match12)

# multiple options for matching
text6 = 'Hello, would you like some catfish?'
text7 = 'Hello, would you like to take a catnap?'
text8 = 'Hello, have you seen this caterpillar?'
pattern9 = r'cat(fish|nap|erpillar)'
match13 = re.search(pattern9, text6)
print('matches13', match13)
match14 = re.search(pattern9, text7)
print('matches14', match14)
match15 = re.search(pattern9, text8)
print('matches15', match15)

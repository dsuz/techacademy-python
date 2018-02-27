file = './ch13.txt'
text = ""

with open(file) as fileobj:
    text = fileobj.read()
    fileobj.close()

text = text.replace('-', ' ').replace('\n', ' ').replace('\r', '').replace('.', '').replace(',', '').lower()
wordlist = text.split(' ')
print(wordlist)

word_counter = {}
for i in range(len(wordlist)):
    if wordlist[i].lower() in word_counter.keys():
        word_counter[wordlist[i]] += 1
    else:
        word_counter[wordlist[i]] = 1

print(word_counter)

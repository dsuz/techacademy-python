file = './ch13.txt'
with open(file) as fileobj:
    text = fileobj.read()
    text = text.replace('-', ' ').replace('\n', ' ').replace('\r', '').replace('.', '').replace(',', '')
    wordlist = text.split(' ')
    print(wordlist)

    word_counter = {}
    for i in range(len(wordlist)):
        if wordlist[i].lower() in word_counter.keys():
            word_counter[wordlist[i].lower()] += 1
        else:
            word_counter[wordlist[i].lower()] = 1

    print(word_counter)
    
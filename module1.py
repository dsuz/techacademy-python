text = 'Fuzzy Wuzzy was a bear. Fuzzy Wuzzy had no hair. Fuzzy Wuzzy wasnt fuzzy, was he?'
text = text.lower().replace('-', ' ').replace(',', ' ').replace('.', '').replace('?', '')
wordlist = text.split(' ')
print(wordlist)

word_counter = {}   # 辞書 word_counter を定義する。辞書については Chapter9 を参照

for i in range(len(wordlist)):  # wordlist 内の全ての単語に対して処理をする
    if wordlist[i] in word_counter.keys():  # 単語が word_counter のキーとして登録されているか調べる 
        word_counter[wordlist[i]] += 1  # 単語が既に登録されていた場合は値を 1 増やす
    else:
        word_counter[wordlist[i]] = 1   # 単語が登録されていなかったら登録して値に 1 を割り当てる
        print (word_counter.keys())

# print(word_counter)

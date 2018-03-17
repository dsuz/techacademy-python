# coding:utf-8
#import tkinter as tk
#import tkinter.filedialog as fd

#root = tk.Tk()
#root.withdraw()

f = open('ch13.txt')
data = f.read()

words = {}
for word in data.split():
    words[word] = words.get(word, 0) + 1

# sort by count
d = [(v,k) for k,v in words.items()]
d.sort()
d.reverse()
for count, word in d:
    print(count, word)
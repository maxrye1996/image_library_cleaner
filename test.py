from textblob import Word

word = Word("back")
print(word.spellcheck()[0][1])


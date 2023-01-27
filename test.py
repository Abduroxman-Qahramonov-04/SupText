from spellchecker import SpellChecker
from textblob import TextBlob

import re
from string import digits

spell = SpellChecker("en")
docx = input("Enter everything:")

#Removing digits from string

remove_digits = str.maketrans('', '', digits)
res = docx.translate(remove_digits)
all_words = res.split()

misspelled = spell.unknown(all_words)

print(misspelled)

# correcting words

new_doc = TextBlob(res)
result = new_doc.correct()


print(result)
# misspelled = "{'hello','my'}"
# n = misspelled[1: len(misspelled)-1]
# print(type(n))


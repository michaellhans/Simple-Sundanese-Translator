# Modul Pattern Matching Metode 3: Regular Expression

import re

# Fungsi / Prosedur
# Mencari pattern dalam text dengan metode regex
def RegexPatternMatching(text, pattern):
    found = re.search(pattern, text)
    return found

# Mengembalikan kalimat-kalimat yang mengandung pattern
def GetPatternRegex(sentence, pattern):
    sentencePattern = []
    for i in range(len(sentence)):
        if (RegexPatternMatching(sentence[i], pattern)):
            sentencePattern.append(sentence[i])
    return sentencePattern
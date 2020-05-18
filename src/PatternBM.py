# Modul Pattern Matching Metode 1: Boyer-Moore

# Fungsi / Prosedur
# Mengembalikan posisi kemunculan terakhir character dalam pattern
def GetLastOccurance(pattern, character):
    position = -1
    n = len(pattern) - 1
    while ((n >= 0) and (position == -1)):
        if (pattern[n] == character):
            position = n
        else:
            n = n - 1
    return position

# Mengembalikan map berisi last occurance dari setiap karakter unik dari text dalam pattern
def BMLastOccurance(text, pattern):
    lastOccurance = {}
    uniqueText = list(set(text))
    for char in uniqueText:
        value = GetLastOccurance(pattern, char)
        lastOccurance.update({char : value})
    return lastOccurance

# Mengembalikan True apabila pattern ditemukan dalam text
def BMPatternMatching(text, pattern):
    lastOccurance = {}
    lastOccurance = BMLastOccurance(text,pattern)
    count = 0
    lengthText = len(text)
    lengthPattern = len(pattern)
    i = lengthPattern - 1
    while (i < lengthText):
        j = lengthPattern - 1
        while ((j >= 0) and (i < lengthText)):
            if (text[i] == pattern[j]):
                i -= 1
                j -= 1
            else:
                lastPosition = lastOccurance.get(text[i])
                if (lastPosition < j):
                    i = i + (lengthPattern - 1) - lastPosition
                elif (lastPosition > j):
                    i = i + lengthPattern - j
                else:
                    i = i + 1
                j = lengthPattern - 1
        i += 1
        if (j < 0):
            return True
    return False

# Mengembalikan kalimat-kalimat yang mengandung pattern
def GetPatternBMSentence(sentence, pattern):
    sentencePattern = []
    for i in range(len(sentence)):
        if (BMPatternMatching(sentence[i], pattern)):
            sentencePattern.append(sentence[i])
    return sentencePattern

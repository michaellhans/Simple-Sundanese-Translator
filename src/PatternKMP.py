# Modul Pattern Matching Metode 2: Algoritma KMP

# Fungsi / Prosedur
# Mengembalikan list of prefix dan suffix dari sebuah pattern
def PrefixSuffixInit(pattern, k):
    prefix = []
    suffix = []
    for i in range (k+1):
        presub = ""
        sufsub = ""
        for j in range (i+1):
            presub = presub + pattern[j]
            sufsub = pattern[k-j] + sufsub
        prefix.append(presub)
        suffix.append(sufsub)
    suffix.pop()
    return prefix, suffix

# Mengembalikan list yang berisi border function
def KMPBorderFunction(pattern):
    length = len(pattern)
    borderFunction = []
    for i in range (1, length):
        prefix = []
        suffix = []
        k = i-1
        prefix, suffix = PrefixSuffixInit(pattern, k)
        maxLength = 0
        for j in range (k):
            if (prefix[j] == suffix[j]):
                maxLength = len(prefix[j])
        borderFunction.insert(k,maxLength)
    return borderFunction

# Mencari banyaknya pattern dalam sebuah text
def KMPPatternMatching(text, pattern):
    borderFunction = KMPBorderFunction(pattern)
    count = 0
    lengthText = len(text)
    lengthPattern = len(pattern)
    i = 0
    while (i < lengthText):
        j = 0
        while ((j < lengthPattern) and (i < lengthText)):
            if (text[i] == pattern[j]):
                i += 1
                j += 1
            elif (j > 0):
                j = borderFunction[j-1]
            else:
                j = 0
                i += 1
        if (j >= lengthPattern):
            return True
    return False

# Mengembalikan kalimat-kalimat yang mengandung pattern
def GetPatternKMPSentence(sentence, pattern):
    sentencePattern = []
    for i in range(len(sentence)):
        if (KMPPatternMatching(sentence[i], pattern)):
            sentencePattern.append(sentence[i])
    return sentencePattern

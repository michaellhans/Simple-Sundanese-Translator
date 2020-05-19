# Load Vocabulary Module

from PatternBM import *
from PatternKMP import *
from PatternRegex import *

# Load Sunda Vocabulary
def LoadVocabulary(fileName) :
    f = open("../test/"+fileName, "r")
    text = f.read()
    f.close()
    vocab = {}
    x = text.split("\n")
    for grammar in x:
        temp = []
        temp = grammar.split(" = ")
        vocab.update({temp[0] : temp[1]})
    return vocab

# Pattern Matching sorted by user choice
def PatternMatching(text, pattern, choice):
    if (choice == 1):
        return BMPatternMatching(text, pattern)
    elif (choice == 2):
        return KMPPatternMatching(text, pattern)
    elif (choice == 3):
        return RegexPatternMatching(text, pattern)

# Translate Sunda into Indonesia
def SundaToIndoTranslator(buffer, SundaToIndo, choice):
    result = buffer.split(" ")
    for i in range(len(result)):
        found = False
        newWord = ""
        for grammar in SundaToIndo:
            if (PatternMatching(result[i], grammar, choice)):
                found = True
                print(result[i], grammar)
                newWord = SundaToIndo[grammar]
                break
        if (found):
            result[i] = newWord
        print(result)

    final = ""
    if (len(result) != 0):
        final = final + result[0]
        for i in range(1, len(result)):
            final = final + " " + result[i]
    return final

# Translate Indonesia to Sunda
def IndoToSundaTranslator(buffer, IndoToSunda, choice):
    result = buffer.split(" ")
    for i in range(len(result)):
        found = False
        newWord = ""
        for grammar in IndoToSunda:
            if (PatternMatching(result[i], grammar, choice)):
                found = True
                print(result[i], grammar)
                newWord = IndoToSunda[grammar]
                break
        if (found):
            result[i] = newWord
        print(result)

    final = ""
    if (len(result) != 0):
        final = final + result[0]
        for i in range(1, len(result)):
            final = final + " " + result[i]
    return final

# Load Vocabulary Indonesia-Sunda and Sunda-Indonesia
IndoToSunda = {}
SundaToIndo = {}
IndoToSunda = LoadVocabulary("indonesia.txt")
SundaToIndo = LoadVocabulary("sunda.txt")

# Choose preference method for pattern matching
print("Simple Sundanese Translator")
print("Created by: 13518056 - Michael Hans")
print("Terdapat 3 buah metode pencocokan string:")
print("1. Algoritma Boyer-Moore")
print("2. Algoritma KMP")
print("3. Regular Expression")
choice = int(input("Masukkan pilihan metode pencocokan string: "))

# Choose Translation Method
print("Terdapat 2 metode penerjemahan:")
print("1. Sunda-Indonesia")
print("2. Indonesia-Sunda")
method = int(input("Masukkan pilihan metode: "))

# Input text that want to be translated
buffer = input("Input text: ")
if (method == 1):
    result = SundaToIndoTranslator(buffer, SundaToIndo, choice)
    print("Sunda     :", buffer)
    print("Indonesia :", result)
else:
    result = IndoToSundaTranslator(buffer, IndoToSunda, choice)
    print("Indonesia :", buffer)
    print("Sunda     :", result)
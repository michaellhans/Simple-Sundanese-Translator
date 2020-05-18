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

# Translate Sunda into Indonesia
def SundaToIndoTranslator(buffer, SundaToIndo, choice):
    result = buffer.split(" ")
    if (choice == 1):
        for i in range(len(result)):
            found = False
            newWord = ""
            for grammar in SundaToIndo:
                if (BMPatternMatching(grammar, result[i])):
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
                
    # elif (choice == 2):
    #     for grammar in SundaToIndo:
    #         if (KMPPatternMatching(result, grammar)):
    #             result = result.replace(grammar, SundaToIndo[grammar])
    # elif (choice == 3):
    #     for grammar in SundaToIndo:
    #         if (RegexPatternMatching(result, grammar)):
    #             result = result.replace(grammar, SundaToIndo[grammar])
    return final

# def IndoToSundaTranslator(buffer, IndoToSunda, choice):


# Translate Indonesia into Sunda
IndoToSunda = {}
SundaToIndo = {}
IndoToSunda = LoadVocabulary("indonesia.txt")
SundaToIndo = LoadVocabulary("sunda.txt")

print("Terdapat 3 buah metode pencocokan string:")
print("1. Algoritma Boyer-Moore")
print("2. Algoritma KMP")
print("3. Regular Expression")
choice = int(input("Masukkan pilihan metode pencocokan string: "))

print("Terdapat 2 metode penerjemahan:")
print("1. Indonesia-Sunda")
print("2. Sunda-Indonesia")
method = int(input("Masukkan pilihan metode: "))
buffer = input("Input text: ")
result = SundaToIndoTranslator(buffer, SundaToIndo, choice)
print(SundaToIndo.get("ti"))
print("Hasil :",result)



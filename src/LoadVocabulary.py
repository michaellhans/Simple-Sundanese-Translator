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
    if (choice == "Algoritma Boyers-Moore"):
        return BMPatternMatching(text, pattern)
    elif (choice == "Algoritma Knuth-Morris-Pratt"):
        return KMPPatternMatching(text, pattern)
    elif (choice == "Regular Expression"):
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
                # print(result[i], grammar)
                newWord = SundaToIndo[grammar]
                break
        if (found):
            result[i] = newWord
        # print(result)

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
                # print(result[i], grammar)
                newWord = IndoToSunda[grammar]
                break
        if (found):
            result[i] = newWord
        # print(result)

    final = ""
    if (len(result) != 0):
        final = final + result[0]
        for i in range(1, len(result)):
            final = final + " " + result[i]
    return final

# Memulai proses penerjemahan
def BeginTranslation(SunIndVocab, IndSunVocab, Translator, choice, buffer):
    # Load Vocabulary
    SundaToIndo = {}
    IndoToSunda = {}
    SundaToIndo = LoadVocabulary(SunIndVocab)
    IndoToSunda = LoadVocabulary(IndSunVocab)

    # Translator
    if (Translator == "Sunda-Indonesia"):
        result = SundaToIndoTranslator(buffer, SundaToIndo, choice)
    elif (Translator == "Indonesia-Sunda"):
        result = IndoToSundaTranslator(buffer, IndoToSunda, choice)
    return result
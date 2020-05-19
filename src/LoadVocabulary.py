# Load Vocabulary Module

from PatternBM import *
from PatternKMP import *
from PatternRegex import *
import random

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

# Clear stop words like 'teh' or 'mah'
def ClearStopWords(buffer):
    if ("teh" in buffer):
        buffer.remove("teh")
    elif ("mah" in buffer):
        buffer.remove("mah")

# Add stop words like 'teh' or 'mah'
def AddStopWords(buffer, grammar):
    n = random.randint(0,1)
    if (n == 1):
        if (grammar == "apa"):
            return "teh " + buffer
        else: 
            return buffer + " teh"
    else:
        if (grammar == "apa"):
            return "mah " + buffer
        else: 
            return buffer + " mah"

# Translate Sunda into Indonesia
def SundaToIndoTranslator(buffer, SundaToIndo, choice):
    result = buffer.split(" ")
    ClearStopWords(result)
    for i in range(len(result)):
        found = False
        newWord = ""
        for grammar in sorted (SundaToIndo.keys(), key=len, reverse=True):
            if (PatternMatching(result[i], grammar, choice)):
                found = True
                print(result[i]," = ",grammar)
                newWord = SundaToIndo[grammar]
                break
        if (found):
            temp = result[i]
            temp = temp.replace(grammar, newWord)
            result[i] = temp

    final = ""
    if (len(result) != 0):
        final = final + result[0]
        for i in range(1, len(result)):
            final = final + " " + result[i]
    return final

# Translate Indonesia to Sunda
def IndoToSundaTranslator(buffer, IndoToSunda, choice):
    penekanan = ["saya", "kamu", "kita", "apa"]
    IsAlreadyPenekanan = False
    result = buffer.split(" ")
    for i in range(len(result)):
        found = False
        newWord = ""
        for grammar in sorted (IndoToSunda.keys(), key=len, reverse=True):
            if (PatternMatching(result[i], grammar, choice)):
                found = True
                print(result[i]," = ",grammar)
                newWord = IndoToSunda[grammar]
                break
        if (found):
            temp = result[i]
            temp = temp.replace(grammar, newWord)
            result[i] = temp
            if ((grammar in penekanan) and not(IsAlreadyPenekanan)):
                result[i] = AddStopWords(result[i], grammar)
                IsAlreadyPenekanan = True

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
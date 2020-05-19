# Asisten Ilmu dan Rekayasa Komputasi
# Pengujian Program melalui Command Prompt (Back End Test)
# Created by: 13518056 / Michael Hans

from PatternBM import *
from PatternKMP import *
from PatternRegex import *
from LoadVocabulary import *

# Main Back End Program
print("Simple Sundanese Translator")
print("Created by: 13518056 - Michael Hans")
print()
SIVFilename = input("Masukkan nama file Sunda-Indo Vocabulary: ")
ISVFilename = input("Masukkan nama file Indo-Sunda Vocabulary: ")

# Load Vocabulary Indonesia-Sunda and Sunda-Indonesia
SundaToIndo = {}
IndoToSunda = {}
SundaToIndo = LoadVocabulary(SIVFilename)
IndoToSunda = LoadVocabulary(ISVFilename)

# for grammar in sorted (SundaToIndo.keys(), key=len, reverse=True):
#     print(grammar, SundaToIndo[grammar])

# Choose preference method for pattern matching
print()
print("Terdapat 3 buah metode pencocokan string:")
print("1. Algoritma Boyers-Moore")
print("2. Algoritma KMP")
print("3. Regular Expression")
choiceInt = int(input("Masukkan pilihan metode pencocokan string: "))
if (choiceInt == 1):
    choice = "Algoritma Boyers-Moore"
elif (choiceInt == 2):
    choice = "Algoritma Knuth-Morris-Pratt"
else:
    choice = "Regular Expression"

# Choose translation Method
print()
print("Terdapat 2 metode penerjemahan:")
print("1. Sunda-Indonesia")
print("2. Indonesia-Sunda")
translatorInt = int(input("Masukkan pilihan metode penerjemahan: "))
if (translatorInt == 1):
    translator = "Sunda-Indonesia"
else:
    translator = "Indonesia-Sunda"

# Translator for Back End
print()
buffer = input("Input text: ")
print()
print("=== Back End Test Module ===")
if (translatorInt == 1):
    result = SundaToIndoTranslator(buffer, SundaToIndo, choice)
    print("Sunda     :", buffer)
    print("Indonesia :", result)
else:
    result = IndoToSundaTranslator(buffer, IndoToSunda, choice)
    print("Indonesia :", buffer)
    print("Sunda     :", result)

# Begin Translation for Front End
print()
print("=== Front End Test Module ===")
if (translator == "Sunda-Indonesia"):
    result = BeginTranslation(SIVFilename, ISVFilename, translator, choice, buffer)
    print("Sunda     :", buffer)
    print("Indonesia :", result)
else:
    result = BeginTranslation(SIVFilename, ISVFilename, translator, choice, buffer)
    print("Indonesia :", buffer)
    print("Sunda     :", result)
# Asisten Ilmu dan Rekayasa Komputasi
# Pengujian Program melalui Command Prompt
# Created by: 13518056 / Michael Hans

from PatternBM import *
from PatternKMP import *
from PatternRegex import *
from LoadVocabulary import *

# Load Vocabulary Indonesia-Sunda and Sunda-Indonesia
IndoToSunda = {}
SundaToIndo = {}
IndoToSunda = LoadVocabulary("indonesia.txt")
SundaToIndo = LoadVocabulary("sunda.txt")

# Choose preference method for pattern matching
print("Simple Sundanese Translator")
print("Created by: 13518056 - Michael Hans")
print("Terdapat 3 buah metode pencocokan string:")
print("1. Algoritma Boyers-Moore")
print("2. Algoritma KMP")
print("3. Regular Expression")
choiceInt = int(input("Masukkan pilihan metode pencocokan string: "))
if (choiceInt == 1):
    choice = "Algoritma Boyers-Moore"
elif (choiceInt == 2):
    choice = "Algoritma Knuth-Morris-Pratt"
elif (choiceInt == 3):
    choice = "Regular Expression"

# Choose Translation Method
print("Terdapat 2 metode penerjemahan:")
print("1. Sunda-Indonesia")
print("2. Indonesia-Sunda")
method = int(input("Masukkan pilihan metode: "))

# Input text that want to be translated
buffer = input("Input text: ")
if (method == 1):
    print(choice)
    result = SundaToIndoTranslator(buffer, SundaToIndo, choice)
    print("Sunda     :", buffer)
    print("Indonesia :", result)
else:
    result = IndoToSundaTranslator(buffer, IndoToSunda, choice)
    print("Indonesia :", buffer)
    print("Sunda     :", result)

result = BeginTranslation("sunda.txt", "indonesia.txt", "Sunda-Indonesia", "Algoritma Boyers-Moore", buffer)
print(result)
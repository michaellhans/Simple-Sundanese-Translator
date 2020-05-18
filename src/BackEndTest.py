# IF2211 - Strategi Algoritma
# Tugas Kecil 4 - Ekstraksi Informasi dengan KMP
# Pengujian Program melalui Command Prompt
# Created by: 13518056 / Michael Hans

from PatternBM import *
from PatternKMP import *
from PatternRegex import *
from ExtractorData import *
from ExtractorApp import *

# # Kamus Data
pattern = []            # menyimpan nilai dari pattern
text = []               # menyimpan string dari sebuah text yang dibaca
sentence = []           # menyimpan daftar kalimat yang telah diparsing
sentencePattern = []    # menyimpan daftar kalimat yang mempunyai pattern

# Algoritma Utama
print("IF2211 - Strategi Algoritma")
print("Tugas Kecil 4 - Ekstraksi Informasi")
print("Sthyrelest - Data Extractor Application")
print("Created by: 13518056 / Michael Hans")
print()
pattern = input("Masukkan pattern yang diinginkan: ")
fileName = input("Masukkan nama file yang ingin dibaca: ")
print("Terdapat 3 buah metode pencocokan string:")
print("1. Algoritma Boyer-Moore")
print("2. Algoritma KMP")
print("3. Regular Expression")
choice = int(input("Masukkan pilihan metode pencocokan string: "))
print()
text = ReadText(fileName)
text = text.lower()
sentence = sent_tokenize(text)

# Pattern Matching
if (choice == 1):
    sentencePattern = GetPatternBMSentence(sentence, pattern)
elif (choice == 2):
    sentencePattern = GetPatternKMPSentence(sentence, pattern)
elif (choice == 3):
    sentencePattern = GetPatternRegex(sentence, pattern)

if len(sentencePattern) == 0:
    print("Pencarian tidak ditemukan")
else:
    # Extraction Data
    for i in range(len(sentencePattern)):
        print(str(i+1)+". ",sentencePattern[i].capitalize())
        jumlah = FindNumber(sentencePattern[i])
        tanggal = FindDate(sentencePattern[i])
        print("Jumlah   : ", jumlah.capitalize())
        print("Tanggal  : ", tanggal.capitalize())
        print()
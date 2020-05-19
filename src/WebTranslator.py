# Calon Asisten Ilmu dan Rekayasa Komputasi
# Menu Program Utama : Web Translator
# Terintegrasi dengan HTML dan Python dengan Flask Framework
# Created by: 13518056 / Michael Hans

from flask import Flask, redirect, render_template, url_for, request
from LoadVocabulary import *

# Generate HTML Based on Flask
app = Flask(__name__)

# Halaman Web Bagian Home / Menu Awal
@app.route("/", methods=["POST","GET"])
@app.route("/home", methods=["POST","GET"])
def home():
    if request.method == "POST":
        SunIndVocab = request.form['SunInd']
        IndSunVocab = request.form['IndSun']
        Translator = request.form['translatemethod']
        method = request.form['matchmethod']
        buffer = request.form['buffer']
        return redirect(url_for("result", SIV = SunIndVocab, ISV = IndSunVocab, Trs = Translator, ptr = method, inputtext = buffer))
    return render_template('home.html')

# Halaman Web Bagian Hasil Terjemahan
@app.route("/result")
def result():
    SunIndVocab = request.args.get('SIV')
    IndSunVocab = request.args.get('ISV')
    Translator = request.args.get('Trs')
    method = request.args.get('ptr')
    buffer = request.args.get('inputtext')
    result = BeginTranslation(SunIndVocab, IndSunVocab, Translator, method, buffer)
    return render_template("result.html", translator = Translator, pattern = method, buffer = buffer, result = result)
    
# Halaman Web Bagian Guide Line / How To Use
@app.route("/guideline")
def guideline():
    return render_template('guideline.html', title='About')

# Menjalankan Aplikasi
if __name__ == '__main__':
    app.run(debug=True)
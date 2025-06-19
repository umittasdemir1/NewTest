from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['file']
    df = pd.read_excel(file)
    analysis_type = request.form.get('analysis')

    if analysis_type == 'sales':
        result = df['Ürün'].value_counts().to_frame(name='Adet').to_html()
    elif analysis_type == 'lift':
        urun1 = request.form.get('urun1')
        urun2 = request.form.get('urun2')
        result = f"{urun1} ve {urun2} için lift hesaplaması henüz eklenmedi."
    elif analysis_type == 'pair':
        result = "Pair analizi henüz yazılmadı."
    elif analysis_type == 'time':
        result = "Zaman bazlı analiz henüz eklenmedi."
    elif analysis_type == 'customer':
        result = "Müşteri tipi analizi henüz yazılmadı."
    else:
        result = "Geçersiz analiz türü."

    return result

if __name__ == '__main__':
    app.run(debug=True)

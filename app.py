from flask import Flask, request, render_template_string
import pandas as pd

app = Flask(__name__)

HTML_FORM = """
<!DOCTYPE html>
<html>
<head>
    <title>Excel Analizi</title>
</head>
<body>
    <h2>Excel Dosyası Yükle ve Analiz Et</h2>
    <form action="/analyze" method="POST" enctype="multipart/form-data">
        <label>Dosya:</label>
        <input type="file" name="file" required><br><br>
        
        <label>Analiz Türü:</label>
        <select name="analysis">
            <option value="sales">Ürün Satış Analizi</option>
            <option value="lift">Sepet Analizi (Lift)</option>
            <option value="pair">Birlikte Satılan Ürünler</option>
            <option value="time">Zaman Bazlı Satış</option>
            <option value="customer">Müşteri Tipi Analizi</option>
        </select><br><br>

        <label>Ürün 1:</label>
        <input type="text" name="urun1"><br><br>
        <label>Ürün 2:</label>
        <input type="text" name="urun2"><br><br>

        <input type="submit" value="Gönder ve Analiz Et">
    </form>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    return render_template_string(HTML_FORM)

@app.route("/analyze", methods=["POST"])
def analyze():
    file = request.files["file"]
    analysis_type = request.form.get("analysis")
    urun1 = request.form.get("urun1")
    urun2 = request.form.get("urun2")

    df = pd.read_excel(file)
    
    result = f"""
    <h3>Analiz Türü: {analysis_type}</h3>
    <p>Ürün 1: {urun1}</p>
    <p>Ürün 2: {urun2}</p>
    <h4>Dosya Önizlemesi:</h4>
    {df.head().to_html()}
    """
    return result

if __name__ == "__main__":
    app.run(debug=True)

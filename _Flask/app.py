from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# JSON dosyasından yazıları oku
def yazilari_yukle():
    with open('blog_posts.json', 'r') as dosya:
        return json.load(dosya)

# JSON dosyasına yazıları yaz
def yazilari_kaydet(yazilar):
    with open('blog_posts.json', 'w') as dosya:
        json.dump(yazilar, dosya)

# Tüm yazıları listele
@app.route('/yazilar', methods=['GET'])
def tum_yazilar():
    yazilar = yazilari_yukle()
    return jsonify(yazilar)

# Yeni bir yazı ekle
@app.route('/yazilar', methods=['POST'])
def yaz_ekle():
    yeni_yazi = request.get_json()
    yazilar = yazilari_yukle()
    yeni_yazi['id'] = len(yazilar) + 1
    yazilar.append(yeni_yazi)
    yazilari_kaydet(yazilar)
    return jsonify(yeni_yazi), 201

# Belirli bir yazıyı getir
@app.route('/yazilar/<int:id>', methods=['GET'])
def yazi_getir(id):
    yazilar = yazilari_yukle()
    yazi = next((y for y in yazilar if y['id'] == id), None)
    if yazi:
        return jsonify(yazi)
    return jsonify({'mesaj': 'Yazı bulunamadı!'}), 404

# Yazıyı güncelle
@app.route('/yazilar/<int:id>', methods=['PUT'])
def yazi_guncelle(id):
    yazilar = yazilari_yukle()
    yazi = next((y for y in yazilar if y['id'] == id), None)
    if yazi:
        guncel_yazi = request.get_json()
        yazi.update(guncel_yazi)
        yazilari_kaydet(yazilar)
        return jsonify(yazi)
    return jsonify({'mesaj': 'Yazı bulunamadı!'}), 404

# Yazıyı sil
@app.route('/yazilar/<int:id>', methods=['DELETE'])
def yazi_sil(id):
    yazilar = yazilari_yukle()
    yazilar = [y for y in yazilar if y['id'] != id]
    yazilari_kaydet(yazilar)
    return jsonify({'mesaj': 'Yazı silindi!'}), 204

if __name__ == '__main__':
    app.run(debug=True)

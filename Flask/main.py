from flask import Flask, render_template

ilkproje = Flask(__name__)

@ilkproje.route("/")
def anasayfa():
    return render_template("index.html") 

@ilkproje.route("/iletisim")
def iletisim():
    metin = """
    İletişim<br/>
    <p>
    Oben SEVEN<br/>
    Tel: 0 555 555 55 55<br/>
    E-mail: obenseven@obenseven.com.tr</p>
    """
    return metin

if __name__ == '__main__':
    ilkproje.run(debug=True)
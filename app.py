from flask import Flask, request, render_template, send_file
import qrcode
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_qr():
    text = request.form['text']
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save QR code image
    img_path = "static/qr_code.png"
    img.save(img_path)
    
    return render_template('index.html', qr_code=img_path)

if __name__ == '__main__':
    app.run(debug=True)

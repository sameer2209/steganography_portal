import os
from flask import Flask, render_template, request, flash
from werkzeug import secure_filename
app = Flask(__name__)

UPLOAD_FOLDER = "uploads/"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/encryption_uploader', methods = ['GET', 'POST'])
def encryption_uploader():
    if request.method == 'POST':
        cover = request.files['cover']
        secret = request.files['secret']
        cover.save(os.path.join(app.config['UPLOAD_FOLDER'], "cover.png"))
        secret.save(os.path.join(app.config['UPLOAD_FOLDER'], "secret.png"))
        return "Cover and Secret Uploaded Succesfully"

@app.route('/decryption_uploader', methods = ['GET', 'POST'])
def decryption_uploader():
    if request.method == 'POST':
        stego = request.files['stego']
        stego.save(os.path.join(app.config['UPLOAD_FOLDER'], "stego.png"))
        return "Stego Uploaded Succesfully"

@app.route('/encrypt')
def encrypt():
    print("Encrypting image....")
    return render_template("home.html")

@app.route('/decrypt')
def decrypt():
    print("Decrypting image...")
    return render_template("home.html")
app.run()

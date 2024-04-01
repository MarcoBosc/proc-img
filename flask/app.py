import os
import requests
from flask import Flask, redirect, url_for, render_template, send_from_directory, request, send_file

from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
#pip install flask-reuploaded flask-wtf

from PIL import Image
from io import BytesIO
import numpy as np

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['UPLOADED_PHOTOS_DEST'] = 'uploads'

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

class UploadForm(FlaskForm):
    photo = FileField(
        validators=[
            FileAllowed(photos, "Apenas imagens são permitidas."),
            FileRequired('Por favor, selecione uma imagem.')
        ]
    )
    submit = SubmitField('Upload')
    
    
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/pricing")
def pricing():
    return render_template("pricing.html")

@app.route('/static/uploads/<filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)

@app.route('/editor', methods=['GET', 'POST'])
def upload_image():
    form = UploadForm()
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = url_for('get_file', filename=filename)
    else:
        file_url = None
        
    return render_template('editor.html', form=form, file_url=file_url)


@app.route('/negative_image')
def negative_image():
    file_url = request.args.get('file_url')
    
    # Verifique se o URL do arquivo foi passado corretamente
    if not file_url:
        return "URL do arquivo não foi fornecido.", 400  # Retorna um erro HTTP 400 Bad Request
    
    try:
        # Abra a imagem usando PIL
        response = requests.get("http://127.0.0.1:5000" + file_url)
        if response.status_code != 200:
            return "Falha ao baixar a imagem.", 500
        image = Image.open(BytesIO(response.content))
        image_array = np.array(image)
        for row in image_array:
            for pixel in row: # pixel é uma tupla contendo os valores do canal de cor (R, G, B)
                pixel[0] = 255 - pixel[0] # Negativando o canal vermelho
                pixel[1] = 255 - pixel[1] # Negativando o canal verde
                pixel[2] = 255 - pixel[2] # Negativando o canal azul
                
        # Criar uma nova imagem a partir da matriz NumPy modificada
        image_negativa = Image.fromarray(image_array)
        
        # Salvar a imagem em um buffer
        img_io = BytesIO()
        image_negativa.save(img_io, 'JPEG')
        img_io.seek(0)
        
        return send_file(img_io, mimetype='image/jpeg')
    
    except Exception as e:
        return str(e), 500  # Retorna um erro HTTP 500 Internal Server Error com a mensagem de erro


@app.route('/gray_scale')
def gray_scale():
    file_url = request.args.get('file_url')
    
    # Verifique se o URL do arquivo foi passado corretamente
    if not file_url:
        return "URL do arquivo não foi fornecido.", 400  # Retorna um erro HTTP 400 Bad Request
    
    try:
        # Abra a imagem usando PIL
        response = requests.get("http://127.0.0.1:5000" + file_url)
        if response.status_code != 200:
            return "Falha ao baixar a imagem.", 500
        image = Image.open(BytesIO(response.content))
        image_array = np.array(image)
        new_image = []
        for row in image_array:
            for pixel in row:
                average = (pixel[0] + pixel[1] + pixel[2]) / 3
                new_image.append(average)
        # Criar uma nova imagem a partir da matriz NumPy modificada
        image_negativa = Image.fromarray(new_image)
        
        # Salvar a imagem em um buffer
        img_io = BytesIO()
        image_negativa.save(img_io, 'JPEG')
        img_io.seek(0)
        
        return send_file(img_io, mimetype='image/jpeg')
    
    except Exception as e:
        return str(e), 500  # Retorna um erro HTTP 500 Internal Server Error com a mensagem de erro



# @app.route("/<name>")
# def user(name):
#     return f"Hello {name}!"

# @app.route("/admin")
# def admin():
#     return redirect(url_for("home"))

# @app.route("/supah_usah")
# def supah_usah():
#     return redirect(url_for("user", name="Admin!"))

if __name__ == "__main__":
    app.run(debug=True)
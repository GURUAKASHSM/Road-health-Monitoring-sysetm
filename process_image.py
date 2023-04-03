from flask import Flask, request, jsonify
import base64
import io
from PIL import Image

app = Flask(__name__)

@app.route('/process_image.py', methods=['POST'])
def process_image():
    # Get the image data from the POST parameter
    imageData = request.form['imageData']
    imageData = imageData.replace('data:image/png;base64,', '')

    # Convert the image data to a PIL image
    image = Image.open(io.BytesIO(base64.b64decode(imageData)))

    # Convert the image to grayscale
    grayImage = image.convert('L')

    # Convert the grayscale image to a data URL and return it
    buffered = io.BytesIO()
    grayImage.save(buffered, format="PNG")
    data = base64.b64encode(buffered.getvalue()).decode()
    return 'data:image/png;base64,' + data

if __name__ == '__main__':
    app.run()
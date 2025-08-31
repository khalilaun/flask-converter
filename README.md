Flask Image Converter

Image Converter Link: https://flask-converter-2.onrender.com

Description:
This project is a web application built with Flask that allows users to upload images and convert them to different formats. The app supports JPEG, PNG, BMP, GIF, TIFF, and WEBP. Users can drag and drop an image or click to select a file, choose the desired format using a bubble-style selector, and download the converted image. The app also provides feedback by showing the uploaded file name and a preview of the image.

Features:
- Upload images via drag-and-drop or file selection.
- Select conversion format using an interactive bubble interface.
- Preview uploaded image before conversion.
- Download converted image in the selected format.
- Handles images with alpha channels correctly when converting to formats like JPEG.

Technologies Used:
- Python 3.13
- Flask 3.1.2
- Pillow 11.3.0 for image processing
- HTML, CSS, and JavaScript for the frontend
- Gunicorn for deployment on Render

How to Run Locally:
1. Clone the repository:
   git clone https://github.com/khalilaun/flask-converter
2. Navigate to the project folder:
   cd flask-converter
3. Install dependencies:
   pip install -r requirements.txt
4. Run the Flask app:
   python app.py
5. Open your browser and go to:
   http://127.0.0.1:5000

Deployment:
- The app is deployed on Render at:
  https://flask-converter-2.onrender.com
- Ensure the requirements.txt file includes gunicorn for deployment.

Notes:
- Make sure to select an output format before converting.
- Images with transparency (RGBA) are automatically converted to RGB when converting to formats that do not support alpha channels, like JPEG.

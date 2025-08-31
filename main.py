from flask import Flask, request, send_file, render_template
from PIL import Image
import io
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        fmt = request.form["format"]  # JPEG, PNG, etc.
        image = Image.open(file)

        # Handle RGBA → JPEG transparency
        if fmt.upper() == "JPEG" and image.mode in ("RGBA", "LA"):
            background = Image.new("RGB", image.size, (255, 255, 255))
            background.paste(image, mask=image.split()[3])
            image = background
        else:
            if image.mode not in ("RGB", "L"):
                image = image.convert("RGB")

        # Save to in-memory buffer
        buffer = io.BytesIO()
        image.save(buffer, format=fmt)
        buffer.seek(0)

        # Preserve original filename
        original_name = os.path.splitext(file.filename)[0]
        download_name = f"{original_name}_converted.{fmt.lower()}"

        # Send the file
        return send_file(buffer, download_name=download_name, as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

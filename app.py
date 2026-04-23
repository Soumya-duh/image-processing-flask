from flask import Flask, render_template, request
import os
from processor import process_image

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)   # ✅ ensure folder exists
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    outputs = []
    filepath = None

    if request.method == 'POST':
        file = request.files['file']
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        outputs = process_image(filepath)

    return render_template('index.html', outputs=outputs, original=filepath)

# ✅ ONLY ONE main block
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
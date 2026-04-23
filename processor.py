import cv2
import os
import time

def process_image(image_path):
    img = cv2.imread(image_path)
    scales = [0.3, 0.6, 1.0]

    output_paths = []

    # ✅ ensure outputs folder exists
    os.makedirs("static/outputs", exist_ok=True)

    # create unique name
    timestamp = int(time.time())

    for scale in scales:
        resized = cv2.resize(img, None, fx=scale, fy=scale)
        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150)

        output_file = f"static/outputs/edge_{scale}_{timestamp}.jpg"
        cv2.imwrite(output_file, edges)

        output_paths.append(output_file)

    return output_paths
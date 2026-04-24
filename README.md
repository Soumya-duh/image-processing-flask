# Multi-Scale Image Processing using Flask and OpenCV

## Project Overview
This project is a web-based image processing application that demonstrates how images behave at different scales after converting to grayscale and applying edge detection. The system allows users to upload an image and view edge detection results at multiple scales.

The application is built using **Python, Flask, and OpenCV** and deployed online using Render.

---

## Problem Statement
Images with different textures and contrast levels produce different edge detection results. This project demonstrates how scaling and grayscale conversion affect edge detection in various real-world images such as documents, crumpled receipts, and medical scans.

---

## Aim
To develop a web-based image processing system that performs multi-scale edge detection on uploaded images and visually demonstrates the effect of image scaling and grayscale processing.

---

## Technologies Used
- Python
- Flask
- OpenCV
- NumPy
- HTML / CSS
- Gunicorn
- Render (Deployment)
- GitHub (Version Control)

---

## Project Structure
image-processing-flask
│
├── app.py
├── processor.py
├── requirements.txt
├── Procfile
│
├── templates
│ └── index.html
│
└── static
├── uploads
└── outputs

---

## How the System Works

1. User uploads an image through the web interface.
2. The Flask server receives the image.
3. The image is resized to different scales:
   - 0.3
   - 0.6
   - 1.0
4. Each scaled image is converted to **grayscale**.
5. **Canny Edge Detection** is applied.
6. Processed images are displayed on the webpage.

---

## Image Processing Pipeline

1. Image Upload  
2. Image Scaling  
3. Grayscale Conversion  
4. Edge Detection (Canny Algorithm)  
5. Display Output Images  

---

## Real World Applications

### Medical Imaging
X-rays and MRI scans are often grayscale. Edge detection helps highlight abnormal structures and tumors.

### Document Analysis
Edge detection helps detect text boundaries and document edges in scanned receipts or notes.

### Surveillance Systems
Used in CCTV systems to detect object boundaries and motion changes.

---

## Example Test Images
The project was tested using:
- Notebook page (high contrast)
- Crumpled receipt (irregular edges)
- Medical MRI scan (low contrast)

These examples demonstrate how edge detection behaves under different image conditions.

---

## Installation (Local Setup)

Clone the repository:

```bash
git clone https://github.com/Soumya-duh/image-processing-flask.git
cd image-processing-flask

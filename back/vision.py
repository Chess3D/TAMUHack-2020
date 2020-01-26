from google.cloud import vision
from google.cloud.vision import types
from PIL import Image, ImageDraw

import pymongo
import cv2
import io
import os

# Initialize the camera
cap = cv2.VideoCapture(0)
    
def detect_face(face_file, max_results=4):
    """Uses the Vision API to detect faces in the given file.

    Args:
        face_file: A file-like object containing an image with faces.

    Returns:
        An array of Face objects with information about the picture.
    """
    client = vision.ImageAnnotatorClient()

    content = face_file.read()
    image = types.Image(content=content)
    
    return client.face_detection(image=image, max_results=max_results).face_annotations


def capture_image():
    while True:
        _,cv2_im = cap.read()
        cv2_im = cv2.cvtColor(cv2_im,cv2.COLOR_BGR2RGB)
        pil_im = Image.fromarray(cv2_im)
        pil_im.save("face_file.png")
        with open("face_file.png", 'rb') as picture:
            joy = detect_face(picture)
            if(joy[0] != 0):
                return joy[0].joy_likelihood




        
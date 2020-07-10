import requests
import png
from PIL import Image
import imageio
import io
import json
import cv2
import base64
import matplotlib.pyplot as plt

#v3: changed to sending the images as json base64 string instead of array.
#v4: added the api key


message="RP, I-Serve Payment Gateway RP, I-Serve Payment Gateway  I-Serve Payment Gateway"


payload = {'content': message}
process = requests.post(url = "http://192.168.0.43:5000/api/hash", json = payload) 
response_b64=json.loads(process.text) 
print(response_b64['response'])

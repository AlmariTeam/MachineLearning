import tensorflow as tf
import tensorflow.keras as keras
from keras.models import load_model
import numpy as np
from flask import jsonify
from google.cloud import storage


model = None

def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)

    blob.download_to_filename(destination_file_name)

    print('Blob {} downloaded to {}.'.format(
        source_blob_name,
        destination_file_name))

def load_image(img_path):

    img = tf.keras.preprocessing.image.load_img(img_path, target_size=(300,300))
    img_tensor = tf.keras.preprocessing.image.img_to_array(img)                    # (height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    img_tensor /= 255.                                      # imshow expects values in the range [0, 1]

    return img_tensor

def handler(request):
    global model

    body = request.get_json()
    file_name = body['file_name']

    if model == None :
        download_blob("almari-bucket", "color_model.h5", "/tmp/color-model.h5")
        model = load_model("/tmp/color-model.h5")

    direktori = "/tmp/" + file_name
    download_blob("almari-bucket", file_name, direktori)
    gambar = load_image(direktori)
    
    prediksi = model.predict_step(gambar)

    list_warna = ["Blue","Green","Indigo","Orange","Red","Violet","Yellow"]
    nilai_warna = np.array(prediksi[0])

    nilai_terbesar = max(nilai_warna)
    index_warna_terbesar = np.argmax(nilai_warna)

    clothing_color = list_warna[index_warna_terbesar]

    resp = {
        'color': clothing_color
    }

    return jsonify(resp), 200

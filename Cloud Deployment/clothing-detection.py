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

    img = tf.keras.preprocessing.image.load_img(img_path, target_size=(224,224))
    img_tensor = tf.keras.preprocessing.image.img_to_array(img)                    # (height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    img_tensor /= 255.                                      # imshow expects values in the range [0, 1]

    return img_tensor

def handler(request):
    global model

    body = request.get_json()
    file_name = body['file_name']

    if model == None :
        download_blob("almari-bucket", "fashion_model.h5", "/tmp/fashion-model.h5")
        model = load_model("/tmp/fashion-model.h5")

    direktori = "/tmp/" + file_name
    download_blob("almari-bucket", file_name, direktori)
    gambar = load_image(direktori)
    
    prediksi = model.predict_step(gambar)

    list_baju = ["Anorak","Blazer","Blouse","Bomber","Button-Down","Caftan","Capris","Cardigan","Chinos","Coat","Coverup","Culottes","Cutoffs","Dress","Flannel","Gauchos","Halter","Henley","Hoodie","Jacket","Jeans","Jeggings","Jersey","Jodhpurs","Joggers","Jumpsuit","Kaftan","Kimono","Leggings","Onesie","Parka","Peacoat","Poncho","Robe","Romper","Sarong","Shorts","Skirt","Sweater","Sweatpants","Sweatshorts","Tank","Tee","Top","Trunks","Turtleneck"]
    nilai_baju = np.array(prediksi[0])

    nilai_terbesar = max(nilai_baju)
    index_baju_terbesar = np.argmax(nilai_baju)

    clothing_type = list_baju[index_baju_terbesar]

    resp = {
        'clothing_type': clothing_type
    }

    return jsonify(resp), 200
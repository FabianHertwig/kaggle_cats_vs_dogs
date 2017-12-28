
import os.path
import urllib.request
import zipfile
import tensorflow as tf


def download_file_if_not_existing(url, dest):
    if not os.path.isfile(dest):
        print("Downloading File")
        urllib.request.urlretrieve(url, dest)
        print("Unzipping file")
        zip = zipfile.ZipFile(dest)
        zip.extractall()
    print("Files ready")
    
def tf_config_use_less_memory() : 
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    session = tf.Session(config=config)
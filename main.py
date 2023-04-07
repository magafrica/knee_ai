import tensorflow as tf
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import ModelCheckpoint
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.utils import set_random_seed
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.utils import class_weight
from matplotlib import pyplot as plt
from NeuralNetwork import *
import os


print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

TRAINSET_PATH = "./data/train_set"
VALIDATESET_PATH = "./data/train_set"
TESTSET_PATH = "./data/test_sest"
MODEL_PATH = "./models/model_1"

os.mkdir(MODEL_PATH)
train_set = pd.read_csv(TRAINSET_PATH)
train_set = train_set.to_numpy(dtype = 'float64')
validate_set = pd.read_csv(VALIDATESET_PATH)
validate_set = validate_set.to_numpy(dtype = 'float64')
test_set = pd.read_csv(TESTSET_PATH)
test_set = test_set.to_numpy(dtype = 'float64')

neural_network = NeuralNetworkLR(300, 0.1, train_set, test_set, validate_set, [10,10], MODEL_PATH)
neural_network.create_network()
neural_network.split_datasets()
results = neural_network.train()

file = open(MODEL_PATH + "/results.txt", "w")
file.write(results)
file.close()

plt.plot(results['accuracy'])
plt.plot(results['accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'val'], loc='upper left')
plt.savefig(MODEL_PATH + '/model_accuracy.jpg')
plt.show()

plt.plot(results['loss'])
plt.plot(results['val_loss'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'val'], loc='upper left')
plt.savefig(MODEL_PATH+'/model_loss.jpg')
plt.show()
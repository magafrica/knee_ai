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
import json


print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

TRAINSET_PATH = "./data/training_set.csv"
TESTSET_PATH = "./data/test_set.csv"
MODEL_PATH = "./models/model_1"
TEST = True
TYPE = False

train_set = pd.read_csv(TRAINSET_PATH)
train_set = train_set.to_numpy(dtype = 'float64')
test_set = pd.read_csv(TESTSET_PATH)
test_set = test_set.to_numpy(dtype = 'float64')

neural_network = NeuralNetwork(5, 0.1, train_set, test_set, [10,10], MODEL_PATH, TYPE)
neural_network.create_network()
neural_network.split_datasets()
results, history = neural_network.train()
neural_network.model.save(MODEL_PATH + "/model.h5")
neural_network.model.save_weights(MODEL_PATH + "/weights.h5")

json_object = json.dumps(results, indent= 2)
with open(MODEL_PATH + "/training_results.json", "w") as outfile:
    outfile.write(json_object)

plt.plot(history.history['accuracy'])
plt.plot(history.history['accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'val'], loc='upper left')
plt.savefig(MODEL_PATH + '/model_accuracy_train.jpg')
plt.show()

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'val'], loc='upper left')
plt.savefig(MODEL_PATH+'/model_loss_train.jpg')
plt.show()


if TEST:
    if not TYPE:
        results = neural_network.test()
        results_dic = {'loss': results[0], 'accuracy': results[1]}
        json_object = json.dumps(results_dic, indent= 4)
        with open(MODEL_PATH + "/test_results.json", "w") as outfile:
            outfile.write(json_object)
    else:
        results, cm = neural_network.test()
        results_dic = {'loss': results[0], 'accuracy': results[1]}
        json_object = json.dumps(results_dic, indent= 4)
        with open(MODEL_PATH + "/test_results.json", "w") as outfile:
            outfile.write(json_object)
        
        file = open(MODEL_PATH + "/cm_test.txt", "w")
        file.write(results)
        file.close()
        
        
        

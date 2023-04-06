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

print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

class NeuralNetworkLR:
    """Red neuronal con salida real, regresión"""
    
    def __init__(self, epochs, lr, train_data, test_data, validate_data, neurons, model_path):
        """
        epochs = int, número de "rondas" de entrenamiento
        lr = float, tasa de aprendizaje
        train_data = dataset, datos de entrenamiento
        validate_data = dataset, datos de validación
        test_data = dataset, datos de test
        neurons = lista python, neuronas de las capas ocultas
        model_path = path para guardar el modelo
        
        """
        self.epochs = epochs
        self.lr = lr
        self.train_data = train_data
        self.validate_data = validate_data
        self.test_data = test_data
        self.neurons = neurons
        self.model = None
        self.X_train = None
        self.Y_train = None
        self.X_validate = None
        self.Y_validate = None
        self.X_test = None
        self.Y_test = None
        self.model_path = model_path
            
    def create_network(self):
        self.model = Sequential()
        #capa de entrada
        self.model.add(Dense(self.train_data.shape[1], activation = 'relu'))
        #capas ocultas
        for layer in range (len(self.neurons)-1):
            self.model.add(Dense(self.neurons[layer], activation = 'relu'))
        #capa de salida
        self.model.add(Dense(self.neurons[-1]), activation = 'softmax')
        
    """def checkpoint(self):
       checkpoint = ModelCheckpoint(self.model_path + '/model', monitor='val_loss', verbose=1, save_best_only=True)
       return checkpoint"""
      
    def split_datasets(self):
        self.X_train = None
        self.Y_train = None
        self.X_validate = None
        self.Y_validate = None
        self.X_test = None
        self.Y_test = None
    
    def train(self):
        self.model.compile(optimizer = tf.keras.optimizers.SDG(learning_rate = self.lr, momentum = 0), loss= 'mean_squared_error', metrics=['accuracy', 'mse'])
        historico = self.model.fit(self.X_train, self.Y_train, epochs = self.epochs, batch_size = 16, validation_data= (self.X_validate, self.Y_validate), shuffle = False, validation_freq = 1) #'''callbacks = [self.checkpoint()],''' 
        epochs_stop = np.where(historico.history['val_loss'] == np.min(historico.history['val_loss']))
        final_epoch=epochs_stop[0][0]
        metrics = {'accuracy': historico.history['accuracy'][final_epoch -1],
                   'loss': historico.history['loss'][final_epoch -1],
                   'val_accuracy': historico.history['val_accuracy'][final_epoch -1],
                   'val_loss': historico.history['val_loss'][final_epoch -1]}
        return metrics
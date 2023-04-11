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

class NeuralNetwork:
    """Red neuronal con salida real, regresión"""
    
    def __init__(self, epochs, lr, train_data, test_data, neurons, model_path, type, last_layer = 1):
        """
        epochs = int, número de "rondas" de entrenamiento
        lr = float, tasa de aprendizaje
        train_data = dataset, datos de entrenamiento
        validate_data = dataset, datos de validación
        test_data = dataset, datos de test
        neurons = lista python, neuronas de las capas ocultas
        model_path = path para guardar el modelo
        type = bol, True = classes, False = logistic regression
        
        """
        self.epochs = epochs
        self.lr = lr
        self.train_data = train_data
        self.test_data = test_data
        self.neurons = neurons
        self.model = None
        self.model_path = model_path
        self.type = type
        self.last_layer = last_layer
        self.X_train, self.Y_train, self.X_test, self.Y_test= self.split_datasets()
    
    def one_hot_encoding(self, y_values, encoder):
        y_onehot = encoder.fit_transform(y_values) 
        return y_onehot    
    
    def create_network(self):
        self.model = Sequential()
        print("created model")
        #capa de entrada
        self.model.add(Dense(units = self.train_data.shape[1] - 1, activation = 'relu', input_shape=(self.train_data.shape[1] - 1,)))
        #capas ocultas
        for layer in range (len(self.neurons)):
            self.model.add(Dense(self.neurons[layer], activation = 'relu'))
            
        if not self.type:
            #capa de salida
            self.model.add(Dense(self.last_layer, activation = 'relu'))
        else:
            self.model.add((Dense(self.last_layer, activation='softmax')))
            
        
        
    def checkpoint(self):
       checkpoint = ModelCheckpoint(self.model_path + '/model', monitor='val_loss', verbose=1, save_best_only=True)
       return checkpoint
      
    def split_datasets(self):
        self.X_train, self.X_test = self.train_data[:, :-1], self.test_data[:, :-1]
        self.Y_train, self.Y_test = self.train_data[:,-1], self.test_data[:,-1]
        if self.type:
            encoder= LabelBinarizer()
            self.Y_train = self.one_hot_encoding(self.Y_train, encoder)
            self.Y_test = self.one_hot_encoding(self.Y_test, encoder)
        return self.X_train, self.Y_train, self.X_test, self.Y_test
    
    def train(self):
        if self.type:
            self.model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), loss='sparse_categorical_crossentropy', metrics=['sparse_categorical_accuracy', 'sparse_categorical_crossentropy'])
            historico= self.model.fit(self.X_train, self.Y_train, epochs=30, validation_freq=1,validation_split=0.2, callbacks = [self.checkpoint()])
            ephocs_stop=np.where(historico.history['val_loss'] == np.min(historico.history['val_loss']))
            final_epoch=ephocs_stop[0][0]
            metrics = {'sparse_categorical_accuracy': historico.history['sparse_categorical_accuracy'][final_epoch - 1],
                        'loss': historico.history['loss'][final_epoch - 1],
                        'val_sparse_categorical_accuracy': historico.history['val_sparse_categorical_accuracy'][final_epoch - 1],
                        'val_loss': historico.history['val_loss'][final_epoch - 1]}
        else:
            self.model.compile(optimizer = tf.keras.optimizers.SGD(learning_rate = self.lr, momentum = 0), loss= 'mean_squared_error', metrics=['accuracy', 'mse'])
            historico = self.model.fit(self.X_train, self.Y_train, epochs = self.epochs, batch_size = 16, shuffle = False, validation_freq = 1, validation_split = 0.2, callbacks = [self.checkpoint()])
            epochs_stop = np.where(historico.history['val_loss'] == np.min(historico.history['val_loss']))
            final_epoch=epochs_stop[0][0]
            metrics = {'accuracy': historico.history['accuracy'][final_epoch -1],
                    'loss': historico.history['loss'][final_epoch -1],
                    'val_accuracy': historico.history['val_accuracy'][final_epoch -1],
                    'val_loss': historico.history['val_loss'][final_epoch -1]}
        return metrics, historico
    
    def test(self):
        if self.type:
            evaluacion=self.model.evaluate(self.Y_train, self.Y_test)

            #predicciones en bruto:
            raw_testPred_pm = self.model.predict(self.Y_train)
            #predicciones de la clase:
            class_testPred_pm = np.argmax(raw_testPred_pm, axis=1)

            cm=confusion_matrix(self.Y_test, class_testPred_pm) 
            print('Classification Report')
            target_names = ['Pobre', 'Aceptable', 'Bueno', 'Excelente']
            print(classification_report(self.Y_test, class_testPred_pm, target_names=target_names))
            return evaluacion, cm
        else:
            evaluation = self.model.evaluate(self.X_test, self.Y_test)
            return evaluation

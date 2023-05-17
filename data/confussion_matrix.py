import pandas as pd
from sklearn.metrics import confusion_matrix, plot_confusion_matrix
import matplotlib.pyplot as plt
from sklearn import metrics

# Load data from CSV
DATASET_PATH = "./data/datasets/"
FILENAME_TO_READ = DATASET_PATH + 'random-forest-valores.csv'
SAVEFIG = True
data = pd.read_csv(FILENAME_TO_READ, sep=';')

# Extract true labels and predicted labels from the data
y_true = data['real-0,9'].tolist()
y_pred = data['predict-0,9'].tolist()
for i in range(len(y_true)):
    if y_true[i] < 65:
        y_true[i] = 0
    elif y_true[i]>= 65 and y_true[i] < 83:
        y_true[i] = 1
    elif y_true[i]>= 83 and y_true[i] < 95:
        y_true[i] = 2
    else:
        y_true[i] = 3
        
    if y_pred[i] < 65:
        y_pred[i] = 0
    elif y_pred[i]>= 65 and y_pred[i] < 83:
        y_pred[i] = 1
    elif y_pred[i]>= 83 and y_pred[i] < 95:
        y_pred[i] = 2
    else:
        y_pred[i] = 3
        

class_names = ['Pobre', 'Aceptable', 'Bueno', 'Excelente']

# Calculate confusion matrix

confusion_matrix = metrics.confusion_matrix(y_true, y_pred)

cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = ['Pobre', 'Aceptable', 'Bueno', 'Excelente'])

cm_display.plot()
plt.title("Matriz de confusión random forest, sensibilidad 0,9")
if SAVEFIG:
    plt.savefig('./data/graficas/mc_RF_0.9.png')
plt.show() 

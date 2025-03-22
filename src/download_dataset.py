# src/download_dataset.py
from sklearn.datasets import fetch_openml
import numpy as np
import os

def download_mnist():
    # Crear directorio data si no existe
    os.makedirs('data', exist_ok=True)

    print('Descargando dataset MNIST...')
    mnist = fetch_openml('mnist_784', version=1)
    X, y = mnist.data.astype('float32'), mnist.target.astype('int32')

    print('Guardando dataset...')
    np.savez_compressed('data/mnist_raw.npz', X=X, y=y)
    print('Dataset guardado exitosamente')

if __name__ == "__main__":
    download_mnist()
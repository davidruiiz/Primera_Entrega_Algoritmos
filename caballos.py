import numpy as np

#Definimos la matriz de adyacencia del grafo G
AG = [[0, 0, 0, 0, 0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 1, 0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 1, 0, 0, 1], [0, 1, 0, 0, 0, 1, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 0, 0, 0]]

AG = np.array(AG)

def caballos():
    
    #Definimos el número de movimientos que realizará el caballo
    k = int(input("Ingrese el número de movimientos que realizará el caballo: "))

    #Definimos la matriz de adyacencia elevada a k
    AGk = np.linalg.matrix_power(AG, k)

    #El número de posibilidades válidas será la suma de los elementos de la matriz de adyacencia elevada a k

    posibilidades = np.sum(AGk)

    print("El número de posibilidades válidas con", k, "movimientos es: ")
    
    return posibilidades

if __name__ == '__main__':
    # Probamos la función
    print(caballos())

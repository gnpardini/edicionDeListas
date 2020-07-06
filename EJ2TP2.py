"""Escribir funciones para:
a. Generar una lista de 50 números aleatorios del 1 al 100.
b. Recibir una lista como parámetro y devolver True si la misma contiene algún
elemento repetido. La función no debe modificar la lista.
c. Recibir una lista como parámetro y devolver una nueva lista con los elementos
únicos de la lista original, sin importar el orden.
Combinar estas tres funciones en un mismo programa."""

import random

def generarLista():
    
    lista = []
    
    for i in range (4):
        numero = random.randint(1,5)
        lista.append(numero)
        
    return lista

def chequearSiHayElementosRepetidos(lista):
    
    contador = 0
    repetido = False

    
    for i in range(len(lista)):
        for j in range (len(lista)):
            if j != i:
                if lista[i] == lista[j]:
                    repetido = True
                
                    
    return repetido
                    
    
 
def generarListaConElementosUnicos(lista):
    
    listaNueva = []
    
    for i in range(len(lista)):
        repetido = False 
        
        for j in range (len(lista)):
            
            if j != i:
                if lista[i] == lista[j]:
                    repetido = True
                    
        if repetido == False:
            listaNueva.append(lista[i])
    
            
    return listaNueva


#main

listaDeNumeros = generarLista()
print(listaDeNumeros)
repetidos = chequearSiHayElementosRepetidos(listaDeNumeros)
print(repetidos)
listaConElementosSinRepetir = generarListaConElementosUnicos(listaDeNumeros)
print(listaConElementosSinRepetir)
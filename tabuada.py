#!/usr/bin/.venv python3

"""Imprime a tabuada do 1 ao 10

Tabuada do 1
1
2
3
4
---------
Tabuada do 2
2
4
6
8
10
---------

    

"""
__version__ = "0.1.0"
__author__ = "Vitor"

list_number = list(range(1,3))

#interables = (PERCORRÍVEIS)

# PARA CADA NÚMERO EM NÚMEROS
for number in list_number:
    print("Tabuada do:", number)
    for others_number in list_number:
        resultado = others_number * number
        print(f"{number} * {others_number} = {resultado}")
    print("------------------")

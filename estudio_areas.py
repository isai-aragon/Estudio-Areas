#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 11:52:17 2018

Software: Estudio_Areas V1.0

@author: ARAGON SOFTWARE COMPANY
"""
"""
Programa que realiza un estudio de áreas, que sirve para deter-
minar el area total que debe contener un espacio en el analisis 
arqitectonico profesional.
"""

# Declaracion de lo mensajes iniciales

print('####################################################\n')
msj1 = '''Programa que calcula el área total para un espacio,
utilizando la tecnica de estudio de areas\n'''
print(msj1)
print('####################################################\n')

# Declaración de la lista que almacena las áreas de muebles

sumMuebles = []
              
# Declaracion de la funcion que realiza la |Orden 1|. Ingresar área 
# de mueble.

def orden1():
    try:  
        lm = input('Escribe el largo del mueble: ')
        lm = float(lm)
            
        am = input('Escribe el ancho del mueble: ')
        am = float(am)
      
        AreaMueble = lm * am
        sumMuebles.append(AreaMueble)
        print('\n¡Muy bien! Datos ingresados correctamente.')
        input('Presiona <Enter> para continuar. ')
        EstudioAreas()
        
    except ValueError:
        print('\n¡A ocurrido un error con lo datos ingresados!')
        print('Por favor revisa que ingresaste un número.')
        print('\nPresiona <Enter> para continuar. ')
        input()
        orden1()
    #finally:
        #EstudioAreas()

# Declaracion de la funcion que realiza la |Orden 2|. Ver áreas 
# ingresadas.

def orden2():
    print('\nLas áreas de mueble ingresadas son las siguiente: \n')
    print(sumMuebles)
    input('\nPresiona <Enter> para continuar. ')
    EstudioAreas()

# Declaracion de la funcion que realiza la |Orden 3|. Calcular área 
# total.
            
def orden3():
    try:
    
        ecirculacion = float(input('''Cuantas personas ingresaran en el área: '''))
        C = 0.6 * ecirculacion
      
        x100cft = float(input('''Ingresa un porcentaje de confort
que consideres adecuado para el área: '''))
    
        AO = sum(sumMuebles)
        confort = (AO * C) * (x100cft/100)
                
        area_total = (AO * C) + confort
        
        input('Presiona <Enter> para calcular')
        print('El área total calculada es: \n')
        area_total = str(area_total)
        print(area_total+' m2\n')
        input('Presiona <Enter> para continuar. ')
        EstudioAreas()            
        
    except ValueError:
        print('\n¡A ocurrido un error con alguno de lo datos ingresados!')
        print('Por favor revisa que ingresaste un número.')
        print('\nPresiona <Enter> para continuar. ')
        input()
        orden3()
    #finally:
        #EstudioAreas()

# Declaracion de la funcion que realiza la |Orden 4|. Salir del pro- 
# grama.
        
def salir():      
        print('Hasta pronto')
        input('Presiona <Enter> para salir')    
        exit
        
# Creación de la funcion principal que realiza la computación prin- # cipal del programa.

def EstudioAreas():
    print('''\nQue quieres hacer ahora:\n 
        1 - Ingresar área de mueble.
        2 - Ver áreas ingresadas.
        3 - Calcular área total.
        4 - Salir.''')
    
    orden = input('\nIngresa la accion a realizar: ')
                               
    if orden == '1':
        orden1()
     
    elif orden == '2':
        orden2()
                  
    elif orden == '3':
        orden3()
            
    elif orden == '4':
        salir()
    
    else:
        EstudioAreas()               
    
EstudioAreas()   
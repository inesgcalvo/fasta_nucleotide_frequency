# -*- coding: utf-8 -*-
"""
@author: Inés G. Calvo
"""

# Esta función abrirá el documento FASTA con la secuencia del gen y leerá todos los nucleótidos

def leer_archivo(fasta_file):
    with open(fasta_file, 'r') as file:
        contenido = file.read().split('\n')
    
    secuencias = []
    secuencia_actual = ''
    
    for linea in contenido:
        if linea.startswith('>'):
            if secuencia_actual:
                secuencias.append(secuencia_actual)
                secuencia_actual = ''
        else:
            secuencia_actual += linea
    
    if secuencia_actual:
        secuencias.append(secuencia_actual)
    
    return secuencias

# Esta función servirá para contar la cantidad de cada nucleótido

def contar_nucleotidos(secuencia):
    conteo = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    
    for nucleotido in secuencia:
        if nucleotido in conteo:
            conteo[nucleotido] += 1
    
    return conteo

# Esta es la función que presentará los resultados usando las dos funciones previas y la ruta de la carpeta de la secuencia señalada posteriormente

def analizar_archivo(fasta_file):
    secuencias = leer_archivo(fasta_file)
    
    for i, secuencia in enumerate(secuencias):
        conteo = contar_nucleotidos(secuencia)
        # print(f'Secuencia {i+1}: {secuencia}')
        print(f'Frecuencia de nucleótidos:')
        for nucleotido, count in conteo.items():
            print(f'{nucleotido}: {count}')
        print()

# Ruta del archivo FASTA
archivo_fasta = "./_fasta/susd4.txt"

# Llamada a la función para analizar el archivo
analizar_archivo(archivo_fasta)

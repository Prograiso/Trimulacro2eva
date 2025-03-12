#contar vocales de diccionario, definimos funcion

def contar_vocales(palabra):

#creamos una lista con las bocales
    vocales = "aeiou"

#creamos diccionario, inicializamos a 0
    resultado = {
    "a" : 0,
    "e" : 0,
    "i" : 0,
    "o" : 0,
    "u" : 0,
}

    for letra in palabra:
        if letra in vocales:
            resultado[letra]+=1

    return resultado


pri#para imprimir ya fuera del bucle y en vez de input le metemos el parámetro en el printnt(contar_vocales("bucaramango"))        

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



#no usamos input, metemos el parametro (palabra) a mano para ver el resultado
print(contar_vocales("bucaramango"))  

 #fin      

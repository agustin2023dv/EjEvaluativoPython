primera_cadena = "Hola soy Agu"
segunda_cadena = "Hola soy Egs"


def detectar_diferencias(cadena1,cadena2):
    '''
    Lo primero que hace la funcion es evaluar si el input recibido matchea en extension 
    utilizando la funcion built in "len()" para ello
    '''
    if len(cadena1) != len(cadena2):

        '''Al contar las mismas con diferentes longitudes, se retorna un mensaje avisando lo mismo'''

        return "Las cadenas deben coincidir en cantidad de caracteres"
    
    '''Declaracion de la lista la cual contendrá los caracteres en los cuales las variables varien'''
    diferencias = []

    '''Utilizo bucle for para iterar sobre cadena1'''
    for i in range(len(cadena1)):

        '''Condicional if para evaluar si el caracter en x lugar de la cadena1 es diferente en la misma ubicacion en la cadena2
        De serlo (diferente) el mismo se agrega a la lista diferencias[] mediante de la funcion append() la cual agrega dicho elemento
        a la ultima posicion de la lista.
        Esto me devolvera los caracteres que ESTEN en la cadena1 y NO ESTEN en la cadena2
        '''
        if cadena1[i] != cadena2[i]:
            diferencias.append(cadena1[i])
    
    return diferencias

print(detectar_diferencias(primera_cadena,segunda_cadena))

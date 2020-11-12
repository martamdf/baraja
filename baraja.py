import random

def creaBaraja(palos, numeros):
    baraja = []
    for palo in palos:
        for numero in numeros:
            baraja.append(numero+palo)

    return baraja
        

'''
def intercambio(primer_valor, segundo_valor):

'''

def barajar(lista_de_naipes):
    for i in range(len(lista_de_naipes)):
        nueva_pos = random.randrange(len(lista_de_naipes))

        '''
        Intercambio de cartas, técnica vaso vacío
        '''

        aux = lista_de_naipes[nueva_pos]
        lista_de_naipes[nueva_pos] = lista_de_naipes[i]
        lista_de_naipes[i]=aux
    return lista_de_naipes

'''
mazacote = creaBaraja()
barajar(mazacote)
print(mazacote)


también se podría hacer con:
print(barajar(creaBaraja()))
'''
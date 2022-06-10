'''En el presente codigo permite obtener el recorrido y el orden de los nodos del grafo,
mediante los vertices asignados en cada nodo, recordando que solo puede ser visitado una vez cada nodo
 indicando si el nodo es dirigido o no, cuando son dirigidos debe seguir su direcciín indicada'''

from queue import Queue
#Crea una función llamada gráfico.
class Grafico:
    #Crea objetos instanciando los atributos.
    def __init__(self, numero_de_nodos, dirigido=True):
        #Ingresa por medio de atributos el número de nodos.
        self.m_numero_de_nodos = numero_de_nodos
        #Ingresa el número de nodos mediante el rango usando el atributo número de nodos.
        self.m_nodos = range(self.m_numero_de_nodos)
        # Instancia el atributo dirigido.
        self.m_dirigido = dirigido
       
        #Se implementa una lista adyacente mediante un diccionario.
        '''Para agregar un diccionario tenemos como parámetro crear un objeto por lista agregando
        un bucle de recorrido que empieza de nodo=0 hasta el rango asignado'''
        self.m_adj_lista = {nodo: set() for nodo in self.m_nodos}     
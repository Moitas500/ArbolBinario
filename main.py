class Nodo():
    def __init__(self,valor,izquierda = None, derecha = None):
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha

def en_orden(arbol):
    if arbol == None:
        return []
    return en_orden(arbol.izquierda) + [arbol.valor] + en_orden(arbol.derecha)

def pre_orden(arbol):
    if arbol == None:
        return []
    return [arbol.valor] + pre_orden(arbol.izquierda) + pre_orden(arbol.derecha)

def post_orden(arbol):
    if arbol == None:
        return []
    return post_orden(arbol.izquierda) + post_orden(arbol.derecha) + [arbol.valor]

def insertar(arbol,valor):
    if valor == None:
      return arbol
    if arbol == None:
        return Nodo(valor)
    if arbol.valor > valor:
        return Nodo(arbol.valor,insertar(arbol.izquierda, valor),arbol.derecha)
    return Nodo(arbol.valor,arbol.izquierda,insertar(arbol.derecha,valor))

def insertarListaNumeros(arbol, lista):
    if lista == []:
      return insertar(arbol, None)
    else:
      return insertarListaNumeros(insertar(arbol, lista[0]),lista[1:])

def buscar(arbol, valor):
    if arbol == None:
        return False
    if arbol.valor == valor:
        return True
    if valor > arbol.valor:
        return buscar(arbol.derecha,valor)
    return buscar(arbol.izquierda,valor)
    
arbol = Nodo(25,Nodo(15,None,Nodo(20)),Nodo(50))

print(en_orden(insertar(arbol,60)))
print(post_orden(insertarListaNumeros(arbol,[80,90,100])))
print(buscar(arbol,80))

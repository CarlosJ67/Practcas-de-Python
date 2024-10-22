llave=False
girarI=False 
girarD=True

def avanzar(llave):
    if(encender()):
        print("Run, run, ruuuun")
    else:
        print("Inserta llave")

def frenar():
    print("Frenando")
def retroceder():
    print("reserva")

def encender():
    print("colocar llave")
    llave=True
    if(llave):
        print("Carro encendido")
    return llave

def apagar():
    print("Quitar llave")
    llave=False
    if(llave==False):
        print("Carro Apagado")

def girarIzq():
    girarI= True
    print("Girando a la izquierda")
    return girarI
def girarDer():
    girarD= True
    print("girando a la derecha")
    return girarD


avanzar()
retroceder()

if(girarDer):
    print("No puedes girar a la izquierda")
    girarI = False
if(girarIzq):
    print("No puedes gitar a la derecha")
    girarD= False


# Ciclo For





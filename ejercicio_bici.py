class Bici:
    def __init__(self, tipo_sillon, num_rin, diam_rueda, tipo_color):
        self.tipo_sillon = tipo_sillon
        self.num_rin = num_rin
        self.diam_rueda = diam_rueda
        self.tipo_color = tipo_color

    def frenar(self):
        print("La bicicleta esta Frenando")
        
    def girar(self, direccion):
        print(f"La bicicleta gira hacia la {direccion}")
        
    def pedalear(self):
        print("Pedaleando")
        
    def avanzar(self):
        print("La Bicicleta esta Avanzando")


mi_bici = Bici("Cuero", 3, 11, "Azul")

print(f'Mi bicicleta: Tipo de Sillon: {mi_bici.tipo_sillon}, numero de Rin: {mi_bici.num_rin}, Diametro de rueda: {mi_bici.diam_rueda}, Color: {mi_bici.tipo_color}')

mi_bici.pedalear()
mi_bici.avanzar() 
mi_bici.frenar()     
mi_bici.girar("izquierda")      

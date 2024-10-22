class Perro:
    def _init_(self, nombre, raza):
        print(f"Creando perro {nombre}, {raza}")

    def ladra(self):
        print("Guau")
    
    def camina(self,pasos):
        print(f"Caminando {pasos} pasos")
        

mi_perro =  Perro("Toby", "Pastor Aleman")
su_perro = Perro("Firulais", "Electrico")

print(type(mi_perro))
print(mi_perro.espacio)
print(su_perro.espacio)
print(Perro.espacio)

mi_perro.ladra()
su_perro.ladra()

mi_perro.camina(5)
su_perro.camina(10)




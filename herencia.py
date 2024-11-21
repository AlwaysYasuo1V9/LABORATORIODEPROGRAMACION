# Clase base Mago
class Mago:
    def hechizos(self):
        return "El Mago lanza un hechizo."

# Clase base Guerrero
class Guerrero:
    def defensa(self):
        return "El Guerrero bloquea el ataque."

# Clase base Elfo
class Elfo:
    def aura(self):
        return "El Elfo invoca un aura protectora."

# Clase derivada DarkLord (hereda de Guerrero y Elfo en ese orden)
class DarkLord(Guerrero, Elfo):
    pass

# Crear una instancia de DarkLord y probar métodos
darklord = DarkLord()
print(darklord.defensa())  # Método de Guerrero
print(darklord.aura())     # Método de Elfo

# Mostrar el MRO (Method Resolution Order)
print("\nMRO con orden [Guerrero, Elfo]:")
print(DarkLord.__mro__)

# Cambiar el orden de herencia
class DarkLordV2(Elfo, Guerrero):
    pass

# Crear una instancia de DarkLordV2 y probar métodos
darklord_v2 = DarkLordV2()
print("\nMRO con orden [Elfo, Guerrero]:")
print(DarkLordV2.__mro__)

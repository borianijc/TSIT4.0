# Integrante: Boriani Juan Cruz

# Clase 1---------

class Vehiculos:
    def __init__(self,tipo_de_vehiculo,sub_tipo,tipo_combustible,marca,modelo):
        velocidad = 0
        self.tipo_de_vehiculo = tipo_de_vehiculo
        self.sub_tipo = sub_tipo
        self.tipo_combustible = tipo_combustible
        self.marca = marca
        self.modelo = modelo
    
    def caracteristicas(self):
        print(self.sub_tipo,"es un vehículo de tipo",self.tipo_de_vehiculo,
        "marca",self.marca,"modelo",self.modelo)
    
    def velocidad_max(self,velocidad_maxima):
        velocidad = velocidad_maxima
        print(self.marca,self.modelo,"tiene una velocidad maxima de",velocidad,"Km/h")

class Vehiculos_terrestres(Vehiculos):
    def __init__(self, tipo_de_vehiculo, sub_tipo, tipo_combustible, marca, modelo,tipo_traccion,tipo_uso):
        Vehiculos.__init__(self,tipo_de_vehiculo, sub_tipo, tipo_combustible, marca, modelo)
        self.tipo_traccion = tipo_traccion
        self.tipo_uso = tipo_uso

    def tipo_de_vehiculo_terrestre(self):
        print(self.sub_tipo,"tracciona con",self.tipo_traccion,"y se utiliza para",self.tipo_uso)

print("\n","Clase 1 - Vehiculos","\n")

automovil = Vehiculos_terrestres("Terrestre", "Automóvil", "Nafta","VW","Gol","Ruedas","Ir al trabajo")
automovil.caracteristicas()
automovil.velocidad_max(110)
automovil.tipo_de_vehiculo_terrestre()

print()

camion = Vehiculos_terrestres("Terrestre", "Camión", "Gas-oil","Scania","G-360","Ruedas","Transporte de Cargas")
camion.caracteristicas()
camion.velocidad_max(80)
camion.tipo_de_vehiculo_terrestre()

print()

retroexcavadora = Vehiculos_terrestres("Terrestre", "Retroexcavadora", "Gas-oil","Cat","320D2","Orugas metalicas",
"Obras civiles")
retroexcavadora.caracteristicas()
retroexcavadora.velocidad_max(15)
retroexcavadora.tipo_de_vehiculo_terrestre

#------------------------------------------------------------------------------------------------------  
# Clase 2---------

class Animales:
    def __init__(self,especie,tipo,edad):
        tipo_alimentacion=""
        self.especie = especie
        self.tipo = tipo
        self.edad = edad

    def caracteristicas(self):
        print(self.especie,"es un animal de tipo",self.tipo,"y tiene",self.edad)
    
    def tipo_alimento(self,alimento):
        
        if alimento == "carne":
            tipo_alimentacion= "carnivoro" 
        elif alimento == "vegetales":
            tipo_alimentacion= "hervivoro"
        elif alimento == "carne y vegetales":
            tipo_alimentacion= "omnivoro"
        else:
            tipo_alimentacion= "desconocida"
        print("segun su alimentacion",self.especie,"es", tipo_alimentacion)

class Animales_mamiferos(Animales):
    def __init__ (self, especie, tipo, edad, raza):
        Animales.__init__(self, especie, tipo, edad)
        self.raza = raza
        
    def habitat_animal (self,habitat):
        if habitat == "domestico":
            nombre = input("Cual es su nombre")
            print(self.especie,"es",habitat,"y se llama",nombre)
        else:
            print(self.especie,"es",habitat)

print("\n""Clase 2 - Animales","\n")

perro = Animales_mamiferos("Perro","Mamifero","10 años","Ovejero aleman")
perro.caracteristicas()
perro.tipo_alimento("carne")
perro.habitat_animal("domestico")

print()

vaca = Animales_mamiferos("Vaca","Mamifero","5 años","Holando argentino")
vaca.caracteristicas()
vaca.tipo_alimento("vegetales")
vaca.habitat_animal("domestico")

print()

leon = Animales_mamiferos("Leon","Mamifero","3 años","")
leon.caracteristicas()
leon.tipo_alimento("carne")
leon.habitat_animal("salvaje")

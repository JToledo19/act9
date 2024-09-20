print("actividad 9 clase humano")
print("Jorge Toledo mat 22308051281106")

#zona de clases

class humano1106:
    #zona de atributo dentro de la clase 
    edad=0
    genero=0
    ojos=0
    estatura=0
    peso=0


    #zona de funcionamiento dentro de la clase 
    def correr1106(self,n):
        print(f"{n} esta corriendo machin ")
    def brincar1106(self,n):
        print(f"{n} esta brincando asta los cielos")
    def cantar1106(self,n):
        print(f"{n} esta cantando CT ")
    def comer1106(self,n):
        print(f"{n} esta comiendo ya sabees ")
#zona de creacion de objetos 
Toledo=humano1106()
Vale=humano1106()

#zona de usando objetos     
print(" resultado para Vale")
Vale.correr1106("Vale")
Vale.brincar1106("Vale")
Vale.cantar1106("Vale")
Vale.comer1106("Vale")

print("atributos de vale:")
Vale.edad=17
Vale.genero="niña"
Vale.ojos="cafes"
Vale.estatura=158
Vale.peso=49
print(f"edad:{Vale.edad}")
print(f"genero:{Vale.genero}")
print(f"ojos:{Vale.ojos}")
print(f"estatura:{Vale.estatura}")
print(f"peso:{Vale.peso}")

print(f"")

print(" resultado para Toledo")
Toledo.edad=18
print(f"edad{Toledo.edad}")
Toledo.correr1106("Toledo")

print("atributos de toledo")
Toledo.edad=18
print(f"edad: {Toledo.edad}")
Vale.brincar1106("Toledo")

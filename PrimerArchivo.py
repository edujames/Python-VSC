import pickle

class Persona:
    def __init__(self, nombre, genero,  edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad

        print("Se ha creado una persona con el nombre de: " + self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)
    

class ListaPersonas:
    personas = []

    def __init__(self):
        listaDePersonas = open("ficheroExterno", "ab+")
        listaDePersonas.seek(0)

        try:
            self.personas =pickle.load(listaDePersonas)

            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))

        except:
            print("El fichero externo esta vacio")

        finally:
            listaDePersonas.close()
            del(listaDePersonas)

    def agregarPersonas(self, Persona):
        self.personas.append(Persona)
        self.guardarPersonasEnFicheroExterno()

    def comprobarPersona(self):
        for p in self.personas:
            print(p)

    def guardarPersonasEnFicheroExterno(self):
        listaDePersonas = open("ficheroExterno", "wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)


    def mostrarInfoFicheroExterno(self):
        listaDePersonas = open("ficheroExterno", "rb")
        personas = pickle.load(listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)

        for p in personas:
            print(p)


miLista=ListaPersonas()
persona=Persona("Juan", "Masculino", 28)
persona2=Persona("Maria", "Femenino", 25)
persona3=Persona("Pedro", "Masculino", 30)
persona4=Persona("Ana", "Femenino", 22)
miLista.agregarPersonas(persona)
miLista.agregarPersonas(persona2)
miLista.agregarPersonas(persona3)
miLista.agregarPersonas(persona4)

miLista.comprobarPersona()



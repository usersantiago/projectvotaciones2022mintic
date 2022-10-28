from Repositorios.RepositorioMesa import RepositorioMesa
from Modelos.Mesa import Mesa
class ControladorMesa():
    def __init__(self):
        self.repositorioMesa = RepositorioMesa()
    def index(self):
        return self.repositorioMesa.findAll()
    def create(self, infoMesa):
        nuevaMesa=Mesa(infoMesa)
        return self.repositorioMesa.save(nuevaMesa)
    def show(self,id):
        laMesa=Mesa(self.repositorioMesa.findById(id))
        return laMesa.__dict__
    def update(self, id, infoMesa):
        mesaActual = Mesa(self.repositorioMesa.findById(id))
        mesaActual.numero = infoMesa["numero"]
        mesaActual.cantidad_inscritos = infoMesa["cantidad_inscritos"]
        return self.repositorioMesa.save(mesaActual)
    def delete(self, id):
        return self.repositorioMesa.delete(id)

"""from Modelos.Estudiante import Estudiante
class ControladorEstudiante():
    def __init__(self):
        print("Creando ControladorEstudiante")
    def index(self):
        print("Listar todos los estudiantes")
        unEstudiante={
            "_id":"abc123",
            "cedula":"123",
            "nombre":"Juan",
            "apellido":"Perez"
        }
        return [unEstudiante]
    def create(self,infoEstudiante):
        print("Crear un estudiante")
        elEstudiante = Estudiante(infoEstudiante)
        return elEstudiante.__dict__
    def show(self,id):
        print("Mostrando un estudiante con id ",id)
        elEstudiante = {
            "_id": id,
            "cedula": "123",
            "nombre": "Juan",
            "apellido": "Perez"
        }
        return elEstudiante
    def update(self,id,infoEstudiante):
        print("Actualizando estudiante con id ",id)
        elEstudiante = Estudiante(infoEstudiante)
        return elEstudiante.__dict__
    def delete(self,id):
        print("Elimiando estudiante con id ",id)
        return {"deleted_count":1}"""
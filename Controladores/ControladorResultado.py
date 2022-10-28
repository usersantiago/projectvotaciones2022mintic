from Modelos.Resultado import Resultado
from Modelos.Mesa import Mesa
from Modelos.Candidato import Candidato
from Repositorios.RepositorioResultado import RepositorioResultado
from Repositorios.RepositorioMesa import RepositorioMesa
from Repositorios.RepositorioCandidato import RepositorioCandidato

class ControladorResultado():
    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
        self.repositorioMesa = RepositorioMesa()
        self.repositorioCandidato = RepositorioCandidato()
    def index(self):
        return self.repositorioResultado.findAll()
    # Asignacion mesa - candidato a resultado
    def create(self, infoResultado,id_mesa,id_candidato):
        nuevoResultado = Resultado(infoResultado)
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa)) #laMesa = el estudiante
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))#elcandidato = laMateria
        nuevoResultado.mesa=laMesa
        nuevoResultado.candidato=elCandidato
        return self.repositorioResultado.save(nuevoResultado)
    #mostrando inscripcion
    def show(self, id):
        elPartido = Resultado(self.repositorioResultado.findById(id))
        return elPartido.__dict__
    #Updating inscripcion ( mesa - candidato)
    def update(self,id,infoResultado,id_mesa,id_candidato):
        resultadoActual = Resultado(self.repositorioResultado.findById(id))
        resultadoActual.id = infoResultado["id"]
        resultadoActual.total_votos = infoResultado["total_votos"]
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        resultadoActual.mesa = laMesa
        resultadoActual.candidato = elCandidato
        return self.repositorioResultado.save(resultadoActual)
    def delete(self, id):
        return self.repositorioResultado.delete(id)
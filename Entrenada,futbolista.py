class personaFut:
     cantidadPersonas=0
     equipo="ND"
     def __init__(self,cedula,nombre):
          self.cedula=cedula
          self.nombre=nombre
          personaFut.cantidadPersonas+=1
     def setEquipo(self,equipo):
          personaFut.equipo=equipo
class entrenador(personaFut):
     def __init__(self,cedula,nombre,idFifa):
          personaFut.__init__(self,cedula,nombre)
          self.idFifa=idFida
class futbolista(personaFut):
     def __init__(self,cedula,nombre,dorsal):
          personaFut.__init__(self,cedula,nombre)
          self.dorsal = dorsal

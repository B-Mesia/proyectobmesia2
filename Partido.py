
class Partido:
  def __init__(self,dia,hora,equipolocal, equipovisitante, estadio):
    self.dia = dia
    self.hora = hora
    self.equipolocal = equipolocal
    self.equipovisitante = equipovisitante
    self.estadio = estadio


  def get_dia(self):
    return self.dia
  
  def get_hora(self):
    return self.hora
  def get_equipolocal(self):
    return self.equipolocal

  def get_equipovisitante(self):
    return self.__description

  def get_estadio(self):
    return self.estadio



  def set_dia(self,new_dia):
    self.__code = new_dia
  
  def set_hora(self,new_hora):
    self.__transmitter = new_hora
  def set_equipolocal(self,new_equipolocal):
    self.__receiver = new_equipolocal

  def set_equipovisitante(self,new_equipovisitante):
    self.__amount = new_equipovisitante
  def set_estadio(self,new_estadio):
    self.__description = new_estadio


  def show_partido(self):
    return f'Fecha:{self.dia}\nHora:{self.hora}\nEquipo local:{self.equipolocal}\nEquipo visitante:{self.equipovisitante}  Estadio:{self.estadio}\n'
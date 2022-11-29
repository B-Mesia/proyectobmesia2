from Equipo import Equipo


class Equipo_local(Equipo):

  def __init__(self,pais,codigo,grupo, localidad):
    Equipo.__init__(self,pais,codigo,grupo)
    self.localidad= True

  def get_localidad(self):
    return self.localidad
  def set_company(self,new_localidad):
    self.localidad = new_localidad

def show_equipo(self):
    return f'Equipo:Local\nPais:{Equipo.get_pais(self)}\nCodigo Nro:{Equipo.get_codigo(self)}\nGrupo:{Equipo.get_grupo(self)}'
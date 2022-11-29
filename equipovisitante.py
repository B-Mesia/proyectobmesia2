from Equipo import Equipo



class Equipo_visitante(Equipo):

  def __init__(self,pais,codigo,grupo, localidad):
    Equipo.__init__(self,pais,codigo,grupo)
    self.localidad= False


  def show_equipo(self):
    return f'Equipo:Visitante\nPais:{Equipo.get_pais(self)}\nCodigo Nro:{Equipo.get_codigo(self)}\nGrupo:{Equipo.get_grupo(self)}'
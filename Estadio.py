class Estadio():
    def __init__(self,nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion


    def get_nombre(self):
        return self.nombre
    def set_nombre(self,new_nombre):
     self.nombre = new_nombre
    def get_ubicacion(self):
        return self.ubicacion
    def set_ubicacion(self,new_ubicacion):
     self.ubicacion= new_ubicacion

    def show_estadio(self):
        return f'Nombre:{self.nombre}\nUbicacion:{self.ubicacion}\n'
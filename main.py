
from funciones import *



def main():
  
  db = {
    'equipos':{
    },
    'partidos':{
    },
    'estadios':{
    },
    }

  db = recive_data_text('base.txt',db)



  while True:
   
    print('Bienvenidos a al mundial de quatar 2022')

    while True:
      try:
        
        option = int(input('Ingrese la opcion que desea realizar:\n1.-Registrar partido\)
        if option not in range(1,6):
          raise Exception
        break
      except:
        print('Ingreso invalido')

    if option == 1:
   
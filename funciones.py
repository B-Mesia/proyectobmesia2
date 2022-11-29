import requests
import pickle
import os
from random import randint
from datetime import datetime
from Partido import Partido
from Estadio import Estadio
from Equipo import Equipo
from equipolocal import Equipo_local
from equipovisitante import Equipo_visitante



def endpoint_json():

  url = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/teams.json'

  response = requests.request('GET',url) 

  return response.json()

def dict_equipos(endpoint,key):

  equipos = {} 

 
  for equipo in endpoint[0][key]:
    localidad = equipo['Quatar'] 
 
    if localidad:
      
      pais = equipo['name']
      codigo = equipo['fifa_code']
      grupo = equipo['group']
      cod2= equipo['id']

      equipo = Equipo_local(pais,codigo,grupo,localidad)

    else:
      
      pais = equipo['name']
      codigo = equipo['fifa_code']
      grupo = equipo['group']
      cod2= equipo['id']
     
      equipo = Equipo_visitante(pais,codigo,grupo)

    equipos[cod2] = equipo 

  return equipos 
    
def valid_data_user(equipo):
 
  print(equipo.show_equipo()) 

  while True:
    try:
     
      option = input('Estos son los datos de su equipo a registrar, si (S) o no (n):\n==> ').lower()
      if option != 's' and option != 'n':
        raise Exception
      break
    except:
      print('Opcion invalida')

  return option
 
def registro(equipos,db):
  
  while True:
    try:
      
      cod2 = int(input('Ingrese el codigo fifa afiliado a su equipo:\n==> '))
      break
    except:
      print('Ingreso invalido')

  for key,values in db['equipo'].items():
    if key == cod2:
      print('El equipo ya esta registrado en el sistema')
      print('\n') 
      return db

  for cod2,value in equipos.items():
    if cod2 == int(cod2): 
      if value.get_localidad():
        print('\n')
        option = valid_data_user(value) 
        if option == 's': 
         
          print('\n')
          pais = value.get_pais()
          grupo = value.get_grupo()
          codigo = value.get_codigo()
         
          equipo = Equipo_visitante(pais,codigo,grupo)

          db['equipos'][cod2] = equipo 
          print('Equipo 1 registrado') 

          return db 
        else:
          break 
      
  
  print('\n')
  print('Codigo incorrecto')
  print('Asegurate de haber seleccionado bien.')
  print('\n')

  return db



def recive_data_text(name_txt,db):

  binary_read = open(name_txt,'rb') 

  if os.stat(name_txt).st_size != 0: 
    db = pickle.load(binary_read) 

  binary_read.close() 
  return db
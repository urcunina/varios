# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 19:38:19 2024

@author: Lennin Escobar
"""
import requests
import csv
import datetime 
import pandas as pd
import random
import time
import json
# Script de incializacion Orion 

IP_Orion="localhost"
IP_Orion="192.168.43.173"#Celular
Port_Orion="1026"


# Get version
def version():
    url='http://'+IP_Orion+':'+Port_Orion+'/version'
    response=requests.get(url)
    print(response.status_code)
    print(response.content) 

# Consulta una entidad específica
def consulta_entiti(entidad):
    url='http://'+IP_Orion+':'+Port_Orion+'/v2/entities/'+entidad
    headers={"Accept":"application/json"}
    response=requests.get(url,headers=headers)
    print(response.status_code)
    response=response.content.decode("utf-8").replace("'", '"')
    response_JSON=json.loads(response)
    print(response_JSON)

# Crea entidad IVA
def crea_entidad_IVA(valor):
        try:
                ContextDataJSON={"id": "",
                                "type": "variable",

                                "valor": {
                                "value": valor,
                                "type": "integer"
                                },
                                "tipo":{
                                "value": "variable",
                                "type": "String"
                                }
                                }
                
                ContextDataJSON['tipo']['value']='variable' # Para filtrar datos desde fiware orion
                ContextDataJSON['id']='IVA'
                # ContextDataJSON['id']='abono_'+str(servicio)  # Nombre de la entidad abono abono_servicio_+randit()
                url='http://'+IP_Orion+':'+Port_Orion+'/v2/entities'
                headers={"Accept":"application/json"}
                response= requests.post(url,headers=headers,json=ContextDataJSON) 
                # print(response.status_code)
                if (response.status_code) == 201:
                    print('Entidad IVA creada satisfactoriamente')
                    return "ok" , ContextDataJSON['id']
                else:
                    print('Al entidad IVA ya existe')
                    return "No ok" , ContextDataJSON['id']

        except:
                return "La entidad IVA NO pudo ser creada",''


# Crea la entidad counter_services_bogota
def crea_counter_services():
        try:
                ContextDataJSON={"id": "counterservices",
                                "type": "counter",
                                
                                "Bogota": {
                                "value": "200100",
                                "type": "String"
                                },
                                "Barranquilla": {
                                "value": "0",
                                "type": "String"
                                },
                                "Medellin": {
                                "value": "400000",
                                "type": "String"
                                },
                                "tipo":{
                                "value": "modelo",
                                "type": "String"
                                }
                                }
                ContextDataJSON['id']='counterservices'
                ContextDataJSON['type']='counter'  
                            
                ContextDataJSON['tipo']['value']='counter' # Para filtrar datos desde fiware orion
                url='http://'+IP_Orion+':'+Port_Orion+'/v2/entities'
                headers={"Accept":"application/json"}
                response= requests.post(url,headers=headers,json=ContextDataJSON) 
                # print(response.status_code)
                if (response.status_code) == 201:
                        return "El counter ha sido creado"
                if (response.status_code) == 422:
                        return "El counter ya existe"
                if (response.status_code) == 400:
                    return "El counter ya existe"
        except:
            return "El counter NO ha sido creado"

# Crea la entidad global_message
def crea_global_message():
        try:
                ContextDataJSON={"id": "global_message",
                                "type": "message",
                                
                                "global_message": {
                                "value": "🔧⛏️  les da la bienvenida ⛏️🔧",
                                "type": "String"
                                },
                                "tipo":{
                                "value": "message",
                                "type": "String"
                                }
                                }
                ContextDataJSON['id']='global_message'
                ContextDataJSON['type']='message'  
                            
                ContextDataJSON['tipo']['value']='counter' # Para filtrar datos desde fiware orion
                url='http://'+IP_Orion+':'+Port_Orion+'/v2/entities'
                headers={"Accept":"application/json"}
                response= requests.post(url,headers=headers,json=ContextDataJSON) 
                # print(response.status_code)
                if (response.status_code) == 201:
                        print('El global_message ha sido creado')
                        return "El global_message ha sido creado"
                if (response.status_code) == 422:
                        print('El global_message ya existe')
                        return "El global_message ya existe"
                if (response.status_code) == 400:
                    print('El global_message ya existe')
                    return "El global_message ya existe"
        except:
            print('El global_message NO ha sido creado')
            return "El global_message NO ha sido creado"
        
# Crea un modelo de producto
def crea_modelo(modelo,marca,producto):
        try:
                ContextDataJSON={"id": "---",
                                "type": "----",
                                "marca": {
                                "value": "---",
                                "type": "String"
                                },
                                "producto": {
                                "value": "---",
                                "type": "String"
                                },
                                "tipo":{
                                "value": "modelo",
                                "type": "String"
                                }
                                }
                ContextDataJSON['id']=str(modelo)
                ContextDataJSON['type']='modelo'  
                
                ContextDataJSON['marca']['value']=marca        
                ContextDataJSON['producto']['value']=producto

                
                ContextDataJSON['tipo']['value']='modelo' # Para filtrar datos desde fiware orion
                url='http://'+IP_Orion+':'+Port_Orion+'/v2/entities'
                headers={"Accept":"application/json"}
                response= requests.post(url,headers=headers,json=ContextDataJSON) 
                # print(response.status_code)
                if (response.status_code) == 201:
                        return "El modelo ha sido creado"
                if (response.status_code) == 422:
                        return "El modelo ya existe"
                if (response.status_code) == 400:
                    print(modelo,marca,producto)
                    return "El modelo ya existe"
        except:
            print(modelo,marca,producto)
            return "El modelo NO ha sido creado"

# Crea parte 
def crea_entidad_parte(referencia,nombre_parte,cantidad,precio,observacion,fecha_actualizacion,ciudad,delivery,marca):
        try:
                ContextDataJSON={"id": "",
                                "type": "parte",

                                "referencia": {
                                "value": "",
                                "type": "String"
                                },
                                "cantidad": {
                                "value": 0,
                                "type": "integer"
                                },
                                "descripcion": {
                                "value": '',
                                "type": "String"
                                },
                                "nombre_parte": {
                                "value": "",
                                "type": "String"
                                },
                                "precio":{
                                "value": "",
                                "type": "String"
                                },
                                "observacion":{
                                "value": "",
                                "type": "String"
                                },
                                "ciudad":{
                                "value": "",
                                "type": "String"
                                },
                                "fecha_actualizacion":{
                                "value": "",
                                "type": "DateTime"
                                },
                                "delivery":{
                                "value": "",
                                "type": "String"
                                },
                                "marca":{
                                "value": "",
                                "type": "String"
                                },
                                "activo":{
                                "value": 1,
                                "type": "integer"
                                },
                                "tipo":{
                                "value": "parte",
                                "type": "String"
                                }
                                }
                
                ContextDataJSON['type']='parte' 

                ContextDataJSON['referencia']['value']=referencia        
                ContextDataJSON['cantidad']['value']=cantidad
                ContextDataJSON['nombre_parte']['value']=nombre_parte
                ContextDataJSON['precio']['value']=int(precio)
                ContextDataJSON['observacion']['value']=observacion
                ContextDataJSON['fecha_actualizacion']['value']=fecha_actualizacion
                ContextDataJSON['ciudad']['value']=ciudad
                ContextDataJSON['delivery']['value']=delivery
                ContextDataJSON['marca']['value']=marca
                
                ContextDataJSON['tipo']['value']='parte' # Para filtrar datos desde fiware orion
                crea_parte=0
                while(crea_parte==0):
                        ContextDataJSON['id']='parte_'+str(random.randint(0,1000000))  # Nombre de la entidad abono abono_servicio_+randit()
                        # ContextDataJSON['id']='abono_'+str(servicio)  # Nombre de la entidad abono abono_servicio_+randit()
                        url='http://'+IP_Orion+':'+Port_Orion+'/v2/entities'
                        headers={"Accept":"application/json"}
                        response= requests.post(url,headers=headers,json=ContextDataJSON) 
                        # print(response.status_code)
                        if (response.status_code) == 201:
                                crea_parte=1
                                break
                        else:
                               time.sleep(1)
                return "ok" , ContextDataJSON['id']

        except:
                return "La parte NO pudo ser creada",''
            
###############################
#Elimina entidad
###############################
def borra_entidad(id_entiti):
        url='http://'+IP_Orion+':'+Port_Orion+'/v2/entities/'+id_entiti
        headers={"Accept":"application/json"}
        response=requests.delete(url,headers=headers)
        print(response.status_code)

###############################
#Actualiza modelos
###############################
def actualiza_modelos():
    file = open('modelos.csv')
    csvreader = csv.reader(file)
    for row in csvreader:
        marca=row[0].split(';')[0]
        producto=row[0].split(';')[1]
        modelo=row[0].split(';')[2].replace('/', '*', 1)
        modelo=modelo.replace(' ', '_', 10)    
        crea_modelo(modelo,marca,producto)

###############################
# Actualiza inventario from CSV
###############################
def actualiza_inventario():
    df = pd.read_csv('samsung.csv',delimiter=';')
    df = df.reset_index()  # make sure indexes pair with number of rows
    for index, row in df.iterrows():
        # print(row['PARTS_CODE'],row['PARTS_DESC'].split(';')[0],row['STOCK_QTY'])
        referencia=row['PARTS_CODE'].upper()
        nombre_parte=row['PARTS_DESC'].split(';')[0].upper()
        cantidad=row['STOCK_QTY']
        fecha_actualizacion=str(datetime.date.today())
        precio=random.randint(5000,100000)
        observacion=''
        ciudad='Bogotá'
        marca='Samsung'.upper()
        delivery=''
        print(crea_entidad_parte(referencia,nombre_parte,cantidad,precio,observacion,fecha_actualizacion, ciudad,delivery,marca))
    


# version()
#actualiza_modelos()
#crea_entidad_IVA()   
# crea_counter_services()
# crea_global_message()
# actualiza_inventario()
# borra_entidad('global_message')
consulta_entiti('200103') 




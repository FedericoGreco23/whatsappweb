import re
import random
#!/usr/bin/env python
# -*- coding: utf-8 -*-


def get_texto_set():
	# (1) MODIFICAR LA RUTA DEL ARCHIVO CON EL TEXTO. ES IMPORTANTE QUE SE UTILICE LA DOBLE BARRA (\\) PARA SEPARAR DIRECTORIOS
    archivo = open('config\\prueba-Fede2022\\set_mensajes.csv','r', encoding='utf-8')
    texto_archivo = archivo.read()
    #lineas_archivo = re.findall(r'[^"]{4}[^"]*',texto_archivo)
    #return lineas_archivo[random.randrange(0,len(lineas_archivo)-1)]
    return texto_archivo

def get_texto_contactos():
	# (2) MODIFICAR LA RUTA DEL ARCHIVO CON LOS CONTACTOS. ES IMPORTANTE QUE SE UTILICE LA DOBLE BARRA (\\) PARA SEPARAR DIRECTORIOS
    archivo = open('config\\prueba-Fede2022\\set_contactos_corto.csv','r', encoding='utf-8')
    return archivo.read()

def get_lista_claves(texto):
    linea_texto = re.split('\n',texto)[0]
    return re.findall("[A-Z]+", linea_texto)

def get_lista_contactos(texto):
    lista = re.split('\n', texto)
    lista.pop(0)
    return lista

def get_mensaje_enviar(mensaje_inicial, lista_valores, lista_claves):
    mensaje_final = mensaje_inicial
    for i in range(1, len(lista_claves)):
        mensaje_final = reemplazar_valor_texto(mensaje_final, lista_valores[i], lista_claves[i])
    return mensaje_final

def get_lista_valores(linea_texto):
    ret = re.findall(r'[^"]+', linea_texto)
    for i in range(0, ret.count(",")):
        ret.remove(",")
    return ret

def reemplazar_valor_texto(texto, valor_nuevo, key):
    texto_final = texto
    texto_final = re.sub(key, valor_nuevo, texto_final)
    return texto_final

import time
import re
from datetime import datetime
from texto import get_texto_set, get_texto_contactos, get_lista_claves, get_lista_contactos, get_mensaje_enviar, get_lista_valores
import pywhatkit as kit
import pyautogui
import keyboard as k

"""

archivo: envio_whatsapp.py
función: Envío masivo de mensajes via whatsapp  
autor:   Federico Greco 
creado:  26/07/2022  
versión: 27/07/2022 14:35

"""



# EL NUMERO DE TELEFONO TIENE QUE SER EL PRIMERO EN EL CSV CON LOS CONTACTOS
def main():
    print("****** ENVIO MENSAJES WHATSAPP ******")
    print("******       VERSION v3.0      ******")
    #Este timer está para esperar a que cargue bien el driver y whatsapp.
    contactos = get_lista_contactos(get_texto_contactos())
    claves = get_lista_claves(get_texto_contactos())
    cantidad = int(input("¿Cuantos quieres enviar?: "))
    for elem in contactos:
        if cantidad == 0:
            cantidad = int(input("¿Quieres enviar más mensajes? (0=No, x>0=Si): "))
            if cantidad == 0:
                ###driver.close()
                break
        lista_valores = get_lista_valores(elem)
        print("\n",lista_valores,"\n")
        numero_enviar = lista_valores[0]

        #print("La variable contactos contiene: ")
        #print(contactos,"\n")
        #print("La variable clave contiene: ")
        #print(claves,"\n")
        #print("La variable lista_valores contiene: ")
        #print(lista_valores,"\n")

        print("\n","Enviando mensaje","\n")

        #texto_enviar = get_mensaje_enviar(get_texto_set(),lista_valores, claves)
        mensaje_final = get_texto_set() ##Cargo el texto del mensaje set_mensaje
        for i in range(0, len(claves)):
            #mensaje_final = reemplazar_valor_texto(mensaje_final, lista_valores[i], claves[i])
            texto_final = mensaje_final
            texto_final = re.sub(claves[i], lista_valores[i], texto_final)

        #No se porque la linea de arriba no cambia el nombre por el valor que obtiene del csv, porque si pasa por las 2 columnas, numero, nombre y link.
        #Asi que hago esta tarea para realmente sustituior la variable NOMBRE en el texto del mensaje por la variable del csv.
        texto_final = re.sub('NOMBRE', lista_valores[1], texto_final)
        time.sleep(1)

        kit.sendwhatmsg_instantly(numero_enviar, str(texto_final), 6, True, 4)
        pyautogui.click(1050, 950)
        k.press_and_release('enter')

        ###enviar_mensaje(driver, str(texto_enviar), elem)
        time.sleep(1)
        #Este timer está para que luego de que se presione el botón de enviar, el mensaje realmente se envíe.
        cantidad = cantidad - 1
        print("Restantes: "+str(cantidad))

if __name__ == "__main__":
    main()

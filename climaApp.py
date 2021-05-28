from tkinter import *
import requests
#La Unión
#50acf6ee499215299ec4d90b1fa7d585
#api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}


def mostrar_respuesta(clima):
    try:
        nombre_ciudad = clima["name"]
        descripcion = clima["weather"][0]["description"]
        temperatura = clima["main"]["temp"]

        mostrar_ciudad["text"] = nombre_ciudad
        mostrar_temperatura["text"] = str(int(temperatura)) + "°C"
        mostrar_descripcion["text"] = descripcion
    except :
         mostrar_ciudad["text"] = "Intenta nuevamente"


def clima_json(ciudad):
    try:
        API_key = "50acf6ee499215299ec4d90b1fa7d585"
        URL = "https://api.openweathermap.org/data/2.5/weather"
        parametros = {"APPID" : API_key, "q": ciudad, "units": "metric", "lang": "es"}
        response = requests.get(URL, params = parametros)
        clima = response.json()  
        mostrar_respuesta(clima)
    except:
        print("ERROR")
    #print(response.json())


ventana = Tk()
ventana.geometry('350x550')

texto_ciudad = Entry(ventana, font = ('Courier', 20, 'normal'), justify= 'center')
texto_ciudad.pack(padx = 30, pady = 30)

obtener_clima = Button(ventana, text = 'Obtener Clima',font = ('Courier', 20, 'normal'), command = lambda: clima_json(texto_ciudad.get()))
obtener_clima.pack()

mostrar_ciudad = Label(font = ('Courier', 20, 'normal'))
mostrar_ciudad.pack(padx = 20, pady = 20)

mostrar_temperatura = Label(font = ('Courier', 20, 'normal'))
mostrar_temperatura.pack(padx = 10, pady = 10)

mostrar_descripcion = Label(font = ('Courier', 20, 'normal'))
mostrar_descripcion.pack(padx = 10, pady = 10)


ventana .mainloop()
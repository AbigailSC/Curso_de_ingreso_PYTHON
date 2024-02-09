import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Abigail
apellido: Sarzuri
---
Ejercicio: entrada_salida_01
---
Enunciado:

para saber el costo de un viaje necesitamos el siguiente algoritmo,
sabiendo que el precio por kilo de pasajero es 1000 pesos
Se ingresan todos los datos por PROMPT
los datos a solicitar de dos personas son,
nombre, edad y peso
se pide  armar el siguiente mensaje
"hola jose y maria , sus pesos son 80 kilos y 60 kilos respectivamente
, sumados da 140 kilos , el promedio de edad es 33 y su viaje vale 140 000 pesos  "
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        precio_kilo = 1000
        nombre = prompt(title="Ingrese el nombre", prompt="Ingrese su primer nombre")
        edad = prompt(title="Ingrese la edad", prompt="Ingrese la primer edad")
        edad = int(edad)
        peso = prompt(title="Ingrese el peso", prompt="Ingrese el primer peso")
        peso = float(peso)

        segundo_nombre = prompt(title="Ingrese el nombre", prompt="Ingrese su segundo nombre")
        segunda_edad = prompt(title="Ingrese la edad", prompt="Ingrese la segunda edad")
        segunda_edad = int(segunda_edad)
        segundo_peso = prompt(title="Ingrese el peso", prompt="Ingrese el segundo peso")
        segundo_peso = float(segundo_peso)

        peso_conjunto = peso + segundo_peso

        edad_promedio = (edad + segunda_edad) / 2
        edad_promedio = int(edad_promedio)

        costo_viaje = peso_conjunto
        costo_viaje = int(costo_viaje)
        costo_viaje = (costo_viaje * precio_kilo)
        alert(title="Resultado", message=f"Hola {nombre} y {segundo_nombre} , sus pesos son {peso} kilos y {segundo_peso} kilos respectivamente, sumados da {peso_conjunto} kilos , el promedio de edad es {edad_promedio} y su viaje vale {costo_viaje} pesos")
    


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

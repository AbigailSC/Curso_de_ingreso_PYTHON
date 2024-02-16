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

La empresa spaceX , nos contrata para poder hacer el cálculo de precio final y descuentos para un viaje al espacio exterior
el costo por millón de kilómetros es de 8 bitcoin 

podes viajar a Marte (60 millones de KM) , la Luna (½ millón de KM)y a Titan (1300 millones de KM)
podes elegir si viajar en verano, primavera  otoño o invierno.

para los viajes a Marte
Si viajan más de 5 personas te hacemos un 50 % de descuento sobre el precio,
viajando en verano al precio con descuento se le suma un 10% , en otoño y primavera se le suma un 25% al precio con descuento.

para los viajes la Luna 
si viajan más de 5 personas te hacemos un 40 % de descuento sobre el precio,
viajando en verano al precio con descuento se le suma un 15% ,  en otoño y primavera al precio con descuento se le suma un 25%

para los viajes a Titan
si viajan más de 5 personas te hacemos un 30 % de descuento sobre el precio,
viajando en verano al precio final se le suma un 10% , en otoño y primavera al precio con descuento se le suma un 20%


'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        costo_millon_kilometro = 8
        destino_seleccionado = prompt(title="Seleccionar destino", prompt="Seleccione el destino a donde quiere ir")
        estacion_seleccionada = prompt(title="Seleccionar estación", prompt="Seleccione la estación del año en que quiere ir")
        cantidad_personas = prompt(title="Seleccionar cantidad personas", prompt="Seleccione la cantidad de personas que van a viajar")
        cantidad_personas = int(cantidad_personas)
        mensaje_respuesta = ""

        destino_kilometros = 0
        porcentaje_descuento = 0
        porcentaje_aumento_adicional = 0
        
        match destino_seleccionado:
            case "Marte":
                destino_kilometros = 60000000
                if cantidad_personas > 5:
                    porcentaje_descuento = 50
                match estacion_seleccionada:
                    case "Verano":
                        porcentaje_aumento_adicional = 10
                    case "Otoño" | "Primavera":
                        porcentaje_aumento_adicional = 25
            case "Luna":
                destino_kilometros = 500000
                if cantidad_personas > 5:
                    porcentaje_descuento = 40
                match estacion_seleccionada:
                    case "Verano":
                        porcentaje_aumento_adicional = 15
                    case "Otoño" | "Primavera":
                        porcentaje_aumento_adicional = 25
            case "Titan":
                destino_kilometros = 1300000000
                if cantidad_personas > 5:
                    porcentaje_descuento = 30
                match estacion_seleccionada:
                    case "Verano":
                        porcentaje_aumento_adicional = 10
                    case "Otoño" | "Primavera":
                        porcentaje_aumento_adicional = 20

        precio_viaje = costo_millon_kilometro * destino_kilometros
        precio_descuento_personas = (precio_viaje * porcentaje_descuento) / 100
        precio_descuento_personas = int(precio_descuento_personas)
        precio_parcial = precio_viaje - precio_descuento_personas
        precio_parcial_aumento = (precio_parcial * porcentaje_aumento_adicional) / 100
        precio_parcial_aumento = int(precio_parcial_aumento)
        precio_final = precio_parcial + precio_parcial_aumento
        precio_final = int(precio_final)

        mensaje_precio_viaje = f"Su viaje a {destino_seleccionado} tiene un valor de {precio_viaje} bitcoins."
        mensaje_descuento_personas = f"Además de que se le aplica un descuento del {porcentaje_descuento}% porque viajan más de 5 personas, quedando el precio del viaje en {precio_parcial} bitcoins."
        mensaje_precio_parcial = f"Y por ultimo se le agrega un aumento del {porcentaje_aumento_adicional}% por viajar en {estacion_seleccionada}."

        mensaje_respuesta = mensaje_precio_viaje

        if cantidad_personas > 5:
            mensaje_respuesta = f"{mensaje_respuesta} {mensaje_descuento_personas}"

        if porcentaje_aumento_adicional > 0:
            mensaje_respuesta = f"{mensaje_respuesta} {mensaje_precio_parcial}"

        mensaje_respuesta = f"{mensaje_respuesta}\nEl precio final es de {precio_final} bitcoins."

        alert(title="Calculadora de costo de viaje", message=mensaje_respuesta)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

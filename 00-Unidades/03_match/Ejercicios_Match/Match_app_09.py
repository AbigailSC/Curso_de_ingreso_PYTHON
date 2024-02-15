import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Abigail
apellido: Sarzuri
---
Ejercicio: Match_09
---
Una agencia de viajes cobra $15.000 por cada estadía como base. 
Luego para calcular las tarifas total realiza el siguiente cálculo, 
en función de la estación del año y del destino elegido:
    Si es invierno: 
        Bariloche tiene un aumento del 20% 
        Cataratas y Córdoba tienen un descuento del 10%
        Mar del plata tiene un descuento del 20%
    Si es Verano:
        Bariloche tiene un descuento del 20%
        Cataratas y Cordoba tienen un aumento del 10%
        Mar del plata tiene un aumento del 20%
    Si es Primavera u Otoño:
        Bariloche tiene un aumento del 10%
        Cataratas tiene un aumento del 10%
        Mar del plata tiene un aumento del 10%
        Córdoba tiene precio sin descuento

'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.label_estaciones = customtkinter.CTkLabel(master=self, text="Estaciones")
        self.label_estaciones.grid(row=0, column=0, padx=20, pady=10)
        estaciones = ['Verano', 'Otoño', 'Invierno', 'Primavera']
        self.combobox_estaciones = customtkinter.CTkComboBox(master=self, values=estaciones)
        self.combobox_estaciones.grid(row=1, column=0, padx=20, pady=(10, 10))

        
        self.label_destinos = customtkinter.CTkLabel(master=self, text="Destinos")
        self.label_destinos.grid(row=2, column=0, padx=20, pady=10)
        destinos = ['Bariloche', 'Mar del plata', 'Cataratas', 'Cordoba']
        self.combobox_destino = customtkinter.CTkComboBox(master=self, values=destinos)
        self.combobox_destino.grid(row=3, column=0, padx=20, pady=(10, 10))

        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=4, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        precio_base_estadia = 15000
        estacion_seleccionada = self.combobox_estaciones.get()
        destino_seleccionado = self.combobox_destino.get()
        match estacion_seleccionada:
            case "Invierno":
                match destino_seleccionado:
                    case "Bariloche":
                        ajuste_porcentaje = 1.20
                    case "Mar del plata":
                        ajuste_porcentaje = 0.80
                    case _:
                        ajuste_porcentaje =  0.90
            case "Verano":
                match destino_seleccionado:
                    case "Bariloche":
                        ajuste_porcentaje = 0.80
                    case "Mar del plata":
                        ajuste_porcentaje =  1.20
                    case _:
                        ajuste_porcentaje = 1.10
            case "Primavera" | "Otoño":
                match destino_seleccionado:
                    case "Cordoba":
                        ajuste_porcentaje = 1
                    case _:
                        ajuste_porcentaje = 1.10
            
        precio_total = precio_base_estadia * ajuste_porcentaje
        precio_total = int(precio_total)
        alert(title="Precio total", message=f"El precio total de la estadía en {destino_seleccionado} en la estación {estacion_seleccionada} es de ${precio_total}")
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Abigail
apellido: Sarzuri
---
TP: IF_Iluminacion
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

        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_destino = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_destino.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        costo_kilometro = 8
        destino_seleccionado = prompt(title="Seleccionar destino", prompt="Seleccione el destino a donde quiere ir")
        estacion_seleccionada = prompt(title="Seleccionar estación", prompt="Seleccione la estación del año en que quiere ir")
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
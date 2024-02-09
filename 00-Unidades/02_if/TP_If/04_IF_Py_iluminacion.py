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
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        precio_producto = 800
        marca_producto = self.combobox_marca.get()
        cantidad_productos = self.combobox_cantidad.get()
        cantidad_productos = int(cantidad_productos)
        descuento = 0

        if (cantidad_productos > 5):
            descuento = 50
        elif (cantidad_productos == 5 and marca_producto == "ArgentinaLuz"):
            descuento = 40
        elif(cantidad_productos == 5): 
            descuento = 30
        elif(cantidad_productos == 4 and (marca_producto == "ArgentinaLuz" or marca_producto == "FelipeLamparas")):
            descuento = 25
        elif(cantidad_productos == 4):
            descuento = 20
        elif(cantidad_productos == 3 and marca_producto == "ArgentinaLuz"):
            descuento = 15
        elif(cantidad_productos == 3 and marca_producto == "FelipeLamparas"):
            descuento = 10
        elif(cantidad_productos == 3):
            descuento = 5

        precio_total = precio_producto * cantidad_productos
        precio_descuento = (precio_total * descuento) / 100
        precio_descuento = int(precio_descuento)
        precio_final = precio_total - precio_descuento

        mensaje = f"Por la compra de {cantidad_productos} productos marca {marca_producto}, usted tiene un descuento del {descuento}%, el total de su compra en ${precio_total}, agregando el descuento de ${precio_descuento} ,el total de su compra queda en ${precio_final}."
        
        if (precio_final > 4000):
            precio_final_temporal = precio_final
            precio_descuento_adicional = (precio_final * 5) / 100
            precio_descuento_adicional = int(precio_descuento_adicional)
            precio_final = precio_final_temporal - precio_descuento_adicional
            mensaje = f"Por la compra de {cantidad_productos} productos marca {marca_producto}, usted tiene un descuento del {descuento}% más un 5% porque su compra supero los $4000, el total de su compra en ${precio_total}, agregando el descuento de ${precio_descuento} ,el total de su compra queda en ${precio_final}."
        alert("Precio final de su compra", message=mensaje)
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
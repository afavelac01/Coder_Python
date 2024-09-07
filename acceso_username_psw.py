#Crear un programa que ingrese usuarios y password and una base de datos. COn tres funciones:
#una para registrar nuesvos usuarios y almacenarlos en una base de datos tipo diccionario
#2nda para grabar los usuarios en archivo texto
#3ra para que un usuario intente accesar y que ingrese sus credenciales y verifique si son validas

import os.path
file_path = 'C:/Python/Ejercicios/1erEntrega'
import tkinter as tk
from tkinter import filedialog
from tkinter import *

BD={}

def registro():
    
    user = input("Ingrese su nombre de usuario: ")
    if user not in BD:
        psw =  input("Ingrese password deseado: ")
        BD.update({user:psw})
        
    else:
        print("usuario ya existe, ingrese uno diferente")
        registro()
    
def leerData(BD):
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    print(folder_selected)
    
    pass

def guardarArchivo():
    print("salvando datos de")
    pass

def crearArchivo(filepath,filename):
    completeName = os.path.join(filepath, filename+".txt")         
    file1 = open(completeName, "w")
    file1.write(str(BD))
    file1.close()
    pass

def leerArchivo():
    print("select file")

    root = tk.Tk()
    root.title("Select a File to be imported")

    open_button = tk.Button(root, text="Open File", command=filedialog.askopenfilename(title="Select a File", filetypes=[("Text files", "*.txt"), ("All files", "*.*")]))
    open_button.pack(padx=20, pady=20)

    selected_file_label = tk.Label(root, text="Selected File:")
    selected_file_label.pack()

    file_text = tk.Text(root, wrap=tk.WORD, height=10, width=40)
    file_text.pack(padx=20, pady=20)
      
    #file1 = open(completeName, "r")
    #content=file1.read()
    #print(content)
    #file1.close()
    pass

def selectFile():

    """root = Tk()
    root.withdraw()
    path = filedialog.askdirectory()
    filename=tkinter.filedialog.askopenfilename()"""

    file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        selected_file_label.config(text=f"Selected File: {file_path}")
        print(file_path)
    return file_path
    


    
    #completeName = os.path.join(filepath, filename+".txt")  
    #return completeName

def login():
    user = input("Ingrese su nombre de usuario: ")
    if user not in BD:
        psw = input("Ingrese su contrasena: ")
        if checar_psw:
            print("Bienvenido al Sistema")
    else:
        Print("")
    pass

#print(BD)"""
#"filename = input("nombre de archivo? :")"
task='none'
while task != 'fin':
    task = input ("seleccione tarea, escriba:\n r = registro nuevo\n a = accesar\n l= leer\n c = crear\n fin para terminar\n")
    if task == 'r':
        registro()
    elif task == 'a':
        login()
    elif task=='l':
        leerArchivo()
    elif task=='c':
        crearArchivo(file_path,filename)
    else:
        break
"""filename = input("nombre de archivo? :")
#crearArchivo(file_path,file_path)
print("EL ARCHIVO LEIDO")
leerArchivo(file_path,filename)"""

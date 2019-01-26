import os

def rename_files():
    #(1) obtener los nombres de archivos de una carpeta
    file_list = os.listdir(r"C:\OPP\prank")
    #print(file_list) //Imprime la lista de los archivos de imagenes
    saved_path = os.getcwd()
    print("El directorio actual es "+saved_path)
    os.chdir(r"C:\OPP\prank")

    #(2) renombra nombre de cada archivo
    for file_name in file_list:
        print("Nombre anterior - "+file_name)
        #print("Nuevo nombre - "+file_name.translate(None,"0123456789")) 
        #os.rename(file_name, file_name.translate(None,"0123456789") // Esta funcionalidad genera el error: TypeError: translate() takes exactly one argument (2 given)
        print("Nuevo nombre - "+file_name.strip("0123456789"))
        os.rename(file_name,file_name.strip("0123456789"))
    os.chdir(saved_path)
    
rename_files()

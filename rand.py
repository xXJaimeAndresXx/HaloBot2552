import os, random

#Choose a random file from the folder
def randomFile():
    file= random.choice(os.listdir("C:/Users/Jaime Andres/Desktop/Paleta/HaloCinematics"))
    print("El dominio invita al Reclamador presente a recordar los acontecimientos ocurridos en:"+ file)
    return file




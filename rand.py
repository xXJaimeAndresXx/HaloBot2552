import os, random
def randomFile():
    file= random.choice(os.listdir("C:/Users/Jaime Andres/Desktop/Paleta/HaloCinematics"))
    print("El dominio invita al Reclamador presente a recordar los acontecimientos ocurridos en:"+ file)
    return file




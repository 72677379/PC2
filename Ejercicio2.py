#¿Qué es una historia de usuario?

#Es una información que se da al programador para ver a que se dedica y que es lo que quiere una empresa.
#Sirve para darnos cuenta en que podemos ayudar a la empresa o cual es su necesidad.
#Ejemplo: 
#Empresa de música
#Como empresa quiero un programa que me pueda registrar el número de canciones que se escuchan al dia y guardarlas
import time
def musica():
    musicas = []
    a = int(input("Cuantas musicas se reprodujeron al día? "))
    musicas.append(a)
    print("procesando...")
    time.sleep(6)
    print("Se guardo correctamente tu registro de musicas ", musicas)
musica()
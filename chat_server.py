# Importamos las librerias necesarias
import socket
# Establecemos el tipo de socket/conexion
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 5000 # Puerto de comunicacion
sock.bind(('18.207.124.217',port)) # IP y Puerto de conexion en una Tupla

print ("esperando conexiones en el puerto ", port)
# Vamos a esperar que un cliente se conecte
# Mientras tanto el script se va a pausar
sock.listen(1)
# Cuando un cliente se conecte vamos a obtener la client_addr osea la direccion
# tambien vamos a obtener la con, osea la conexion que servira para enviar datos y recibir datos
con, client_addr =  sock.accept()

name = "Server"
command = "NULL"

while command != "END":
    command = input(name+": ")
    msgSend = name+": "+command
    con.send(msgSend.encode()) # Enviamos el texto al cliente que se conecta
    msgReceive = con.recv(4096)
    print(msgReceive.decode())  

con.close() # Cerramos la conexion
sock.close() # Cerramos el socket
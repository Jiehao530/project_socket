import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/../../" ))
import socket
import threading
from chat_socket_project.config.settings import IP, PORT


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(5)
clients = {}

def manage_client(connection, address):
    

print("[*] Server awaiting connection...")
while True:
    connection, address = server.accept()
    threading.Thread(target=manage_client, args=(connection, address)).start()
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/../../" ))
import socket
import threading
from config.settings import IP, PORT
from auth.login import user_authentication
from ia.openai import get_response_ia


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(5)
clients = {}

def manage_client(connection, address):
    print(f"[*] A client with the address: {address} has connected")
    try:
        user = user_authentication(connection)
        if not user:
            connection.close()
            return
        clients[connection] = user
    except Exception as error:
        print(f"[x] Error: {error}")
        connection.close()
        return
    
    try:
        while True:
            message = connection.recv(1024).decode()
            if not message or message.lower() == "exit":
                break

            if message.startswith("IA"):
                message_for_ia = message[2:].strip()
                response = get_response_ia(message_for_ia)
                connection.send(f"ChatGPT: {response}".encode())

            else:
                print(f"The user {user} said {message}")
                message_to_send = f"{user}: {message}"
                for client in clients:
                    if client != connection:
                        client.send(message_to_send.encode())

    except Exception as error:
        print(f"[x] Error : {error}")
    
    print(f"[*] Client disconnected: {user} with address {address}")
    clients.pop(connection)
    connection.close()


print("[*] Server awaiting connection...")
while True:
    connection, address = server.accept()
    threading.Thread(target=manage_client, args=(connection, address)).start()

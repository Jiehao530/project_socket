import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/../../" ))
import socket
import threading
from config.settings import IP, PORT

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))

def get_messages():
    while True:
        try:
            message = client.recv(1024).decode()
            if not message:
                break
            print(message)
        except:
            break

threading.Thread(target=get_messages, daemon=True).start()
while True:
    message = str(input("> "))
    if message.lower == "exit":
        break
    client.send(message.encode())
client.close()
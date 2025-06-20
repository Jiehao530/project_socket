import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/../" ))
from auth.database import mongo_client
from passlib.context import CryptContext

crypt = CryptContext(schemes=["bcrypt"])

def user_authentication(connection):
    while True:
        connection.send("[*] Do you have an account? (y/n):".encode())
        response = connection.recv(1024).decode().strip().lower()

        if response == "y":
            while True:
                connection.send("Username: ".encode())
                username = connection.recv(1024).decode().strip()
                print(username)
                
                search = mongo_client.users.find_one({"username": username})
                print("buscando")
                if not search:
                    connection.send("[x] Username not found\n".encode())
                    continue
                break
            while True:
                connection.send("Password: ".encode())
                password = connection.recv(1024).decode().strip()

                if not crypt.verify(password, search["password"]):
                    continue
                break

            connection.send("[*] Welcome user".encode())
            return username

        elif response == "n":
            while True:
                connection.send("Enter a username: ".encode())
                username = connection.recv(1024).decode().strip()
                user_exist = mongo_client.users.find_one({"username": username})
                if user_exist:
                    connection.send("[x] Existing user".encode())
                    continue
                break

            connection.send("Enter a password: ".encode())
            password = connection.recv(1024).decode().strip()
            crypt_password = crypt.hash(password)

            mongo_client.users.insert_one({
                "username": username,
                "password": crypt_password
            })
            connection.send("[*] Welcome user".encode())
            return username

        else:
            connection.send("[x] Invalid option\n".encode())
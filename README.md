
# BACKEND FOR SECURE CHAT WITH USER AUTHENTICATION AND AI-DRIVEN MESSAGING

## DESCRIPTION

A multi-client chat system implemented with sockets using IPv4 and TCP, allowing multiple users to simultaneously connect to the server (with authentication via MongoDB), communicate in real time, and access AI features by OpenAI.
## TECHNOLOGIES USED

- socket – Interface for client-server network communication
- threading – Module for running concurrent tasks
- MongoDB - NoSQL Database
- PyMongo - Connector for MongoDB
- passlib - Secure Password Hashing
- OpenAI – AI platform

## INSTALLING

- git clone git@github.com:Jiehao530/project_socket.git
- pip install -r requirements.txt
## RUN THE PROJECT'S SOURCE CODE

- First, run python server.py in one terminal (this will be our server, which must remain running at all times). 

- Then, from another terminal or multiple terminals run python client.py (these will be the clients connecting to the server)


## AUTHOR

- [Jiehao530](https://github.com/Jiehao530)


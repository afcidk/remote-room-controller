import socket, select
import logging
from threading import Thread

class ClientThread(Thread):

    def __init__(self, ip, port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        print("[+] New thread started for {}:{}".format(ip, port))
    def run(self):
        while True:
            pass

def send_mes(x):
    if conn:
        x += '\n'
        conn.send(bytes(x.encode()))
    else:
        print("[!] Connection not established")

TCP_IP = '0.0.0.0'
TCP_PORT = 5000
BUFFER_SIZE = 1024
threads = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((TCP_IP, TCP_PORT))
print("[+] Binded to {}:{}".format(TCP_IP, TCP_PORT))
s.listen(2)
(conn, (ip, port)) = s.accept()

newthread = ClientThread(ip, port)
newthread.start()

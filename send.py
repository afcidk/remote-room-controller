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

class ConnectionThread(Thread):
    def __init__(self, soc):
        Thread.__init__(self)
        self.socket = soc
        self.connected = False
        print("[+] Connection thread started")
    def run(self):
        while True:
            (self.conn, (self.ip, self.port)) = self.socket.accept()
            self.connected = True

            newthread = ClientThread(self.ip, self.port)
            newthread.start()

    def send_mes(self, x):
        x += '\n'
        if self.connected:
            self.conn.send(bytes(x.encode()))
        else:
            self.connected = False
            print("[!] Connection not established")
            print("[!] Reconnecting")
        

def create_connection_thread():

    TCP_IP = '0.0.0.0'
    TCP_PORT = 5000
    BUFFER_SIZE = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((TCP_IP, TCP_PORT))
    print("[+] Binded to {}:{}".format(TCP_IP, TCP_PORT))
    s.listen(2)

    connection = ConnectionThread(s)
    return connection

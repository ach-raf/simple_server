#!/usr/bin/env python3

import sys
import os
import socket
from threading import Thread


def message_handler(received_message):
    match received_message.lower():
        case 'exit':
            print('Server is shutting down!')
            os._exit(1)
        case _:
            print(received_message)


def tcp_client(host, port):
    buffer_size = 1024
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(1)
    conn, address = server_socket.accept()
    if conn:
        print(f'connected at: {address}')
        msg_to_send = f'{host}:{port}'
        conn.sendall(bytes(msg_to_send, 'utf-8)'))
        data = conn.recv(buffer_size).decode()
        message_handler(data)


def server():
    # get the ip of the host from the hostname
    HOST = '0.0.0.0'
    # port number
    PORT = 7777

    tcp_server = Thread(target=tcp_client, args=(HOST, PORT))
    tcp_server.start()

    #tcp_server.join()


def main():
    counter = 0
    while counter < 1000:
        server()
        counter += 1


if __name__ == "__main__":
    # execute only if run as a script
    main()

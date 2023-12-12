import socket

if __name__ == '__main__':

    tcp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    tcp_server.bind(('127.0.0.1',3000))

    tcp_server.listen(128)

    tcp_client,tcp_client_addr = tcp_server.accept()

    recv_data = tcp_client.recv(1024)

    recv_content = recv_data.decode(encoding = 'utf-8')

    send_data = recv_content.encode(encoding = 'utf-8')

    tcp_client.send(send_data)

    tcp_client.close()

    tcp_server.close()

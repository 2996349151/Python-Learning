import socket

if __name__ == '__main__':

    tcp_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    tcp_client.connect(('127.0.0.1',5000))

    send_data = 'test_data'.encode(encoding='utf-8')

    tcp_client.send(send_data)

    recv_data = tcp_client.recv(1024)

    print(recv_data.decode(encoding='utf-8'))

    tcp_client.close()

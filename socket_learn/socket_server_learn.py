import socket
SOCKET_ADDR = "127.0.0.1"
SOCKET_PORT = 65432

_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
_sock.bind((SOCKET_ADDR, SOCKET_PORT))
_sock.listen(1)
with _sock:
    print("wait sock connection")
    conn, addr = _sock.accept()
    print("new connection {}.{} is accepted".format(conn, addr))
    with conn:
        # while True:
            print("conn wait data from socket")
            delimiter = conn.recv(1024)
            print("delimiter is {}".format(delimiter.decode("utf-8")))
            # conn.sendall(bytes("received {}".format(str(delimiter)), "utf-8"))
            conn.sendall(bytes("received", "utf-8"))
import socket,sys

job = [
    b'\x1b%-12345X@PJL INFO ID\r\n',
    b'@PJL ECHO DELIMITER25494\r\n',
]

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((sys.argv[1], 9100))
for b in job:
    soc.sendall(b)
print(soc.recv(1200).decode())
soc.close()

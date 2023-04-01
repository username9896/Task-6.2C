import socket

serversock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
localhost = socket.gethostname()

port = 6001

serversock.bind((localhost,port))

local_data = {
    'www.google.com': {'type': 'A', 'value': '192.147.32.56'},
    'www.example.com': {'type': 'CNAME', 'value': '172.132.34.21'},
    'www.facebook.com': {'type': 'A', 'value': '169.163.73.0'},
    'www.amazon.com': {'type': 'CNAME', 'value': 'www.amazon.co.uk'}
}

print('The DNS serve is listening on port ' + str(port))

while True:
    data, addr = serversock.recvfrom(2048)
    hostname = data.decode().lower()

    if hostname in local_data:
        data_type = local_data[hostname]['type']
        data_value = local_data[hostname]['value']

        server_reply = f"{hostname} and its type is {data_type} and value is {data_value}"
        serversock.sendto(server_reply.encode(), addr)
        print(f"response Sent from ({server_reply}) to {addr}")
    else:
        serversock.sendto("Enter hostname is not found".encode(), addr)
        print(f"Couldn't find the hostname that you have entered {hostname}")

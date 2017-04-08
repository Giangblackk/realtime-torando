import websocket
websocket.enableTrace(True)
ws = websocket.create_connection("ws://127.0.0.1:8888/websocket")
ws.send('Hello, Tornado')
result = ws.recv()
print(result)
ws.close()

# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# host = 'localhost'
# port = 8888
# s.connect((host , port))
# message = "GET / HTTP/1.1\r\n\r\n"
# s.sendall(message)
# chunk = s.recv(4096)
# data = []
# data.append(chunk)
# ''.join(data)

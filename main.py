# main.py
import socket

print("pyEthernetTool")

def test():
	print("server started")
	
	HOST = "127.0.0.1"
	PORT = 1234

	buf = 20

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((HOST, PORT))
	print("bind")
	s.listen(1)
	print("listening")

	conn, addr = s.accept()
	print('address: ', addr)
	while 1:
		data = conn.recv(buf)
		if not data: break
		print("data: ", data)

def main():
	print("test start")
	test()
	print("test end")
	
	input()

if __name__ == "__main__":
	main()
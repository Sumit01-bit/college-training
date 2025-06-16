import socket

try:
    # Creating UDP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Receiver socket created.")

    ip = "127.0.0.1"  # Your machine IP
    port = 8888
    s.bind((ip, port))

    print("Waiting for messages...")

    while True:
        data, addr = s.recvfrom(1024)
        print(f"Received message from {addr}: {data.decode()}")

except Exception as e:
    print("An error occurred:", e)

finally:
    s.close()

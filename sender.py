import socket

try:
    # Creating UDP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Sender socket created.")

    ip = "127.0.0.1"  # Use receiver's IP address here if running on different systems
    port = 8888
    address = (ip, port)

    while True:
        message = input("Enter message to send (or 'exit' to quit): ")
        if message.lower() == "exit":
            break
        s.sendto(message.encode(), address)
        print("Message sent.")

except Exception as e:
    print("An error occurred:", e)

finally:
    s.close()

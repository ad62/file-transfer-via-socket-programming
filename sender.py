import os,socket,time

#creating the socket object
sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((socket.gethostname(),22222))
sock.listen(5)
print("HOST: ",sock.getsockname())

#accepting the connection from the client
client,address=sock.accept()

#getting the file details to be sent
file_name=input("enter file name:")
file_size=os.path.getsize(file_name)

#sending the file details to the client
client.send(file_name.encode())
client.send(str(file_size).encode())

#opening and reading the file
with open(file_name,"rb") as file:
    c=0

    #start the time capture
    start_time=time.time()

    #running the loop until the file is sent
    while c<=file_size:
        data = file.read(1024)
        if not(data):
            break
        client.sendall(data)
        c+=len(data)

    
    #end the time capture
    end_time=time.time()

print("File transfer complete.Total time:", end_time-start_time)

#closing the socket
sock.close()
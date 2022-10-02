import socket 
import random
import json
import sys
import hashlib
import helper as h
n=60254176704887048568377189579489538851356170421806890050175939028825164407591
text="location1".encode('utf-8')
g= 3
v = h.generate_prime_number()
# c = h.generate_prime_number()
x = int(hashlib.md5(text).hexdigest()[:8], 16) % n
y= pow(g,x,n)
t = pow(g,v,n)
s = socket.socket()
s.bind(("localhost",9999))
s.listen(4)
print("Waiting for connection")
client, addr = s.accept()
while True:
    message = client.recv(1024)
    if message.decode('utf-8') == "Connected with gateway":       
        print("connected with gateway", addr)
        client.send(str(t).encode('utf-8'))
    elif message.decode('utf-8') == "You are verified":
        print(message.decode('utf-8'))        
        print("Exiting....")        
        break
    else:
        c = int(message.decode('utf-8'))
        r = (v - c * x)
        data=json.dumps({"r":r,"y":y})
        client.send(data.encode('utf-8'))
        print('G=',g,'\t(Generator)')


        # print('\n======The secret==================')
        print("x = "+ str(x))

        print('\tv=',v)

        print('\n======Shared value===============')
        print('t = g^x mod P=\t',t)
        print('r=\t\t',r)
       


   

    

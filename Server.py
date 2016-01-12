import socket
import pickle


HOST = 'localhost'
PORT = 7070

PACKET_START = 2
PACKET_LENGTH = 3
PACKET_MODEL = 4
PACKET_FLAT = 5
PACKET_DATA_START = 7
PACKET_END = -1
PACKET_CHECKSUM = -2

sumdata=[[],[],[],[],[],[],[],[]]

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((HOST,PORT))
    s.listen(1)
    while 1 :
        try:
            conn,addr=s.accept()
            while 1:
                data = conn.recv(1024)
                if data:
                    if data == 'end':
                        print('end')
                        break
                    if not (data[:2]=='\xaa\xa8' and data[-1:]=='\x28'):
                        conn.send('error start or end')
                        continue
                    if data[PACKET_MODEL:PACKET_FLAT] != '\x21':
                        conn.send('only receive 0x21 packet')
                        continue
                    Plen = ord(data[PACKET_START:PACKET_LENGTH])
                    if(len(data) != Plen +4):
                        conn.send('length not match')
                        continue
                    datalen = Plen - 5
                    if datalen % 12 != 0:
                        conn.send('error data lenght')
                        continue
                    data = data[PACKET_DATA_START:-2]
                    for i in range(datalen/12):
                        block=data[i*12:(i+1)*12+1]
                        for j in range(4):
                            first = ord(data[j*3])
                            second = ord(data[j*3+1])
                            third = ord(data[j*3+2])
                            first= ((second & 0x000f) << 8 )| first
                            third = ((second & 0x00f0) << 4 )| third
                            sumdata[j*2].append(first)
                            sumdata[j*2+1].append(second)
                    conn.send('next')
            for i in range(8):
                with open('text'+str(i), 'wb') as f:
                    pickle.dump(sumdata[i], f)
        except(socket.error):
            continue







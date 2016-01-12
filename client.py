import socket
import mmap

def read_pack( mfile , start):
    end = mfile.find('\x28',start)+1
    return mfile[start:end] , end

if __name__ == '__main__':
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(('localhost',7070))
    with open('ECG.txt','r+b') as f:
        mm=mmap.mmap(f.fileno(),0)
        packstart = 0
        while 1:
            data,packstart = read_pack(mm,packstart)
    #        print(packstart)
    #        print('%r'%data)
            if data:
                client.send(data)
            else:
                client.send('end')
                print('end')
                break
            result=client.recv(1024)
            print(result)
    client.close()











import socket, threading
class main():
    def __init__(self):
        try :
            self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.s.bind(("0.0.0.0",6969))
            self.s.listen(2)
            self.conn1, self.addr1 = self.s.accept()
            print("got connection one")
            self.conn2, self.addr2 = self.s.accept()
            print("got connection two")
        except KeyboardInterrupt:
            print("quitting from the __init__ magic method")
            exit()
    def get1(self):
        try :
            while 1 :
                try :
                    data = self.conn1.recv(1024)
                    if data != b'':
                        print(data)
                        self.forward2(data)
                except KeyboardInterrupt:
                    print("quitting from get1 while loop ")
                    exit()
        except KeyboardInterrupt :
            print("quitting from get1 function")
            exit()
    def get2(self):
        try :
            while 1:
                try :
                    data2 = self.conn2.recv(1024)
                    if data2 != b'':
                        print(data2)
                        self.forward1(data2)
                except KeyboardInterrupt:
                    print("quitting from get2 while loop")
                    exit()
        except KeyboardInterrupt :
            print("quitting from get2 funcion")
            exit()
    def forward1(self,data):
        try :
            if data != b'':
                print("connection one said to two :",data)
                self.conn1.send(data)
        except KeyboardInterrupt:
            print("quitting from forward1 function")
            exit()
    def forward2(self,data):
        try :
            if data != b'':
                print("connection two said to one :",data)
                self.conn2.send(data)
        except KeyboardInterrupt :
            print("quitting from forward2 function")
            exit()
    def clean_up(self):
        try:
            self.conn1.close()
            self.conn2.close()
            self.s.close()
        except KeyboardInterrupt:
            print("quitting from clean_up function")
            exit()
    def start(self):
        try :
            self.t1 = threading.Thread(target = self.get1)
            self.t2 = threading.Thread(target = self.get2)
            self.t1.start()
            self.t2.start()
        except KeyboardInterrupt :
            t1.join()
            t2.join()
            self.clean_up()
            exit()
if __name__ == '__main__':
    try :
        o = main()
        o.start()
    except KeyboardInterrupt :
        print("quitting from the checking class method")
        exit()

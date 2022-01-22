import threading
import time
import queue
from threading import Thread, Lock
mutex = Lock()

queue = queue.Queue(maxsize=5)

class TenedorFilosofo(threading.Thread):
    def __init__(self, tenedores, filosofosNum):
        threading.Thread.__init__(self)
        self.tenedores = tenedores
        self.filosofosNum = filosofosNum
        
   
    def iniciar(self):
        mutex.acquire()
        print("Filosofo iniciando", self.filosofosNum)
        time.sleep(2)
        print("Filosofo ", self.filosofosNum, "recoge el tenedor del lado izquierdo")
        self.tenedores[self.filosofosNum]
        time.sleep(2)
        print("Filosofo ", self.filosofosNum, "recoge tenedor del lado derecho")
        self.tenedores[self.filosofosNum]
        time.sleep(2)
    
    def terminar(self):
      
        print("Filosofo ", self.filosofosNum, "libre izquierdo")
        self.tenedores[self.filosofosNum]
        time.sleep(2)
        print("Filosofo ", self.filosofosNum, "libre derecho")
        self.tenedores[self.filosofosNum]
        time.sleep(2)
        mutex.release()

    def run(self):
        self.iniciar()
        self.terminar()

tenedorArray = [1,1,1,1,1]

for i in range(0,5):
    tenedorArray[i] = threading.BoundedSemaphore(1)

for i in range(0,5):
    total = TenedorFilosofo(tenedorArray, i)
    total.start()

from logging import captureWarnings


class NodePelanggan:
    def __init__(self, namaPelanggan):
        self._namaPelanggan = namaPelanggan
    def getNamaPelanggan(self):
        return self._namaPelanggan

class WarungMakan:
    DEFAULT_CAPACITY = 5
    def __init__(self): #tidak boleh mengganti / menambah metode init
        self._data = [None] * WarungMakan.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0
    
    def dequeue(self): #menghapus data paling depan, dan memajukan urutan data yang dibelangkangnya
        if self.is_empty():
            print('Empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        print('\n### Pelanggan',answer.getNamaPelanggan(),'Selesai Membayar ###')
        listBaru = [None] * len(self._data)
        counterListBaru = 0
        for i in range(len(self._data)):
            if self._data[i] != None:
                listBaru[counterListBaru] = self._data[i]
                counterListBaru += 1 
        self._data = listBaru
        self._front = 0
        pass
    
    def enqueue(self, namaPelanggan): #menambah data ke list
        pelangganMasuk = NodePelanggan(namaPelanggan)
        if self._size == len(self._data):
            self.resizeBy3(2*len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = pelangganMasuk
        self._size +=1
        pass
    
    def resizeBy3(self,cap): #menambah ukuran queue sebesar 3
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0
        print('\n### Melakukan Resize 3 ###')
        pass
    
    def printAll(self):
        print("\n=== WarungMakan ===")
        for i in range(len(self._data)):
            if self._data[i] != None:
                print(i+1,end=". ")
                print(self._data[i].getNamaPelanggan())
            else:
                print(i+1,end=". ")
                print("Kosong")
                
# test case program
wm = WarungMakan()
wm.enqueue("Pelanggan A")
wm.enqueue("Pelanggan B")
wm.enqueue("Pelanggan C")
wm.enqueue("Pelanggan D")
wm.enqueue("Pelanggan E")
wm.printAll()
wm.enqueue("Pelanggan F")
wm.enqueue("Pelanggan G")
wm.printAll()
wm.dequeue()
wm.dequeue()
wm.dequeue()
wm.printAll()
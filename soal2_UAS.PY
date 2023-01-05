class Node:
    def __init__(self,data,priority) -> None:
        self._data = data
        self._priority = priority
        self._next = None
        self._prev = None

class PQSTugas:
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0
    
    def isEmpty(self) -> bool:
        #isi kode anda
        return self._size == 0
        pass
    
    def printAll(self) -> None:
        for i in range(len(self._data)):
            if self._data[i] != None:
                print(i+1,end=". ")
                print(self._data[i])
            else:
                print(i+1,end=". ")
        #isi kode anda
        pass
    
    def _addHead(self, newNode) -> None:
        #isi kode anda
        pass
    
    def _addTail(self, newNode) -> None:
        #isi kode anda
        pass
    
    def _addMiddle(self, newNode) -> None:
        #isi kode anda
        pass
    
    def add(self, data, priority) -> None:
        data = [int(priority), data]
        self._data.append(data)
        self._data.sort()
        self.size += 1
        #isi kode anda
        pass
 
    def remove(self) -> None:
        del self._data[0]
        self._size -= 1
        #isi kode anda
        pass

    def removePriority(self, priority) -> None:
        lst2 = []
        for x in range(len(self._data)):
            if self._data[x][0] == priority:
                del self._data[x][1]
        for y in range(len(self._data)):
            if len(self._data[y]) == 1:
                pass
            else:
                lst2.append(self._data[y])
        self._data = lst2
        self._size -= 1
        #isi kode anda
        pass
    
if __name__ == "__main__":
 tugasKu = PQSTugas()
 tugasKu.add("StrukDat",1)
 tugasKu.add("Menyapu", 4)
 tugasKu.add("Cuci Baju", 3)
 tugasKu.add("Beli Alat Tulis", 2)
 tugasKu.add("Cuci Sepatu", 3)
 tugasKu.printAll()
 tugasKu.remove()
 tugasKu.printAll()
 tugasKu.removePriority(2)
 tugasKu.removePriority(4)
 tugasKu.printtAll()
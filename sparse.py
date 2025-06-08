class sparse:
    def __init__(self,nn,mm,k,x):
        self.nn = nn
        self.mm = mm        
        self.data = []
        self.k = k
        self.size = int(nn[k - 1] * mm[k])
        for i in range(self.size):
            self.data.append(x)
        self.head = 0
    def insert(self,newkey):
        low = self.head
        high = (self.size + self.head - 1) 
        while low <= high:
            m = (low + high) >> 1
            if self.data[m % self.size] < newkey:
                low = m + 1
            elif self.data[m % self.size] > newkey:
                high = m - 1
            else:
                print("Key already exists:", newkey)
                return
        print("initial position for insertion:", m)
        if self.data[m % self.size] < newkey and ( m + 1) % self.size != self.head:
            m += 1
        
        if self.isDummy(m):
            self.data[m % self.size] = newkey
        else:
            c = 0
            while not self.isDummy(m + c + 1):
                c += 1
            while c > 0:
                self.data[(m + c + 1) % self.size] = self.data[(m + c) % self.size]
                c -= 1
            self.data[(m) % self.size] = newkey
            if (self.head >= m % self.size) and (self.head < (m + c + 1) % self.size):
                self.head = (self.head + 1) % self.size

    def isDummy(self,pos):
        # η τελευταια θεση δεν ειναι ποτε dummy
        if pos % self.size  == self.head - 1:
            return False
        # αν η θεση ειναι dummy, το στοιχειο στην θεση αυτη ειναι το ιδιο με το επομενο
        return  self.data[pos % self.size] == self.data[(pos + 1) % self.size]

    def delete(self,oldkey):
        print("Deleting key:", oldkey)

    def binarySearch(self,key):
        low = self.head
        high = (self.size + self.head - 1) 
        while low <= high:
            mid = (low + high) >> 1
            if self.data[mid % self.size] < key:
                low = mid + 1
            elif self.data[mid % self.size] > key:
                high = mid - 1
            else:
                while mid < self.head + self.size and self.data[mid % self.size] == self.data[(mid + 1) % self.size]:
                    mid += 1
                return mid % self.size
        return -1
    def print_data(self):
        row = "["
        for i in range(self.size):
            if i == self.head:
                row += f" >{self.data[i]}<"
            else:
                row += f" {self.data[i]}"
            if i < self.size - 1:
                row += ","
        row += " ]"
        print(row)
    
    def expand(self):
        print("Expanding data structure")
       
    def shrink(self):
        print("Shrinking data structure")
class sparse:
    def __init__(self,nn,mm,k,x):
        self.nn = nn
        self.mm = mm        
        self.data = []
        self.k = k
        self.n = 1
        self.size = int(nn[k - 1] * mm[k])
        for i in range(self.size):
            self.data.append(x)
        self.head = 0
        
    def insert(self,newkey):
        if (self.n == self.nn[self.k]):
            self.expand()
            
        low = self.head
        high = (self.size + self.head - 1) 
        m = int((low + high) / 2) 
        while low <= high:
            
            m = int((low + high) / 2) 

            if self.data[m % self.size] < newkey:
                low = m + 1
            elif self.data[m % self.size] > newkey:
                high = m - 1
            else:
                return

        if self.data[m % self.size] < newkey:
            m = (m + 1) % self.size
        if self.isDummy(m):
            self.data[m % self.size] = newkey
            if (m % self.size) == self.head:
                self.head = (self.head + 1) % self.size
            self.n += 1
        else:
            c = 0
            while not self.isDummy(m + c +1):
                c += 1
            changeHead = True
            if(m+c+1) % self.size == self.head:
                self.head = (self.head + 1) % self.size
                changeHead
            
            while c >= 0:
                
                self.data[(m + c + 1) % self.size] = self.data[(m + c) % self.size]
                if (  (m+c) % self.size == self.head ) and changeHead:
                    self.head = (self.head + 1) % self.size
                    changeHead = False
                c -= 1
            self.data[(m) % self.size] = newkey
            self.n += 1


    def expand(self):
        self.k += 1
        newm  = int(self.nn[self.k -1] * self.mm[self.k-1])
        newdata = []
        q = int(newm/self.n)
        r = newm % self.nn[self.k-1]
        for i in range(self.size):
            if int(i*r/self.k) < int((i+1)*r/self.k):
                for j in range(q + 1):
                    newdata.append(self.data[(self.head+i) % self.size])
            else:
                for j in range(q):
                    newdata.append(self.data[(self.head +i) % self.size])
        self.data = newdata
        self.size = newm
        self.head = 0
        
    def delete(self,oldkey):
        print("Deleting key:", oldkey)   

    def shrink(self):
        print("Shrinking data structure")

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

    def isDummy(self,pos):
        # η τελευταια θεση δεν ειναι ποτε dummy
        if ( pos +1 ) % self.size  == self.head :
            return False
        # αν η θεση ειναι dummy, το στοιχειο στην θεση αυτη ειναι το ιδιο με το επομενο
        return  self.data[pos % self.size] == self.data[(pos + 1) % self.size]    
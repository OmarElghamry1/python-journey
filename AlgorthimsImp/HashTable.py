class Hashtable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
        if not found:
            self.arr[h].append((key, val))

    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                print("del", idx)
                del self.arr[h][idx]


if __name__ == "__main__":
    t = Hashtable()
    t["march 6"] = 310  # with hash 9
    # t["march 7"] = 420
    # t["march 8"] = 67
    # t["march 17"] = 63457 # with hash 9
    t["march 17"] = 421
    t["march 17"] = "***"
    t["march 16"] = 1  # with hash 9
    # t["march 6"] = 2
    t["march 26"] = 3  # with hash 9
    # t["march 35"] = 4  # with hash 9
    # t["march 44"] = 5  # with hash 9
    del t["march 26"]
    # t["march 26"] = 1000

    print(t.arr)
    print(t["march 16"])

#  for i in range(1, 40):
#     print("march:", i, "from",t.get_hash(f'march {i}'))

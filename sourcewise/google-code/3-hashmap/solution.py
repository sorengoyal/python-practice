'''Implementing a hash map using arrays'''

class MyHashmap:
    def __init__(self):
        self.table = [[]]*10
    def hash(self, key):

        return index

    def insert(self, key, value):
        self.insert_helper(key, value, self.table, 1)

    def insert_helper(self, key, value, table, level):
        index = self.hash(key+str(level))
        if len(table[index]) == 0:
            table[index] = [(key, value)]
        elif len(table[index]) == 1:
            [(key2, value2)] = table[index]
            table[index] = [[]]*128
            index2 = self.hash(key2 + str(level+1))
            table[index][index2] = [(key2, value2)]
            self.insert_helper(key, value, table[index], level+1)
        else:
            self.insert_helper(key, value, table[index], level+1)

    def get(self, key):
        return self.get_helper(key, self.table, 1)

    def get_helper(self, key, table, level):
        index = self.hash(key + str(level))
        if len(table[index]) == 0:
            raise Exception('Not Found')
        elif len(table[index]) == 1:
            return table[index][0][1]
        else:
            self.get_helper(key, table[index], level+1)
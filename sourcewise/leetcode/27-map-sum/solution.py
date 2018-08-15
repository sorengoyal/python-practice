class MapSum(object):
    def __init__(self):
        self.root = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.insert_helper(key, val, self.root)

    def insert_helper(self, key, val, node):
        if key == '':
            node["val"] = val
            return
        if key[0] not in node:
            node[key[0]] = {}
        self.insert_helper(key[1:], val, node[key[0]])

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        node = self.root
        while prefix != '':
            if prefix[0] not in node:
                return 0
            node = node[prefix[0]]
            prefix = prefix[1:]
        return self.sum_helper(node)

    def sum_helper(self, node):
        sum = 0
        for key in node:
            if key == "val":
                sum += node["val"]
            else:
                sum += self.sum_helper(node[key])
        return sum

    def print_tree(self, node):
        for key in node:
            if key == 'val':
                print node[key],
            else:
                print '(' + key + ', ',
                self.print_tree(node[key])
        print ')',

if __name__ == '__main__':
    obj = MapSum()
    obj.insert("apple", 3)
    obj.insert("app", 2)
    obj.insert("ball", 10)
    obj.print_tree(obj.root)
    print obj.sum("a")

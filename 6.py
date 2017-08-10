import sys

class child(object):
    def __init__(self, name, x, y, z):
        self.name = name
        self.x = x;
        self.y = y;
        self.z = z;

    def __lt__(self, other):
        return int(self.x) * int(self.y) * int(self.z) <= int(other.x) * int(other.y) * int(other.z)

while True:
    n = int(input())
    childs = []
    if n == -1:
        break
    for i in range(n):
        x, y, z, name = list(input().split())
        childs.append(child(name,x,y,z))

    print(sorted(childs)[n-1].name + " took clay from " + sorted(childs)[0].name + ".")
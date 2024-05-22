# TODO: Complete a classe Retangulo
class Retangulo:
    def __init__(self):
        self.__x1: int
        self.__y1: int
        self.__x2: int
        self.__y2: int

    @property
    def x1(self):
        return self.__x1
    
    @x1.setter
    def x1(self, valor):
        self.__x1 = valor

    @property
    def x2(self):
        return self.__x2

    @x2.setter
    def x2(self, valor):
        self.__x2 = valor
        
    @property
    def y1(self):
        return self.__y1

    @y1.setter
    def y1(self, valor):
        self.__y1 = valor
        

    @property
    def y2(self):
        return self.__y2
    
    @y2.setter
    def y2(self, valor):
        self.__y2 = valor

    def area(self):
        return abs((self.__x2 - self.__x1) * (self.__y2 - self.__y1))

if __name__ == "__main__":

    retangulo = Retangulo()

    n = int(input())

    for i in range(n):
        linha = input().split()

        if linha[0] == "R":
            x1, y1, x2, y2 = map(int, linha[1:])
            retangulo.x1 = x1
            retangulo.y1 = y1
            retangulo.x2 = x2
            retangulo.y2 = y2
        else:
            print(retangulo.area())

from abc import ABC, abstractmethod 
import math

class FiguraGeometrica(ABC):
    def __init__(self):
        self.nome = None

    def setNome(self, nomeFigura):
        self.nome = nomeFigura

    def getNome(self):
        return self.nome

    @abstractmethod
    def setArea(self):
        pass 

    @abstractmethod 
    def setPerimetro(self):
        pass 


class Circulo(FiguraGeometrica):
    def __init__(self):
        super().__init__()
        self.raio = None 

    def setPerimetro(self):
        return (2 * math.pi) * self.raio

    def setArea(self):
        return math.pi * (self.raio ** 2)

    def setRaio(self, raioCirculo):
        self.raio = raioCirculo

class Retangulo(FiguraGeometrica):
    def __init__(self):
        super().__init__()
        self.altura = None 
        self.largura = None 

    def setAltura(self, alturaRetangulo):
        self.altura = alturaRetangulo

    def setLargura(self, larguraRetangulo):
        self.largura = larguraRetangulo

    def setArea(self):
        return self.largura * self.altura

    def setPerimetro(self):
        return 2 * (self.largura + self.altura)

class Triangulo(FiguraGeometrica):
    def __init__(self):
        super().__init__()
        self.ladoUm = None 
        self.ladoDois = None 
        self.ladoTres = None 
        self.perimetro = None
        self.semiPerimetro = None
        self.area = None

    def setLadosTriangulo(self, lado1, lado2, lado3):
        self.ladoUm = lado1
        self.ladoDois = lado2
        self.ladoTres = lado3
        self.setPerimetro()
        self.setSemiPerimetro()
        self.setArea()

    def setPerimetro(self):
        self.perimetro = self.ladoUm + self.ladoDois + self.ladoTres
        return self.perimetro

    def setSemiPerimetro(self):
        self.semiPerimetro = self.perimetro / 2
        return self.semiPerimetro

    def setArea(self):
        s = self.semiPerimetro
        a = self.ladoUm
        b = self.ladoDois
        c = self.ladoTres
        self.area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return self.area

circulo = Circulo()
circulo.setNome("Circulo")
circulo.setRaio(2)

retangulo = Retangulo()
retangulo.setNome("Retangulo")
retangulo.setAltura(30)
retangulo.setLargura(5)

figuras = []
figuras.append(circulo)
figuras.append(retangulo)

print(figuras)

for figura in figuras:
    print(f"Nome: {figura.getNome()}")  
    print(f"Area: {figura.setArea()}")
    print(f"Perimetro: {figura.setPerimetro()}")
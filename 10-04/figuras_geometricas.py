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

    def setLadosTriangulo(self, lado1, lado2, lado3):
        self.ladoUm = lado1
        self.ladoDois = lado2
        self.ladoTres = lado3

    def setArea(self):
        pass 

    def setPerimetro(self):
        

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

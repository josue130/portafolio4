class rectangulo:
     def __init__(self,base,altura):
          self.base=base
          self.altura=altura
     def calcularArea(self):
          return self.base*self.altura
     def calcularPerimetro(self):
          baseT=self.base*2
          alturaT=self.altura*2
          return baseT + alturaT
     def motrarA(self):
          print("Esta es la altura de su rectangulo",self.altura)
          print("Esta es la base de su rectangulo",self.base)

class crarFactura:
     def __init__(self,numFact,fecha,cliente):
          self.numFact=numFact
          self.facha=fecha
          self.cliente=cliente
          lista=[]
          self.lista=lista
          total=0
          self.total=total
          despuesIm=0
          self.despuesIm=despuesIm

     def agregarItem(self,nomProd,precioUnitario,cantidad):
          self.nomProd=nomProd
          self.precioUnitario=precioUnitario
          self.cantidad=cantidad
          temP=[]
          temP+=[self.precioUnitario,self.cantidad]
          self.lista+=[temP]
     def verTotal(self):
          if self.lista==[]:
               print("Tiene que agregar items al carrito")
          for i in self.lista:
               print(i)
               indice1=i[0]
               indice2=i[1]
               res=indice1*indice2
               self.total+=res
          self.lista=[]
          impuesto=0
          impuesto=self.total*0.13
          self.despuesIm+=self.total+impuesto
          print("Antes del impuesto",self.total,"Impuesto~~> 13%","Despues del impuesto",self.despuesIm)
     def cerrarFacturar(self):
          if self.despuesIm==0:
               print("Tiene que ingresar a ver total")
          print("Total a pagar~~~>",self.despuesIm)

(class) forma :
    def desenhar(self):
         print("desenhando forma")
 class circulo(forma):
    def desenhar(self):
    print("desenhando circulo")

 class quadrado(forma): 
    def desenhar (self):
    print("desenhando quadrado")

formas = [circulo(), quadrado()]
for forma in formas:
        forma.desenha()
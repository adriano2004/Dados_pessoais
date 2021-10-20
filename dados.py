class info :
    def __init__(self,d1,d2,d3):
        self.nome = d1
        self.sobrenome = d2
        self.idade = d3

    def mostra(self):
        print("{} {} tem {} anos".format(self.nome, self.sobrenome , self.idade))

n = input('Digite seu nome: ')
n2 = input('Digite seu sobrenome: ')
d = input('Digite sua idade: ')

x = info(n,n2,d)
x.mostra()
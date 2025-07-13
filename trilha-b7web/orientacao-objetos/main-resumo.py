# class Pessoa:
#     def __init__(self, name):
#         self.name = name
        
#     def saudar(self):
#         print(f"Opa, eu sou {self.name}")


# p1 = Pessoa("José Marques")
# p2 = Pessoa("Joao Pedro")

# p1.saudar()
#####################################################
# class Conta:
#     def __init__(self):
#         self._saldo = 0
        
#     @property
#     def saldo(self):
#         return self._saldo
    
#     def depositar(self, valor):
#         self._saldo += float(valor)
        
#     def sacar(self, valor):
#         if self._saldo >= valor:
#             self._saldo -= valor
#             return True
#         else:
#             return False
        
# c1 = Conta()
# c1.depositar(200)
# c1.depositar(500)
# c1.sacar(300)
# print(c1.saldo)

# class Modificador:
#     @staticmethod
#     def maiuscula(valor):
#         return valor.upper()
    
# class Produto:
#     def __init__(self, nome, preco):
#         self.nome = nome
#         self._preco = float(preco)
    
#     @property
#     def preco(self):
#         return self._preco    
   
#     @preco.setter
#     def preco(self, novo_preco):
#         if novo_preco > 0:
#             self._preco = float(novo_preco)
            
# nome_do_produto = Modificador.maiuscula("Mouse XYZ")
            
# p1 = Produto(nome_do_produto, 100)
# p1.preco = 10
# print(f"{p1.nome} - R$ {p1.preco}")

###################################################



# class Usuario:
#     usuarios = []
    
#     def __init__(self, nome):
#         self.nome = nome 
#         Usuario.usuarios.append(self)
        
#     def dar_oi(self):
#         print(f"Oi, eu sou {self.nome}")
        
#     @classmethod
#     def total_usuarios(cls):
#         return len(cls.usuarios)
    
# usuario1 = Usuario("Jose Marques")
# usuario2 = Usuario("Magda")
# usuario3 = Usuario("Murilo")
# usuario4 = Usuario("Ana")
# # usuario1.dar_oi()
# print(Usuario.total_usuarios())

##################################

## Herança X Composição

# class Animal:
#     def fazer_som(self):
#         print("Algum som")
        
# class Cachorro(Animal):
#     pass

# ## Herança = Todo cachorro é um animal
# dog = Cachorro()
# dog.fazer_som()


# Composição 

# class Motor:
#     def ligar(self):
#         print("Ligando o motor...")
        
# class Carro:
#     def __init__(self):
#         self.motor = Motor()
        
#     def ligar(self):
#         self.motor.ligar()

# #### Herança = Todo carro é um motor (isso seria se fosse herança) = Acoplado
# #### Composição = Todo carro tem um motor = Desacoplado

# fiat = Carro()
# fiat.ligar()

############### Polimorfismo e sobrescrita de métodos

# class Pagamento:
#     def pagar(self, valor):
#         print(f"Pagando R$ {valor}")
        
# class PagamentoPromessa(Pagamento):
#     pass

# class PagamentoCartao(Pagamento):
#     def pagar(self, valor):
#         print(f"Pagando no cartão R$ {valor}")
        
# class PagamentoPix(Pagamento):
#     def pagar(self, valor):
#         print(f"Pagando no pix R$ {valor}")
        
# def realizar_pagamento(meio: Pagamento, valor):
#     meio.pagar(valor)
    
# promessa = PagamentoPromessa()
# cartao = PagamentoCartao()
# pix = PagamentoPix()

# realizar_pagamento(cartao, 100)

#### Classes abstratas e interfaces com ABC
# from abc import ABC, abstractmethod

# # ABC = Abstract Base Class
# class Pagamento(ABC):
#     @abstractmethod
#     def pagar(self, valor):
#         pass
        
# class PagamentoPromessa(Pagamento):
#     def pagar(self, valor):
#         print(f"Pagando na promessa R$ {valor}")

# class PagamentoCartao(Pagamento):
#     def pagar(self, valor):
#         print(f"Pagando no cartão R$ {valor}")
        
# class PagamentoPix(Pagamento):
#     def pagar(self, valor):
#         print(f"Pagando no pix R$ {valor}")
        
# def realizar_pagamento(meio: Pagamento, valor):
#     meio.pagar(valor)
    
# promessa = PagamentoPromessa()
# cartao = PagamentoCartao()
# pix = PagamentoPix()

# realizar_pagamento(cartao, 100)

### Princípio da responsabilidade única (S. O. L. I. D.)
# Princípio 1 - SRP = Single Responsability Principle

### Exemplo de classe que viola o SRP = Faz coisas diferentes, responsibilidades diferentes, para corrigir deve-se criar 3 classes
# class RelatorioFinanceiro:
#     #Processamento das informações
#     def calcular_dados(self, dados):
#         pass
    
#     #I/O, gerenciamento de arquivos
#     def salvar_arquivo(self):
#         pass
    
#     #Enviar e-mail
#     def enviar_email(self, email):
#         pass

# class RelatorioFinanceiro:
#     #Processamento das informações
#     def calcular_dados(self, dados):
#         pass
    
# class RelatorioArquivo:
#     def salvar_relatorio(self, relatorio: RelatorioFinanceiro):
#         pass

# class RelatorioEnvio:
#     def enviar_email(self, relatorio: RelatorioFinanceiro):
#         pass


# relatorio = RelatorioFinanceiro()
# relatorio_arquivo = RelatorioArquivo()
# relatorio_envio = RelatorioEnvio()
# relatorio_pronto = relatorio.calcular_dados("abc")
# relatorio_arquivo.salvar_relatorio(relatorio_pronto)
# relatorio_envio.enviar_email(relatorio_pronto)

#### OCP = Open/Closed Principle




        

    






    
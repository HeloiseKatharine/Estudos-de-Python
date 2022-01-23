from abc import ABC, abstractmethod

class Livro():
  @abstractmethod #para mostrar que a classe é abstrata
  def __init__(self, titulo= '', autor = ''):
    self.titulo = titulo
    self.autor = autor
  
class A(Livro):
  def __init__(self, titulo):
    self.titulo = titulo


teste = A('kf')
print(vars(teste))
class A:
  def imprime_a(self):
    print('a')

class B:
  def imprime_b(self):
    print('b')

class C(A, B):
  def imprime_c(self):
    print('c')

# como hereda de A y de B , C puede usar sus métodos
c = C()
c.imprime_a()
c.imprime_b()
c.imprime_c()

import unittest
from soma import soma

class TestClass(unittest.TestCase):

    def testa_correta(self):
        somaCerta = soma(10,20)
        self.assertEqual(somaCerta,30)

    def testa_errado(self):
        somaErrada = soma('abc',25)
        self.assertEqual(somaErrada,0)

if __name__ == '__main__':
    unittest.main()
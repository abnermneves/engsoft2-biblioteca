import unittest
from biblioteca import Livro, Biblioteca

class TestLivro(unittest.TestCase):
    def setUp(self):
        self.livro = Livro('O Deserto dos Tártaros', 'Dino Buzzati')

    def test_emprestar(self):
        self.assertTrue(self.livro.disponivel)
        self.livro.emprestar()
        self.assertFalse(self.livro.disponivel)

    def test_devolver(self):
        self.livro.emprestar()
        self.assertFalse(self.livro.disponivel)
        self.livro.devolver()
        self.assertTrue(self.livro.disponivel)

class TestBiblioteca(unittest.TestCase):
    def setUp(self):
        self.biblioteca = Biblioteca()
        self.livro = Livro('O Deserto dos Tártaros', 'Dino Buzzati')

    def test_adicionar_livro(self):
        self.assertEqual(len(self.biblioteca.livros), 0)
        self.biblioteca.adicionar_livro(self.livro)
        self.assertEqual(len(self.biblioteca.livros), 1)

    def test_listar_livros(self):
        self.biblioteca.adicionar_livro(self.livro)
        self.assertEqual(len(self.biblioteca.livros), 1)

if __name__ == '__main__':
    unittest.main()

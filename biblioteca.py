class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"Você emprestou o livro '{self.titulo}' de {self.autor}.")
        else:
            print(f"Desculpe, o livro '{self.titulo}' não está disponível para empréstimo.")

    def devolver(self):
        self.disponivel = True
        print(f"Você devolveu o livro '{self.titulo}' de {self.autor}.")

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f"O livro '{livro.titulo}' foi adicionado à biblioteca.")

    def listar_livros(self):
        print("Livros disponíveis na biblioteca:")
        for livro in self.livros:
            print(f"- {livro.titulo} ({livro.autor})")

if __name__ == "__main__":
    biblioteca = Biblioteca()

    demian = Livro("Demian", "Hermann Hesse")
    mrs_dalloway = Livro("Mrs. Dalloway", "Virginia Woolf")

    biblioteca.adicionar_livro(demian)
    biblioteca.adicionar_livro(mrs_dalloway)

    demian.emprestar()
    mrs_dalloway.emprestar()

    biblioteca.listar_livros()

    demian.devolver()
    mrs_dalloway.devolver()

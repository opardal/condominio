class Pessoa():

    def __init__(self, nome):
        self.nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

class Proprietario(Pessoa):

    def __init__(self, economia):
        self.economia = economia

class Funcionario(Pessoa):

    def __init__(self):
        pass
    

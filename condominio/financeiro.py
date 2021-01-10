
class Boleto:

    def __init__(self, economia):
        self.economia = economia
        self.boleto = {}

    def __str__(self):
        cabecalho = f"Boleto gerado para o apartamento {self.economia}\n\n"
        conteudo = ""
        for key, value in self.boleto.items():
            conteudo += f"{key}{(100-len(key+str(value)))*'.'}{value}\n"
        return cabecalho + conteudo


class FonteDoRecurso:
    """
    Colocar Conta Corrente, Fundo de Reserva, Fundo de Obras, Coletividade e cada um dos apartamentos

    Na logica, quando selecionado a Coletividade, será necessário buscar um critério de divisão.e

    Ao registrar cada novo apartamento, garantir que seja incluido no bd como uma nova fonte de recurso.
    
    """
    pass


class Despesa:

    def __init__(self, titulo: str):
        self.titulo = titulo
    
    @property
    def titulo(self):
        return self._titulo
    
    @property
    def valor(self):
        return self._valor
    
    @property
    def fonte_do_recurso(self):
        return self._fonte_do_recurso
    
    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo
    
    @valor.setter
    def valor(self, valor):
        self._valor = valor

    @fonte_do_recurso.setter
    def fonte_do_recurso(self, fonte):
        self._fonte_do_recurso = fonte
    
    def boletar(self, boleto: Boleto):
        boleto.boleto[self.titulo] = self.valor
        print('Boletado.')


class produto:
    #Atributos
    nome:str
    preco:float
    saldo:int
    #Metodos
    def valor_total_estoque(self) -> float:
        return self.preco * self.saldo
    def adicionar_produtos(self, quantidade) -> int:
        self.saldo = self.saldo + quantidade 
        return self.saldo
    def remover_produtos(self, quantidade ) -> int:
        self.saldo = self.saldo - quantidade 
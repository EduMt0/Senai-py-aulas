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
    def dados_produto(self) -> str:
        saida = f'''
            dados do produto:
            \tNome do Produto: {self.nome}
            \tValor da compra do produto: R$ {self.preco}
            \tQuantidade em estoque: {self.saldo}
            \tValor total em estoque: {self.valor_total_estoque():.2f}
        '''
        return saida
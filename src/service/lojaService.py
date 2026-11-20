from data.Vendas import vendas
import pandas as pd



class Loja:
    def __init__(self, dados_vendas = vendas):
        
        self.__vendas_DF = pd.DataFrame(dados_vendas)
        self.__vendas_DF["faturamento"] = self.__vendas_DF["quantidade"] * self.__vendas_DF["preco"] 
        self.__vendas_DF["porcentagem"] = round(self.__vendas_DF['faturamento'] / self.__vendas_DF['faturamento'].sum() * 100,2)
    
    def faturamentoTotal(self) -> str:
        return (f"R$ {sum(self.__vendas_DF["faturamento"])}")
    
    def faturamentoIndividual(self):
        return self.__vendas_DF[["produto","faturamento","porcentagem"]]
    
    def produtosVendidos(self):
        return self.__vendas_DF['quantidade']
    
    def totalVendidos(self):
        return self.__vendas_DF['quantidade'].sum()
        
    def maisVendido(self):
        return self.__vendas_DF.sort_values(["quantidade"],ascending=False).head(1)
    
    def filtroQtdVenda(self, qtd: int):
        return self.__vendas_DF[self.__vendas_DF['quantidade'] > qtd]
    
    def maiorfaturamentoProd(self):
        return self.__vendas_DF.sort_values('faturamento', ascending=False).head(1)
    
    def maiorfaturamentoCatg(self):
        return self.__vendas_DF[['categoria','faturamento','porcentagem']].groupby('categoria').sum().sort_values('faturamento', ascending=False).head(1)
    
    def participacaoFaturamentoCatg(self):
        return self.__vendas_DF[['categoria','faturamento','porcentagem']].groupby('categoria').sum()
        
    def relatorio(self):
        print("="*5 + " RELATÓRIO DE VENDAS "+"="*5 )
        
        print(f"\nFaturamento total: {self.faturamentoTotal()}")
        print(f"Quantidade de itens vendidos: {self.totalVendidos()}")
        
        print(f"\nProduto mais vendido: \n{self.maisVendido()} \n")
        print(f"Maior faturamento por produto: \n{self.maiorfaturamentoProd()}\n")
        ''
        
        print("="*5 + " CATEGORIAS "+"="*5 )
        
        print(self.participacaoFaturamentoCatg())


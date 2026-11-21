from data.Vendas import vendas
import pandas as pd
import matplotlib.pyplot as plt



class Loja:
    def __init__(self, dados_vendas = vendas):
        
        self._vendas_DF = pd.DataFrame(dados_vendas)
        self._vendas_DF["faturamento"] = self._vendas_DF["quantidade"] * self._vendas_DF["preco"] 
        self._vendas_DF["porcentagem"] = round(self._vendas_DF['faturamento'] / self._vendas_DF['faturamento'].sum() * 100,2)
    
    def faturamentoTotal(self) -> str:
        return (f"R$ {sum(self._vendas_DF["faturamento"])}")
    
    def faturamentoIndividual(self):
        return self._vendas_DF[["produto","faturamento","porcentagem"]]
    
    def produtosVendidos(self):
        return self._vendas_DF['quantidade']
    
    def totalVendidos(self):
        return self._vendas_DF['quantidade'].sum()
        
    def maisVendido(self):
        return self._vendas_DF.sort_values(["quantidade"],ascending=False).head(1)
    
    def filtroQtdVenda(self, qtd: int):
        return self._vendas_DF[self._vendas_DF['quantidade'] > qtd]
    
    def maiorfaturamentoProd(self):
        return self._vendas_DF.sort_values('faturamento', ascending=False).head(1)
    
    def maiorfaturamentoCatg(self):
        return self._vendas_DF[['categoria','faturamento','porcentagem']].groupby('categoria').sum().sort_values('faturamento', ascending=False).head(1)
    
    def participacaoFaturamentoCatg(self):
        return self._vendas_DF[['categoria','faturamento','porcentagem']].groupby('categoria').sum()
        
    def relatorio(self):
        print("="*5 + " RELATÓRIO DE VENDAS "+"="*5 )
        
        print(f"\nFaturamento total: {self.faturamentoTotal()}")
        print(f"Quantidade de itens vendidos: {self.totalVendidos()}")
        
        print(f"\nProduto mais vendido: \n{self.maisVendido()} \n")
        print(f"Maior faturamento por produto: \n{self.maiorfaturamentoProd()}\n")
        ''
        
        print("="*5 + " CATEGORIAS "+"="*5 )
        
        print(self.participacaoFaturamentoCatg())


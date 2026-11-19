from data.Vendas import vendas
import pandas as pd



class Loja:
    def __init__(self, dados_vendas = vendas):
        
        self._vendas_DF = pd.DataFrame(dados_vendas)

        
        self._vendas_DF["faturamento"] = self._vendas_DF["quantidade"] * self._vendas_DF["preco"] 
    
    
    def faturamentoTotal(self) -> int:
        return sum(self._vendas_DF["faturamento"])
    
    def faturamentoIndividual(self):
        return self._vendas_DF[["produto","faturamento"]]
    
    def produtosVendidos(self):
        return self._vendas_DF['quantidade']
    
    def totalVendidos(self):
        return self._vendas_DF['quantidade'].sum()
        
    def maisVendido(self):
        return self._vendas_DF.sort_values(["quantidade"],ascending=False).head(1)
    
    def maiorfaturamento(self):
        return self._vendas_DF.sort_values('faturamento', ascending=False).head(1)
    
    def participacaoFaturamentoCatg(self):
        categoria_df = self._vendas_DF#.groupby('categoria')['faturamento'].sum()
        
        categoria_df["porcentagem"] = round(categoria_df['faturamento'] / categoria_df['faturamento'].sum() * 100,2)

        return categoria_df[['categoria','faturamento','porcentagem']].groupby('categoria').sum()
        
    def relatorio(self):
        print("="*5 + " RELATÓRIO DE VENDAS "+"="*5 )
        
        print(f"\nFaturamento total: R$ {self.faturamentoTotal()}")
        print(f"Quantidade de itens vendidos: {self.totalVendidos()}")
        
        print(f"\nProduto mais vendido: \n{self.maisVendido()} \n")
        print(f"Maior faturamento por produto: \n{self.maiorfaturamento()}\n")
        ''
        
        print("="*5 + " CATEGORIAS "+"="*5 )
        
        print(self.participacaoFaturamentoCatg())


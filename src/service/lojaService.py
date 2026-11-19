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
        
    def maisVendido(self):
        return self._vendas_DF.sort_values(["quantidade"],ascending=False).head(1)
    
    

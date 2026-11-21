import matplotlib.pyplot as plt
from service.lojaService import Loja

class LojaCharts:
    def __init__(self, loja: Loja):
        self.loja = loja
        
        self._vendas = loja._vendas_DF
        
    def faturamentoCatg(self):
        plt.bar(self._vendas['categoria'],self._vendas['faturamento'])
        plt.title("Faturamento por categoria")
        plt.xlabel("Categoria")
        plt.ylabel("Faturamento")
        
        plt.show()

    def faturamentoProd(self):
        plt.bar(self._vendas['produto'],self._vendas['faturamento'])
        plt.title("Faturamento por produto")
        plt.xlabel("produto")
        plt.ylabel("Faturamento")
        
        plt.show()

# if __name__ == "__main__":
    
#     LojaCharts.faturamentoCatg([10,20],["carro", "Moto"])
from service.lojaService import Loja
from charts.lojaCharts import LojaCharts

class Menu:
    def __init__(self):
        self._loja = Loja()
        self._graficos = LojaCharts(self._loja)
        
    
    def start(self):
        
        
        while(True):
            print("\n1. Faturamneto total")
            print("2. Faturamneto individual")
            print("3. Porcentagem do faturamento por categoria")
            print("4. Categoria com o maior faturamento ")
            print("5. Produto com maior faturamento")
            print("6. faturamento por categoria")
            print("7. Total vendidos")
            print("8. Produto mais vendido")
            print("9. Produto com mais de 5 vendas")
            print("10. Relatório")
            print("11. Gráficos")
            print("0. Sair")
            
            try:
                opcao = int(input("\nEscolha uma opção: "))
            except Exception as e:
                print(f"\nOcorreu um erro: \n{e} \nTente Novamente!")
                continue
            
            if opcao == 0:
                print("SAINDO....")
                break
            elif opcao == 1:
                print(self._loja.faturamentoTotal())
            elif opcao == 2:
                print(self._loja.faturamentoIndividual())
            elif opcao == 3:
                print(self._loja.participacaoFaturamentoCatg())
            elif opcao == 4:
                print(self._loja.maiorfaturamentoCatg())
            elif opcao == 5:
                print(self._loja.maiorfaturamentoProd())
            elif opcao == 6:
                print(self._loja.participacaoFaturamentoCatg())
            elif opcao == 7:
                print(self._loja.totalVendidos())
            elif opcao == 8:
                print(self._loja.maisVendido())
            elif opcao == 9:
                print(self._loja.filtroQtdVenda(5))
            elif opcao == 10:
                self._loja.relatorio()
            elif opcao == 11:
                self.graficosLoja()
            else:
                print("Opçao não encontrada!")

                
    def graficosLoja(self):
        
        while(True):
            print("==Gráficos==")
            print("\n1. faturamento por produto")
            print("2. faturamento por categoria")
            print("0. Sair")
            
            try:
                opcao = int(input("\nEscolha uma opção: "))
            except Exception as e:
                print(f"\nOcorreu um erro: \n{e} \nTente Novamente!")
                continue
            
            if opcao == 0:
                break
            
            elif opcao == 1:
                self._graficos.faturamentoProd()
                
            elif opcao == 2:
                self._graficos.faturamentoCatg()
            
            else:
                print("Opoção não encontrada!!")
import pandas as pd


arquivo = "Fashion_Retail_Sales.csv"

try:
    dados = pd.read_csv(arquivo)
    print("Sucesso! O Python leu o arquivo de vendas.")
    print("\n--- Veja as primeiras 5 linhas dos seus dados: ---")
    # print(dados.head())
except Exception as e:
 print(f"Ops, algo deu errado: {e}")
print("\n--- Informações Gerais do arquivo ---") 
print(dados.info())
#Vamos ver quais são os itens que mais aparecem nessa lista
print("\n--- Contagem de itens por categoria: ---")
print(dados['Item Purchased'].value_counts())
#Criando o filtro: nota igual a 5.0
nota_maxima = dados[dados['Review Rating'] == 5.0]
print("\n --- Itens com a nota máxima de 5.0 ---")
print(nota_maxima)
#Itens com valores maiores que 80 reais
itens_maiores_80 = dados[dados['Purchase Amount (USD)'] > 80]
print('\n --- Itens com preço maior que 80 reais ---')
print(itens_maiores_80)
#Qual forma de pagamento é mais utilizada?
print("\n --- Contagem de formas de pagamento: ---")
print(dados['Payment Method'].value_counts())
#Mediana dos valores de compra
mediana_compra = dados['Purchase Amount (USD)'].median()
print(f"\n --- A mediana dos valores de compra é: {mediana_compra:.2f} USD ---")
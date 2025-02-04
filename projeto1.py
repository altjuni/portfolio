import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose

# Configuração para visualizações
sns.set(style="whitegrid")

# Simulação de um dataset de vendas
data = {
    'Data': pd.date_range(start='2023-01-01', periods=365, freq='D'),
    'Produto': np.random.choice(['Produto A', 'Produto B', 'Produto C', 'Produto D'], 365),
    'Vendas': np.random.randint(50, 500, size=365),
    'Regiao': np.random.choice(['Norte', 'Sul', 'Leste', 'Oeste'], 365)
}

# Criação do DataFrame
df = pd.DataFrame(data)

# Exibindo as primeiras linhas do dataset
print(df.head())

# ------------------------------
# Limpeza de Dados
# ------------------------------

# Verificar valores nulos
print("\nValores nulos por coluna:\n", df.isnull().sum())

# Verificar duplicatas
print("\nQuantidade de duplicatas:", df.duplicated().sum())

# Remover duplicatas, se houver
df = df.drop_duplicates()

# ------------------------------
# Análise Exploratória de Dados
# ------------------------------

# Estatísticas descritivas
print("\nEstatísticas descritivas:\n", df.describe())

# Vendas totais por produto
vendas_produto = df.groupby('Produto')['Vendas'].sum().sort_values(ascending=False)
print("\nVendas totais por produto:\n", vendas_produto)

# Vendas por região
vendas_regiao = df.groupby('Regiao')['Vendas'].sum().sort_values(ascending=False)
print("\nVendas por região:\n", vendas_regiao)

# ------------------------------
# Visualizações Gráficas
# ------------------------------

# Gráfico de Vendas por Produto
plt.figure(figsize=(8, 6))
sns.barplot(x=vendas_produto.index, y=vendas_produto.values, palette="viridis")
plt.title('Vendas Totais por Produto')
plt.xlabel('Produto')
plt.ylabel('Total de Vendas')
plt.show()

# Gráfico de Vendas por Região
plt.figure(figsize=(8, 6))
sns.barplot(x=vendas_regiao.index, y=vendas_regiao.values, palette="coolwarm")
plt.title('Vendas Totais por Região')
plt.xlabel('Região')
plt.ylabel('Total de Vendas')
plt.show()

# Tendência de Vendas ao longo do tempo
plt.figure(figsize=(12, 6))
df.groupby('Data')['Vendas'].sum().plot()
plt.title('Tendência de Vendas Diárias')
plt.xlabel('Data')
plt.ylabel('Vendas')
plt.show()

# ------------------------------
# Modelagem e Insights
# ------------------------------

# Análise de Correlação
# Codificando variáveis categóricas para análise de correlação
df_encoded = df.copy()
df_encoded['Produto'] = df_encoded['Produto'].astype('category').cat.codes
df_encoded['Regiao'] = df_encoded['Regiao'].astype('category').cat.codes

# Matriz de correlação
correlation_matrix = df_encoded.corr()
print("\nMatriz de Correlação:\n", correlation_matrix)

# Mapa de calor da correlação
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Matriz de Correlação')
plt.show()

# Decomposição de Séries Temporais
vendas_diarias = df.groupby('Data')['Vendas'].sum()
decomposition = seasonal_decompose(vendas_diarias, model='additive', period=30)

# Exibindo componentes da decomposição
plt.figure(figsize=(12, 8))
decomposition.plot()
plt.suptitle('Decomposição da Série Temporal de Vendas', fontsize=16)
plt.show()

# ------------------------------
# Insights
# ------------------------------

# Produto com maior desempenho
produto_top = vendas_produto.idxmax()
print(f"\nProduto com maior desempenho: {produto_top}")

# Região com maior volume de vendas
regiao_top = vendas_regiao.idxmax()
print(f"Região com maior volume de vendas: {regiao_top}")

# Identificação de sazonalidade
print("\nA decomposição da série temporal indica padrões sazonais que podem ser explorados para otimizar estratégias de vendas.")

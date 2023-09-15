#-------------------------------------------------------------------------------------------------------
#
#      script plotar estações  
#
#--------------------------------------------------------------------------------------------------------
# by reginaldo.venturadesa@gmail.com  em agosto de 2023 
#
#  
#
#---------------------------------------------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

import geopandas as gpd
import matplotlib.pyplot as plt



# Função para calcular a variancia no período
def plota_estacoes(df,arquivo_out_png, limite_max,limite_min):
    periodo = df[(df['per_dados_validos'] >=limite_min ) & (df['per_dados_validos'] <= limite_max)]
    print(len(periodo)) 

    if not periodo.empty:
       # Extrair as coordenadas das estações
       longitudes = periodo["longitude"]
       latitudes = periodo["latitude"]
       nomes = periodo["Nome"]

       # Extrair os valores da coluna "per_dados_validos"
       per_dados_validos = periodo["per_dados_validos"]

       # Definir mapeamento de cores com base nos intervalos especificados
       cmap = ListedColormap(['red','purple','magenta','violet','pink', 'orange','yellow', 'lime','green', 'blue','black'])
       bounds = [ 0, 0.1, 0.2, 0.3,  0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
       norm = plt.Normalize(bounds[0], bounds[-1])

      #colors = ['blue', 'green', 'yellow', 'orange', 'red', 'purple', 'pink', 'brown', 'gray', 'cyan', 'magenta', 'lime', 'teal', 'indigo', 'violet']


       # Plotar o gráfico com cores mapeadas
       plt.figure(figsize=(10, 8))
       scatter = plt.scatter(longitudes, latitudes, c=per_dados_validos, cmap=cmap, norm=norm, marker="o")
     
       # Plotar o shapefile
       gdf.plot(ax=plt.gca(), color='gray')  # Use ax=plt.gca() para sobrepor o shapefile ao scatter plot

       # Adicionar rótulos de estação
       for index, row in df.iterrows():
           plt.text(row['longitude'], row['latitude'], row['Nome'], fontsize=2, ha="right")

       plt.title("Distribuição de estações "+str(limite_max*100)+"% a "+str(limite_min*100)+"%")
       plt.xlabel("Longitude")
       plt.ylabel("Latitude")
       plt.grid(True)

       # Adicionar uma legenda de cores
       cbar = plt.colorbar(scatter)  # Use o objeto scatter como mappable
       print("0yyy")
       cbar.set_label("Percentagem de Dados Válidos", labelpad=15)
       
       # Salvar o gráfico como arquivo PNG
       plt.savefig(arquivo_out_png, dpi=300, bbox_inches="tight")
       plt.show()
       return None
    else:
       print("O DataFrame está vazio. Verifique o arquivo Excel e os cabeçalhos das colunas.")
       return None




# Carregar o shapefile
shapefile_path = 'bahia.shp'
gdf = gpd.read_file(shapefile_path)


# Carregar os dados do arquivo Excel
file_path = "selecao.xlsx"
sheet_name = "all"  # Substitua pelo nome correto da planilha, se necessário

# Ler o arquivo Excel, considerando a primeira linha como cabeçalhos das colunas
df = pd.read_excel(file_path, sheet_name=sheet_name)

plota_estacoes(df,"estacoes_BAHIA_100_a_80_per.png",1.0,.80) 
plota_estacoes(df,"estacoes_BAHIA_100_a_60_per.png",1.0,.60) 
plota_estacoes(df,"estacoes_BAHIA_100_a_50_per.png",1.0,.50) 

plota_estacoes(df,"estacoes_BAHIA_todo_o_conjunto.png",1,0) 
plota_estacoes(df,"estacoes_BAHIA_descartados.png",.30,0) 


plota_estacoes(df,"estacoes_BAHIA_30_a_50_per.png",.50,.30) 




# import pandas as pd
# import matplotlib.pyplot as plt

# # Carregar os dados do arquivo Excel
# file_path = "./relatorio.xlsx"
# df = pd.read_excel(file_path)

# # Carregar os dados do arquivo Excel
# file_path = "relatorio.xlsx"
# sheet_name = "CLIMA"  # Substitua pelo nome correto da planilha, se necessário

# # Ler o arquivo Excel, considerando a primeira linha como cabeçalhos das colunas
# df = pd.read_excel(file_path, sheet_name=sheet_name)


# # Extrair as coordenadas das estações
# longitudes = df["longitude"]
# latitudes = df["latitude"]
# nomes = df["Nome"]

# # Plotar o gráfico
# plt.figure(figsize=(10, 8))
# plt.scatter(longitudes, latitudes, marker="o", color="blue")

# # Adicionar rótulos de estação
# for i, nome in enumerate(nomes):
    # plt.text(longitudes[i], latitudes[i], nome, fontsize=2, ha="right")

# plt.title("Posição das Estações")
# plt.xlabel("Longitude")
# plt.ylabel("Latitude")
# plt.grid(True)

# # Salvar o gráfico como arquivo PNG
# plt.savefig("posicao_estacoes.png", dpi=300, bbox_inches="tight")
# plt.show()




# HUMAN RESOURCE ANALYTICS

![image](https://user-images.githubusercontent.com/65432970/149674264-d23ce4c9-6e1f-438d-8dcc-d8262d385ef1.png)

Neste projeto cobrindo todas as etapas de um projeto real de Data Science pude resolver o problema de como utilizar dados para responder a questões importantes para permitir que uma empresa tenha conhecimento sobre:
  
  - Quais são os fatores que influenciam para um colaborador deixar a empresa?
  - Como reter pessoas?
  - Como antecipar e saber se um determinado colaborador vai sair da empresa?
  - E por fim disponibilizar recursos para que a empresa consiga realizar a predição para verificar se um colaborador vai ou não deixar a empresa com base em atributos como comportamento e carga de trabalho, nível de satisfação com a empresa e resultados de performance.

# TECNOLOGIAS USADAS PARA A CONSTRUÇÃO DO PROJETO

![image](https://user-images.githubusercontent.com/65432970/149674414-12fcdfe6-b1ad-4f4d-835e-e471250f7ef2.png)

# ARQUITETURA DA SOLUÇÃO

![image](https://user-images.githubusercontent.com/65432970/149682323-6c2aed58-d35a-45e5-b33f-c147c9b28127.png)

Para resolver esse problema foi construído uma solução completa para armazenamento, gestão e automatização de fluxos de dados utilizando tecnologias como Apache Airflow, Docker e Minio além de explorar uma suíte poderosa de tecnologias para trabalhar com Análise de Dados e Machine Learning que são: Pandas, Scikit-learn, Pycaret,SweetViz, Streamlit.

Depois da infraestrutura devidamente criada e configurada, levando em consideração o desafio proposto foram criados e modelados atributos relevantes para análise utilizando fontes de dados diversas como arquivos em formato xlsx, json e dados no Sistemas de Gerenciamento de Banco de Dados MySQL.

- Coleta dos dados;
- Estruturação dos dados em um banco MySQL;
- Criação do DataLake separando em estágios;
- Desenvolvimento do Modelo de Machine Learning;
- Disponibilização da Solução

# ANÁLISE EXPLORATÓRIA DE DADOS

Na etapa de Análise Exploratória de Dados foram descobertos os vários insights importantes abaixo:

## Análise Univariada 

![image](https://user-images.githubusercontent.com/65432970/149682642-94251cce-1852-470d-b44d-14a45cea88aa.png)

- A empresa possui uma rotatividade de aproximadamento 24%.

## Análise Bivariada

![image](https://user-images.githubusercontent.com/65432970/149682697-eb3b30ce-0512-462c-8fd3-bfecc986ef15.png)

- Existe um pico de empregados com baixa satisfação mas a maior concentração está em 60 a 80.

![image](https://user-images.githubusercontent.com/65432970/149682690-da1c1489-0e10-4c07-ab78-1cff944c8988.png)

**Resumo:** 
 - Empregados com o nível de satisfação em 20 ou menos tendem a deixar a empresa.
 - Empregados com o nível de satisfação em até 50 tem maior probabilidade de deixar a empresa.
 - Existe uma razão para o pico de empregados insatisfeitos?

### 

![image](https://user-images.githubusercontent.com/65432970/149682746-15518acd-db5d-4e1c-9d6e-9a778b2de6ae.png)

**Summary:**
 - A maioria dos empregados que saíram tinha salário **baixo** ou **médio**.
 - Quase nenhum empregado com alto salário deixou a empresa.
 
**Questões:** 
 - Como é o ambiente de trabalho? Isso se difere por salário?
 - O que faz empregados com alto salário sairem da empresa.

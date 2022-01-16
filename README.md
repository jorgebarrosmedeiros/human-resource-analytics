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

![image](https://user-images.githubusercontent.com/65432970/149682835-11d37e24-2540-44a6-b48a-76c92fb1dea9.png)

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

![image](https://user-images.githubusercontent.com/65432970/149682844-bceb8edd-b243-41cf-8e13-7dc779048dce.png)

![image](https://user-images.githubusercontent.com/65432970/149682847-1f703b3d-eca4-49e2-a234-791a2c9f0893.png)

***
**Resumo:** Vamos ver mais informações sobre os departamentos da empresa.
 - Os departamentos de vendas, técnico e suporte são top 3 departamentos com maior índice de turnover.
 - O departamento management tem o menor volume de turnover.

**Questões:** 
 - Será que examinar em profundidade os departamentos que tem maior índice de turnover e o menor pode nos revelar mais    informações importantes?
 - Qual o salário nestes departamentos?

![image](https://user-images.githubusercontent.com/65432970/149682854-631d2c75-0b9b-4948-9938-2321d5121e02.png)

- Todos os empregados que estavam inseridos sem muitos projetos deixaram a empresa.

![image](https://user-images.githubusercontent.com/65432970/149682883-755261a8-76a2-4dfe-941e-6236d5f8642b.png)

![image](https://user-images.githubusercontent.com/65432970/149682877-ce1f2d45-39a2-4f49-a710-37415f7dde7c.png)

**Resumo:** 
 - Temos uma distribuição bimodal para o conjunto que deixou a empresa.
 - Colaboradores com **baixa performance** tendem a deixar a empresa.
 - Colaboradores com **alta performance** tendem a deixar a empresa.
 - O **ponto ideal** para os funcionários que permaneceram está dentro da avaliação de 60 à 80.

![image](https://user-images.githubusercontent.com/65432970/149682912-1c6b4030-10c3-4342-9063-b9c18a912d40.png)

***
**Resumo:** 
- Há um **aumento na avaliação** para os funcionários que realizaram mais projetos dentro do grupo de quem deixou a empresa. 
- Para o grupo de pessoas que permaneceram na empresa, os empregados tiveram uma **pontuação de avaliação consistente**, apesar do aumento nas contagens de projetos.
- Empregados que permaneceram na empresa tiveram uma **avaliação média em torno de 70%**, mesmo com o número de projetos crescendo.
- Esta relação muda drasticamente entre os empregados que deixaram a empresa. A partir de 3 projetos, as **médias de avaliação aumentam consideravelmente**.
- Empregados que tinham **dois projetos e uma péssima avaliação** saíram.
- Empregados com **mais de 3 projetos e avaliações altas** deixaram a empresa.

**Questões:**
  - Por que será que os funcionários que saíram tiveram em média uma avaliação superior aos funcionários que não saíram, mesmo com um aumento no número de projetos?
  - Os funcionários com avaliações mais baixas não deveriam ter tendência a sair mais da empresa?

## Clustering 

Através da análise foi possível desenvolver 3 grupos distintos para agrupar colaboradores que deixaram a empresa por comportamentos similares que são:

![image](https://user-images.githubusercontent.com/65432970/149682954-d7e75599-7706-492c-8070-5036dd5fd621.png)

- Grupo 1 (Empregados insatisfeitos e trabalhadores): A satisfação foi inferior a 20 e as avaliações foram superiores a 75. Que corresponde ao grupo de funcionários que deixaram a empresa e eram bons trabalhadores, mas se sentiam péssimos no trabalho.

- Grupo 2 (Empregados ruins e insatisfeitos): Satisfação entre 35 à 50 e as suas avaliações abaixo de ~ 58. Corresponde aos empregados que foram mal avaliados e se sentiram mal no trabalho.

- Grupo 3 (Empregados satisfeitos e trabalhadores): Representa os empregados ideais, que gostam do seu trabalho e são bem avaliados por seu desempenho.Este grupo pode indicar os empregados que deixaram a empresa porque encontraram outra oportunidade de trabalho.

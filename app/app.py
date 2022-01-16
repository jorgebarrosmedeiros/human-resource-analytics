#carregando as bibliotecas
import pandas as pd
import streamlit as st
from minio import Minio
import joblib
import pickle
import matplotlib.pyplot as plt
from lightgbm  import LGBMClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

#função auxiliar para transformar os dados que serão enviados para o modelo de classificação
def data_preparation(df):

    #selecionando as colunas que serão usadas para o treinamento
    select_columns = ['projectCount', 'satisfaction', 'evaluation', 'yearsAtCompany']
    df = df[select_columns]

    #change data types
    df["projectCount"]   = df["projectCount"].astype(int)
    df["satisfaction"]   = df["satisfaction"].astype(float)
    df["evaluation"]     = df["evaluation"].astype(float)
    df["yearsAtCompany"] = df["yearsAtCompany"].astype(int)

    #read scaling models
    evaluation_scaler = pickle.load(open("/scaler/evaluation_scaler.pkl","rb"))
    projectCount_scaler = pickle.load(open("/scaler/projectCount_scaler.pkl","rb"))
    satisfaction_scaler = pickle.load(open("/scaler/satisfaction_scaler.pkl","rb"))
    yearsAtCompany_scaler = pickle.load(open("/scaler/yearsAtCompany_scaler.pkl","rb"))
    
    #apply rescaling
    df["evaluation"]  = evaluation_scaler.transform(df[['evaluation']])
    df["projectCount"]  = projectCount_scaler.transform(df[['projectCount']])
    df["satisfaction"]  = satisfaction_scaler.transform(df[['satisfaction']])
    df["yearsAtCompany"]  = yearsAtCompany_scaler.transform(df[['yearsAtCompany']])

    return df

def predict(df):

    response = model.predict_proba(df)[:,1][0]
    return response

#Baixando os aquivos do Data Lake
client = Minio(
        "localhost:9000",
        access_key="minioadmin",
        secret_key="minioadmin",
        secure=False
    )

#modelo de classificacao,dataset e cluster.
client.fget_object("curated","model.pkl","/model/model.pkl")
client.fget_object("curated","dataset.csv","/data/dataset.csv")
client.fget_object("curated","cluster.joblib","/model/cluster.joblib")

#extraindo os modelos de rescaling para cada variável que será usada 
client.fget_object("curated",'evaluation_scaler.pkl','/scaler/evaluation_scaler.pkl')
client.fget_object("curated",'yearsAtCompany_scaler.pkl','/scaler/yearsAtCompany_scaler.pkl')
client.fget_object("curated",'satisfaction_scaler.pkl','/scaler/satisfaction_scaler.pkl')
client.fget_object("curated",'projectCount_scaler.pkl','/scaler/projectCount_scaler.pkl')

#carregando o modelo treinado.
model = pickle.load(open("/model/model.pkl","rb"))
model_cluster = joblib.load("/model/cluster.joblib")

#carregando o conjunto de dados.
dataset = pd.read_csv("/data/dataset.csv")

# título
st.title("Human Resource Analytics")

# subtítulo
st.markdown("Este é um Data App utilizado para exibir a solução de Machine Learning para o problema de Human Resource Analytics.")

# imprime o conjunto de dados usado
st.dataframe(dataset.head())

# grupos de empregados.
kmeans_colors = ['green' if c == 0 else 'red' if c == 1 else 'blue' for c in model_cluster.labels_]
kmeans_colors.append("green")

st.sidebar.subheader("Defina os atributos do empregado para predição de turnover")

# mapeando dados do usuário para cada atributo
satisfaction = st.sidebar.number_input("Nível de Satisfação do Funcionário (0 - 100)", value=dataset["satisfaction"].mean())
evaluation = st.sidebar.number_input("Avaliação do desempenho do Funcionário (0 - 100)", value=dataset["evaluation"].mean())
projectCount = st.sidebar.number_input("Quantidade de Projetos", value=dataset["projectCount"].mean())
yearsAtCompany = st.sidebar.number_input("Anos na empresa", value=dataset["yearsAtCompany"].mean())

# inserindo um botão na tela
btn_predict = st.sidebar.button("Realizar Classificação")

# verifica se o botão foi acionado
if btn_predict:
    data_teste = pd.DataFrame()
    data_teste["satisfaction"] = [satisfaction]
    data_teste["evaluation"] =	[evaluation]    
    data_teste["projectCount"] = [projectCount]
    data_teste["yearsAtCompany"] = [yearsAtCompany]

    #realiza a preparação dos dados
    data = data_preparation(data_teste)
    
    #realiza a predição
    result = predict(data)
    st.success("Probabilidade de Turnover: {:.2f}%".format(result*100))

    fig = plt.figure(figsize=(10, 6))
    plt.scatter( x="satisfaction"
                ,y="evaluation"
                ,data=dataset[dataset.turnover==1],
                alpha=0.25, color = kmeans_colors)
#
    plt.xlabel("Satisfaction")
    plt.ylabel("Evaluation")

    plt.scatter( x=model_cluster.cluster_centers_[:,0]
                ,y=model_cluster.cluster_centers_[:,1]
                ,color="black"
                ,marker="X",s=100)
    
    plt.scatter( x=[satisfaction]
                ,y=[evaluation]
                ,color="yellow"
                ,marker="X",s=300)
#
    plt.title("Grupos de Empregados - Satisfação vs Avaliação.")
    plt.show()
    st.pyplot(fig) 
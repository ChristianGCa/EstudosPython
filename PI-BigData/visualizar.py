
import pandas as pd
import matplotlib.pyplot as plt

# Lendo os arquivos
pars = pd.read_csv("/home/christian/Documentos/bases SIASUS/Bases-SIASUS/PARS2312.csv", encoding="ISO-8859-1", usecols=['PA_CIDPRI', 'PA_UFMUN', 'PA_CNPJCPF'])
cid = pd.read_csv("/home/christian/Documentos/bases SIASUS/Bases-SIASUS/S_CID.csv", encoding="ISO-8859-1", usecols=['CD_COD', 'CD_DESCR'])
mun = pd.read_csv("/home/christian/Documentos/bases SIASUS/Bases-SIASUS/tb_municip.csv", encoding="ISO-8859-1", usecols=['CO_MUNICIP', 'DS_NOME'])
cpf_cnpj = pd.read_csv("/home/christian/Documentos/bases SIASUS/Bases-SIASUS/CADGERRS.csv", encoding="ISO-8859-1", usecols=['CPF_CNPJ', 'FANTASIA'])

# Relacionando as colunas PA_CIDPRI e CD_COD das tabelas
pars = pd.merge(pars, cid, left_on='PA_CIDPRI', right_on='CD_COD')

# Relacionando as colunas PA_CNPJCPF e CPF_CNPJ das tabelas
pars = pd.merge(pars, cpf_cnpj, left_on='PA_CNPJCPF', right_on='CPF_CNPJ')

print(pars['FANTASIA'].value_counts())


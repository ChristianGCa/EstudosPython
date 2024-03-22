
import pandas as pd

pars = pd.read_csv("/home/christian/Documentos/bases SIASUS/Bases-SIASUS/PARS2312.csv", encoding="ISO-8859-1")

genero = pars["PA_SEXO"].value_counts()
cpfCnpj = pars["PA_CNPJCPF"].value_counts()

cpf_e_genero = pd.concat([cpfCnpj, genero], axis=1)
cpf_e_genero.columns = ["CPF/CNPJ", "Sexo"]

print(cpf_e_genero)

import gspread
import pandas as pd
import json


gc = gspread.oauth()
email = 'leitor-de-planilhas@dotted-signer-438321-m8.iam.gserviceaccount.com'
dict_planilhas = {}
with open("dicionario_planilhas.json", "r") as arquivo:
    dict_planilhas = json.load(arquivo)
    print(dict_planilhas)

class planilhas():

    def guarda_planilhas(nome_planilha):
        nome = nome_planilha
        nome_planilha = {"nome_planilha" : nome, "sheet" : sheet, "worksheet" : worksheet}
        print (f"Planilha {nome_planilha} foi guardada no dicionário {dict_planilhas}")
        dict_planilhas[nome] = nome_planilha;
        return dict_planilhas
     

    def criar_planilha(nome_planilha):
        sheet = gc.create(nome_planilha)
        worksheet = sheet.sheet1
        print(f"A Planilha {nome_planilha} foi criada com sucesso!")
        planilhas.guarda_planilhas(nome_planilha)
        planilhas.compartilhar_planilha(sheet)


    def abrir_planilha(sheet, nome_planilha, worksheet):
        sheet = gc.open(nome_planilha)
        worksheet = sheet.sheet1
        print(f"A planilha {nome_planilha} foi aberta!")
        return worksheet


    def compartilhar_planilha(sheet):
        sheet.share(email, perm_type = 'user', role = 'writer')
        print(f"Planiilha compartilhada corretamente com o E-mail {email}!")

class manipulacao_dados():
    def converte_df(worksheet):
        dataframe = pd.DataFrame(worksheet.get_all_records())
        print("Planilha convertida em dataframe!")
        print(dataframe)

    def separacao_dados():
        coluna_usuario = planilhas.worksheet.row_values()
        for usuario in coluna_usuario:
            if usuario == "Bernardo":
                print("O usuário é o bernardo")
            elif usuario == "Jessyka":
                print("O usuário é a jessyka")


if __name__ == "__main__":

    '''manipulacao_dados.converte_df()
    sheet = input("Digite a sheet: ")
    nome_planilha = input("Digite o nome da planilha: ")
    worksheet = input("Digite a worksheet: ")
    planilhas.criar_planilha(nome_planilha)
    dict_planilhas = planilhas.guarda_planilhas(nome_planilha)
    print(dict_planilhas)'''


    '''planilhas.abrir_planilha(dict_planilhas["dados-habitos"]['sheet'], dict_planilhas["dados-habitos"]['nome_planilha'], dict_planilhas["dados-habitos"]['worksheet'])'''

    manipulacao_dados.converte_df(planilhas.abrir_planilha(dict_planilhas["dados-habitos"]['sheet'], dict_planilhas["dados-habitos"]['nome_planilha'], dict_planilhas["dados-habitos"]['worksheet']))

    with open("dicionario_planilhas.json", "w") as arquivo:
        json.dump(dict_planilhas, arquivo, indent=4)

    



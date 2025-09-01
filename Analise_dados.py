import gspread
import pandas as pd
import json

dict_planilhas = {}

class planilhas():

    
    gc = gspread.oauth()
    email = 'leitor-de-planilhas@dotted-signer-438321-m8.iam.gserviceaccount.com'
    
    def carrega_dict():
        with open("dicionario_planilhas.json", "r") as arquivo:
                dict_planilhas = json.load(arquivo)
                print(f"Dados carregados em dict_planilhas! {dict_planilhas}")
 
    def guarda_dict_json():
        planilhas.carrega_dict()
        with open("dicionario_planilhas.json", "w") as arquivo:
                print("Guardando o dicionário com as informações no Json...")
                json.dump(dict_planilhas, arquivo, indent=14)
                print(dict_planilhas)


    def variaveis_planilhas():
        sheet = input("digite a sheet: ")
        worksheet = input("Digite o nome da worksheet: ")
        nome_planilha =  input("Digite o nome da planilha: ")
        return sheet, worksheet, nome_planilha
    
    def compartilhar_planilha(sheet):
        sheet.share(planilhas.email, perm_type = 'user', role = 'writer')
        print(f"Planiilha compartilhada corretamente com o E-mail {planilhas.email}!")

    def parametros_planilhas():
        try:
            lista_planilhas = []
            cont = 0
            for i in dict_planilhas:
                lista_planilhas.append(i)
                print (f"{cont} - {i}")
                cont += 1

            chave = int(input("Insira o número da planilha que deseja manipular: "))

            for i in planilhas.dict_planilhas:
                if lista_planilhas[chave] == i:
                    nome_planilha = planilhas.dict_planilhas[lista_planilhas[chave]]["nome_planilha"]
                    sheet = planilhas.dict_planilhas[lista_planilhas[chave]]["sheet"]
                    worksheet = planilhas.dict_planilhas[lista_planilhas[chave]]["worksheet"]
                    print (f"nome da planilha = {nome_planilha}, sheet = {sheet}, worksheet = {worksheet}")
                    return nome_planilha, sheet, worksheet

        except IndexError as e:
            print (f"O index passado não existe na lista! {e}")
    
    def guarda_planilhas(nome_planilha, sheet, worksheet):
        nome = nome_planilha
        nome_planilha = {"nome_planilha" : nome, "sheet" : sheet, "worksheet" : worksheet}
        print (f"Planilha {nome_planilha} foi guardada no dicionário {dict_planilhas}")
        dict_planilhas[nome] = nome_planilha;
        planilhas.guarda_dict_json()
        return dict_planilhas
     

    def criar_planilha(nome_planilha = variaveis_planilhas()[0]):
        sheet = planilhas.gc.create(nome_planilha)
        print(f"Planilha {nome_planilha}criada!")
        worksheet = sheet.sheet1
        print(f"O worksheet {worksheet} foi criado com sucesso!")
        planilhas.guarda_planilhas(nome_planilha, sheet, worksheet)
        planilhas.compartilhar_planilha(sheet)


    def abrir_planilha(sheet, nome_planilha, worksheet):
        sheet = planilhas.gc.open(nome_planilha)
        worksheet = sheet.sheet1
        print(f"A planilha {nome_planilha} foi aberta!")
        return worksheet


class manipulacao_dados():
    def converte_df(worksheet = planilhas.variaveis_planilhas):
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


     #planilhas.abrir_planilha(dict_planilhas["dados-habitos"]['sheet'], dict_planilhas["dados-habitos"]['nome_planilha'], dict_planilhas["dados-habitos"]['worksheet'])

    '''planilhas.variaveis_planilhas()
    planilhas.criar_planilha()'''

    #planilhas.criar_planilha()
    #planilhas.carrega_dict()
    planilhas.guarda_planilhas(planilhas.variaveis_planilhas()[0], planilhas.variaveis_planilhas()[1], planilhas.variaveis_planilhas()[2])
    #planilhas.guarda_dict_json()
    #planilhas.parametros_planilhas()
    



    #manipulacao_dados.converte_df(planilhas.abrir_planilha(dict_planilhas["dados-habitos"]['sheet'], dict_planilhas["dados-habitos"]['nome_planilha'], dict_planilhas["dados-habitos"]['worksheet']))

    

    



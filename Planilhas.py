import Manipulacao_dados as md
import gspread
import pandas as pd
import json

dict_planilhas = {}
dict_dados_bernardo = {}
dict_dados_jessyka  = {}
gc = gspread.oauth()
email = 'leitor-de-planilhas@dotted-signer-438321-m8.iam.gserviceaccount.com'

class planilhas():

    # Continuar estruturaçãode logica de dicionarios
    def escolher_json():
        dict_jsons = {
            "json_planilhas" :"dict_planilhas.json",
            "json_dados_bernardo" : "dict_dados_bernardo.json",
            "json_dados_jessyka" : "dict_dados_jessyka.json"
        }
        cont = 0
        opcao = int(input("Insira o número do dicionário que deseja usar: "))
        for chave in dict_jsons:
            cont += 1
            print(f"{cont} - {chave}")
        if opcao == 1:
            return dict_planilhas, dict_jsons["json_planilhas_geral"]
        elif opcao == 2:
            return dict_dados_bernardo, dict_jsons["json_dados_bernardo"]
        elif opcao == 3:
            return dict_dados_jessyka, dict_jsons["json_dados_jessyka"]

    def carrega_dict(dict_return_def, caminho_json):
        try:
            with open(caminho_json, "r") as arquivo:
                    dict_return_def = json.load(arquivo)
                    print(f"Os dados do Json já estão disponiveis em dict_planilhas! ")
                    return dict_return_def
        except json.decoder.JSONDecodeError as erro:
            print(f"O dicionário está vazio! Segue o erro {erro}")

    dict_planilhas = carrega_dict(dict_planilhas, "dict_planilhas.json")

    def guarda_dict_json():
        with open("caminho_json", "w") as arquivo:
                print("Guardando o dicionário com as informações no Json...")
                json.dump(dict_planilhas, arquivo, indent=4)
                print(dict_planilhas)

    def parametros_variaveis():
        sheet = input("digite a sheet: ")
        worksheet = input("Digite o nome da worksheet: ")
        nome_planilha =  input("Digite o nome da planilha: ")
        
        return sheet, worksheet, nome_planilha

    def parametros_dict():
        lista_planilhas = []
        cont = 0
        sheet = ''
        worksheet = ''
        nome_planilha = ''
        print("\n---- Dicionários disponíveis ----")
        for chave in planilhas.dict_planilhas:
            lista_planilhas.append(chave)
            print (f"{cont} - {chave}")
            cont += 1
        try: 
            chave = int(input("Insira o número da planilha que deseja manipular: "))
        except ValueError as e:
            print(f"Input inválido! Favor inserir o número da planilha! {e}")

        try:
            for i in planilhas.dict_planilhas:
                if lista_planilhas[chave] == i:
                    nome_planilha = planilhas.dict_planilhas[lista_planilhas[chave]]["nome_planilha"]
                    sheet = planilhas.dict_planilhas[lista_planilhas[chave]]["sheet"]
                    worksheet = planilhas.dict_planilhas[lista_planilhas[chave]]["worksheet"]
                    print (f"nome da planilha = {nome_planilha}, sheet = {sheet}, worksheet = {worksheet}")
        except IndexError as e:
            print (f"O index passado não existe na lista! {e}")
        return sheet, worksheet, nome_planilha

    def guarda_planilhas():
        sheet_variaveis, worksheet_variaveis, nome_planilha_variaveis = planilhas.parametros_variaveis()
        nome = nome_planilha_variaveis
        nome_planilha_variaveis = {"nome_planilha" : nome, "sheet" : sheet_variaveis, "worksheet" : worksheet_variaveis}
        print (f"Planilha {nome_planilha_variaveis} foi guardada no dicionário {dict_planilhas}")
        dict_planilhas[nome] = nome_planilha_variaveis;
        planilhas.guarda_dict_json()

    def compartilhar_planilha(sheet):
        sheet.share(planilhas.email, perm_type = 'user', role = 'writer')
        print(f"Planiilha compartilhada corretamente com o E-mail {planilhas.email}!")

    def criar_planilha():
        sheet_variaveis, worksheet_variaveis, nome_planilha_variaveis = planilhas.parametros_variaveis()
        planilhas.guarda_planilhas(sheet_variaveis, worksheet_variaveis, nome_planilha_variaveis)
        sheet = planilhas.gc.create(nome_planilha_variaveis)
        print(f"Planilha {nome_planilha_variaveis}criada!")
        worksheet_variaveis = sheet.sheet1
        print(f"O worksheet {worksheet_variaveis} foi criado com sucesso!")
        planilhas.compartilhar_planilha(sheet)

    def abrir_planilha():
        nome_planilha_dict = planilhas.parametros_dict()[2]
        sheet = gc.open(nome_planilha_dict)
        worksheet_gspread = sheet.sheet1
        print(f"A planilha {nome_planilha_dict} foi aberta!")
        return worksheet_gspread
    
    def separa_dados():
        worksheet_gspread = planilhas.abrir_planilha()
        cell_list_bernardo = worksheet_gspread.findall("Bernardo")
        print(cell_list_bernardo)

        cell_list_jessyka = worksheet_gspread.findall("Jessyka")
        print(cell_list_jessyka)
    
        for celula in cell_list_bernardo:
            values_list_bernardo = worksheet_gspread.row_values(celula.row)
            print(celula)
            print(values_list_bernardo)
            
        for celula in cell_list_jessyka:
            values_list_jessyka = worksheet_gspread.row_values(celula.row)
            print(celula)
            print(values_list_jessyka)

if __name__ == "__main__":
    menu = int(input("---- Menu Planilhas ----\n" \
                     "Escolha a opção de acordo com o número da posição:\n" \
                     "1 - Criar nova planilha: \n" \
                     "2 - Abrir planilha: \n" \
                     "3 - Manipular dados: \n" \
                     "0 - Sair: "))
    while menu != 0:
        if menu == 1:
            planilhas.criar_planilha(planilhas.parametros_variaveis()[2])
            break

        elif menu == 2:
            planilhas.abrir_planilha()
            break

        elif menu == 3:
            planilhas.separa_dados()
            break


    


  
    

    



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
    def escolher_json(opcao):
        dict_jsons = {
            "json_planilhas" :"dict_planilhas.json",
            "json_dados_bernardo" : "dict_dados_bernardo.json",
            "json_dados_jessyka" : "dict_dados_jessyka.json"
        }
        cont = 0
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

    def guarda_dict_json(dict_return_def, caminho_json):
        with open(caminho_json, "w", encoding = 'utf-8') as arquivo:
                json.dump(dict_return_def, arquivo, ensure_ascii = False, indent=4)
                

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
    
    
    def separa_dados(worksheet_gspread = None):
        if worksheet_gspread is None:
            worksheet_gspread = planilhas.abrir_planilha()
        
        try:    
            dict_return_bernardo, caminho_json_bernardo = planilhas.escolher_json(2)
            planilhas.dict_dados_bernardo = planilhas.carrega_dict(dict_return_bernardo, caminho_json_bernardo)
            cell_list_bernardo = worksheet_gspread.findall("Bernardo")
            cont_bernardo = 1
            for i in cell_list_bernardo:
                dias_bernardo = f"Dia {cont_bernardo}"

                linhas_bernardo = worksheet_gspread.row_values(i.row)

                sub_dict_bernardo = {"Data" : linhas_bernardo[0], "Horario que acordou" : linhas_bernardo[2], "Academia" : linhas_bernardo[3], "Litros Agua" : linhas_bernardo[4], "Refeicoes" : linhas_bernardo[5], "Horario cama" : linhas_bernardo[6]}
                
                planilhas.dict_dados_bernardo[dias_bernardo] = sub_dict_bernardo

                planilhas.guarda_dict_json(planilhas.dict_dados_bernardo, caminho_json_bernardo)
                
                cont_bernardo += 1



            dict_return_jessyka, caminho_json_jessyka = planilhas.escolher_json(3)
            planilhas.dict_dados_jessyka = planilhas.carrega_dict(dict_return_jessyka, caminho_json_jessyka)
            cell_list_jessyka = worksheet_gspread.findall("Jessyka")
            cont_jessyka = 1
            for j in cell_list_jessyka:
                dias_jessyka = f"Dia {cont_jessyka}"

                linhas_jessyka = worksheet_gspread.row_values(j.row)

                sub_dict_jessyka = {"Data" : linhas_jessyka[0], "Horario que acordou" : linhas_jessyka[2], "Academia" : linhas_jessyka[3], "Litros Agua" : linhas_jessyka[4], "Refeicoes" : linhas_jessyka[5], "Horario cama" : linhas_jessyka[6]}
                
                planilhas.dict_dados_jessyka[dias_jessyka] = sub_dict_jessyka

                planilhas.guarda_dict_json(planilhas.dict_dados_jessyka, caminho_json_jessyka)
                
                cont_jessyka += 1
        except TypeError as e:
            print (f"O dict está retornando None! Se o json estiver vazio, insira um colchete vazio, para que ele não retorne None. Segue o erro {e}")

        return planilhas.dict_dados_bernardo, planilhas.dict_dados_jessyka, worksheet_gspread

if __name__ == "__main__":
    menu = int(input("---- Menu Planilhas ----\n" \
                     "Escolha a opção de acordo com o número da posição:\n" \
                     "1 - Criar nova planilha: \n" \
                     "2 - Abrir planilha: \n" \
                     "3 - Manipular dados: \n" \
                     "4 - Converter em DataFrame \n" \
                     "5 - Comparar dados\n" \
                     "6 - escolhe comparação\n" \
                     "0 - Sair: "))
    
    worksheet_gspread = None
    dados_bernardo = None
    dados_jessyka = None
    while menu != 0:
        if menu == 1:
            planilhas.criar_planilha(planilhas.parametros_variaveis()[2])
            break

        elif menu == 2:
            planilhas.abrir_planilha()
            break

        elif menu == 3:
            if worksheet_gspread is None:
                worksheet_gspread = planilhas.abrir_planilha()
            dados_bernardo, dados_jessyka, _ = planilhas.separa_dados(worksheet_gspread)
            break

        elif menu == 4:
            if worksheet_gspread is None or dados_bernardo is None or dados_jessyka is None:
                worksheet_gspread, dados_bernardo, dados_jessyka = planilhas.separa_dados(worksheet_gspread)
            md.manipulacao_dados.converte_df()
            break
        elif menu == 5:
            if worksheet_gspread is None or dados_bernardo is None or dados_jessyka is None:
                worksheet_gspread = planilhas.abrir_planilha()
                dados_bernardo, dados_jessyka, _ = planilhas.separa_dados(worksheet_gspread)
            md.manipulacao_dados.compara_dados(dados_bernardo)
            break
        elif menu == 6:
            md.manipulacao_dados.escolhe_comparacao()
            break
    


  
    

    



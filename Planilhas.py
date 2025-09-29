import Manipulacao_dados as md
import gspread
import pandas as pd
import json
from datetime import datetime, date, timedelta

dict_planilhas = {}
dict_dados_bernardo = {}
dict_dados_jessyka  = {}
gc = gspread.oauth()
email = 'leitor-de-planilhas@dotted-signer-438321-m8.iam.gserviceaccount.com'

class planilhas():

    # Continuar estruturaçãode logica de dicionarios
    def escolher_json(opcao = None):
        dict_jsons = {
            "json_planilhas" :"dict_planilhas.json",
            "json_dados_bernardo" : "dict_dados_bernardo.json",
            "json_dados_jessyka" : "dict_dados_jessyka.json"
        }
        cont = 0
        if opcao is None:
            for chave in dict_jsons:
                cont += 1
                print(f"{cont} - {chave}")
            opcao = input("Escolha o dicionário que deseja abrir: ")
        if opcao == 1:
            print(dict_jsons["json_planilhas_geral"])
            return dict_planilhas, dict_jsons["json_planilhas_geral"]
        elif opcao == 2:
            print(dict_jsons["json_dados_bernardo"])
            return dict_dados_bernardo, dict_jsons["json_dados_bernardo"]
        elif opcao == 3:
            print(dict_jsons["json_dados_jessyka"])
            return dict_dados_jessyka, dict_jsons["json_dados_jessyka"]

    def carrega_dict(dict_return_def, caminho_json):
        try:
            with open(caminho_json, "r") as arquivo:
                    dict_return_def = json.load(arquivo)
                    print(f"Os dados do Json já estão disponiveis em dict_planilhas! ")
                    return dict_return_def
        except json.decoder.JSONDecodeError as erro:
            print(f"O dicionário está vazio! Segue o erro abaixo: \n {erro}")

    dict_planilhas = carrega_dict(dict_planilhas, "dict_planilhas.json")

    def guarda_dict_json(dict_return_def, caminho_json):
        with open(caminho_json, "w", encoding = 'utf-8') as arquivo:
                json.dump(dict_return_def, arquivo, ensure_ascii = False, indent=4)
                
    def parametros_variaveis():
        sheet = input("digite a sheet: ")
        worksheet = input("Digite o nome da worksheet: ")
        nome_planilha =  input("Digite o nome da planilha: ")
        
        return sheet, worksheet, nome_planilha

    def parametros_dict(chave = None):
        lista_planilhas = []
        cont = 0
        sheet = ''
        worksheet = ''
        nome_planilha = ''

        if chave == None:
            print("\n---- Dicionários disponíveis ----")
            for j in planilhas.dict_planilhas:
                lista_planilhas.append(j)
                print (f"{cont} - {j}")
                cont += 1
            chave = int(input("Insira o número da planilha que deseja manipular: "))

        else: 
            for j in planilhas.dict_planilhas:
                lista_planilhas.append(j)

        try:
            for i in planilhas.dict_planilhas:
                if lista_planilhas[chave] == i:
                    nome_planilha = planilhas.dict_planilhas[lista_planilhas[chave]]["nome_planilha"]
                    sheet = planilhas.dict_planilhas[lista_planilhas[chave]]["sheet"]
                    worksheet = planilhas.dict_planilhas[lista_planilhas[chave]]["worksheet"]
                    print (f"nome da planilha = {nome_planilha}")
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

    def abrir_planilha(worksheet_gspread = None):
        if  worksheet_gspread is None:
            nome_planilha_dict = planilhas.parametros_dict(2)[2]
            sheet = gc.open(nome_planilha_dict)
            worksheet_gspread = sheet.sheet1
            print(f"A planilha {nome_planilha_dict} foi aberta!")
            return worksheet_gspread
        else:
            return worksheet_gspread
    

    # Continuar logica de criar uma classe coringa para transformação de dados 
    def converte_dados(worksheet_gspread = None, parametro_json = None):
        mascara_data = '%d/%m/%Y %H%M%S'
        lista_datas = []

        if parametro_json is None:
            planilhas.escolher_json()
        

    def separa_dados(worksheet_gspread = None):
        mascara_data = '%d/%m/%Y %H:%M:%S'
        lista_datas_jessyka = []
        lista_datas_bernardo = []
        if worksheet_gspread is None:
                worksheet_gspread = planilhas.abrir_planilha()
        worksheet_gspread.get_all_records()
        try:    
            dict_return_bernardo, caminho_json_bernardo = planilhas.escolher_json(2)
            planilhas.dict_dados_bernardo = planilhas.carrega_dict(dict_return_bernardo, caminho_json_bernardo)
            cell_list_bernardo = worksheet_gspread.findall("Bernardo")
            cont_bernardo = 1
            for i in cell_list_bernardo:
                dias_bernardo = f"Dia {cont_bernardo}"
                linhas_bernardo = worksheet_gspread.row_values(i.row)
                if (linhas_bernardo[3] == "Sim"):
                    linhas_bernardo.pop(3)
                    linhas_bernardo.insert(3, 1)
                elif (linhas_bernardo[3] == "Não"):
                    linhas_bernardo.pop(3)
                    linhas_bernardo.insert(3, 0)
                    

                sub_dict_bernardo = {"Data" : linhas_bernardo[0], "Horario que acordou" : linhas_bernardo[2], "Academia" : linhas_bernardo[3], "Litros Agua" : linhas_bernardo[4], "Refeicoes" : linhas_bernardo[5], "Horario cama" : linhas_bernardo[6]}
                
                planilhas.dict_dados_bernardo[dias_bernardo] = sub_dict_bernardo

                planilhas.guarda_dict_json(planilhas.dict_dados_bernardo, caminho_json_bernardo)
                
                cont_bernardo += 1

            dict_return_jessyka, caminho_json_jessyka = planilhas.escolher_json(3)
            planilhas.dict_dados_jessyka = planilhas.carrega_dict(dict_return_jessyka, caminho_json_jessyka)
            cell_list_jessyka = worksheet_gspread.findall("Jessyka")
            cont_jessyka = 0
            for j in cell_list_jessyka:
                dias_jessyka = f"Dia {cont_jessyka}"

                linhas_jessyka = worksheet_gspread.row_values(j.row)

                if (linhas_jessyka[0]):
                    data_jessyka = datetime.strptime(linhas_jessyka[0], mascara_data).date()
                    linhas_jessyka.pop(0)
                    linhas_jessyka.insert(0, data_jessyka.strftime('%d/%m/%y'))
                    lista_datas_jessyka.append(linhas_jessyka[0])
                    if(len(lista_datas_jessyka) > 1 and lista_datas_jessyka[cont_jessyka] is lista_datas_jessyka[cont_jessyka - 1]):
                        lista_datas_jessyka.pop(cont_jessyka)
                        data_estimada = lista_datas_jessyka[cont_jessyka-1] + timedelta(days = 1)
                        lista_datas_jessyka.insert(cont_jessyka, data_estimada)

                if (linhas_jessyka[2]):
                    hora_acordou = int(linhas_jessyka[2][:2])
                    linhas_jessyka.pop(2)
                    linhas_jessyka.insert(2, hora_acordou)
                    print(hora_acordou)
                    
                if (linhas_jessyka[3] == "Sim"):
                    linhas_jessyka.pop(3)
                    linhas_jessyka.insert(3, 1)
                elif (linhas_jessyka[3] == "Não"):
                    linhas_jessyka.pop(3)
                    linhas_jessyka.insert(3, 0)
                cont_jessyka += 1

                if (linhas_jessyka[4]):
                    litros_agua = int(linhas_jessyka[4])
                    linhas_jessyka.pop(4)
                    linhas_jessyka.insert(4, litros_agua)

                if (linhas_jessyka[5]):
                    refeicoes = int(linhas_jessyka[5])
                    linhas_jessyka.pop(5)
                    linhas_jessyka.insert(5, refeicoes)

                if (linhas_jessyka[6]):
                    horario_cama = int(linhas_jessyka[6][:2])
                    linhas_jessyka.pop(6)
                    linhas_jessyka.insert(6, horario_cama)

            k = 0
            while k < len(lista_datas_jessyka):
                if(k + 1 < len(lista_datas_jessyka)):
                    if lista_datas_jessyka[k] == lista_datas_jessyka[k+1]:
                        data_jessyka = datetime.strptime(lista_datas_jessyka[k+1], '%d/%m/%y')
                        data_estimada = data_jessyka + timedelta(days = 1)
                        lista_datas_jessyka.pop(k+1)
                        lista_datas_jessyka.insert(k+1, data_estimada.strftime('%d/%m/%y'))
                        k = -1
                k += 1



            sub_dict_jessyka = {"Data" : linhas_jessyka[0], "Horario que acordou" : linhas_jessyka[2], "Academia" : linhas_jessyka[3], "Litros Agua" : linhas_jessyka[4], "Refeicoes" : linhas_jessyka[5], "Horario cama" : linhas_jessyka[6]}
                
            planilhas.dict_dados_jessyka[dias_jessyka] = sub_dict_jessyka

            planilhas.guarda_dict_json(planilhas.dict_dados_jessyka, caminho_json_jessyka)
        except TypeError as e:
            print (f"O dict está retornando None! Se o json estiver vazio, insira um colchete vazio, para que ele não retorne None. Segue o erro abaixo: \n {e}")

        return planilhas.dict_dados_bernardo, planilhas.dict_dados_jessyka, worksheet_gspread
    
    def limpa_dados():
        pass
        

if __name__ == "__main__":
    menu = int(input("---- Menu Planilhas ----\n" \
                     "Escolha a opção de acordo com o número da posição:\n" \
                     "1 - Criar nova planilha: \n" \
                     "2 - Abrir planilha: \n" \
                     "3 - Manipular dados: \n" \
                     "4 - Converter em DataFrame \n" \
                     "5 - Separa dados\n"
                     "6 - Comparar dados\n" \
                     "7 - escolhe comparação\n" \
                     "0 - Sair: \n"))
    
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
                worksheet_gspread = planilhas.abrir_planilha()
                dados_bernardo, dados_jessyka, _ = planilhas.separa_dados(worksheet_gspread)
            md.manipulacao_dados.converte_df(dados_bernardo, dados_jessyka, worksheet_gspread)
            break

        elif menu == 5:
            if worksheet_gspread is None:
                worksheet_gspread = planilhas.abrir_planilha()
            planilhas.separa_dados(worksheet_gspread)
            break
            

        elif menu == 6:
            if worksheet_gspread is None or dados_bernardo is None:
                dados_bernardo = planilhas.parametros_dict(0)
                dados_jessyka = planilhas.parametros_dict(1)
                worksheet_gspread = planilhas.abrir_planilha()
                dados_bernardo, dados_jessyka, _ = planilhas.separa_dados(worksheet_gspread)
            md.manipulacao_dados.compara_dados(dados_bernardo, dados_jessyka, worksheet_gspread)
            break
        elif menu == 7:
            md.manipulacao_dados.escolhe_comparacao()
            break
        elif menu == 8:
            md.manipulacao_dados.cria_grafico()
            break
    


  
    

    



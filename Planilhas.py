import Manipulacao_dados as md
import gspread
import pandas as pd
import json
from datetime import datetime, date, timedelta

dict_planilhas = {}
dict_dados_bernardo = {}
dict_dados_int_bernardo = {}
dict_dados_jessyka  = {}
dict_dados_int_jessyka = {}
gc = gspread.oauth()
email = 'leitor-de-planilhas@dotted-signer-438321-m8.iam.gserviceaccount.com'

class planilhas():

    # Continuar estruturaçãode logica de dicionarios
    def escolher_json(opcao = None):
        dict_jsons = {
            "json_planilhas" :"dict_planilhas.json",
            "json_dados_bernardo" : "dict_dados_bernardo.json",
            "json_dados_jessyka" : "dict_dados_jessyka.json",
            "json_dados_int_bernardo" : "dict_dados_int_bernardo.json",
            "json_dados_int_jessyka" : "dict_dados_int_jessyka.json"
        }
        cont = 0
        if opcao is None:
            for chave in dict_jsons:
                cont += 1
                print(f"{cont} - {chave}")
            opcao = input("Escolha o dicionário que deseja abrir: ")
        if opcao == 1:
            print(dict_jsons["json_planilhas"])
            return dict_planilhas, dict_jsons["json_planilhas_geral"]
        elif opcao == 2:
            print(dict_jsons["json_dados_bernardo"])
            return dict_dados_bernardo, dict_jsons["json_dados_bernardo"]
        elif opcao == 3:
            print(dict_jsons["json_dados_jessyka"])   
            return dict_dados_jessyka, dict_jsons["json_dados_jessyka"]
        elif opcao == 4:
            print(dict_jsons["json_dados_int_bernardo"])
            return dict_dados_int_bernardo, dict_jsons["json_dados_int_bernardo"]
        elif opcao == 5:
            print(dict_jsons["json_dados_int_jessyka"])
            return dict_dados_int_jessyka, dict_jsons['json_dados_int_jessyka']
        
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

    def transfere_dados_para_lista(worksheet_gspread = None, parametro_json = None):
        linhas_convertidas = {}

        if worksheet_gspread is None:
            worksheet_gspread = planilhas.abrir_planilha()

        if (parametro_json == 2 or parametro_json == 4):
            nome = "Bernardo"

        if(parametro_json == 3 or parametro_json == 5):
            nome = "Jessyka" 

        cell_list = worksheet_gspread.findall(nome)

        print(cell_list)

        cell_list_copia = cell_list.copy()
        cont = 0
        for i in cell_list_copia:
            linhas = worksheet_gspread.row_values(i.row)
            linhas_convertidas[cont] = linhas
            cont += 1
        linhas_convertidas_copia = linhas_convertidas.copy()

        return linhas_convertidas_copia, cell_list_copia

    def converte_dados(linhas_convertidas, cell_list, parametro_json):
        mascara_data = '%d/%m/%Y %H:%M:%S'
        dict_dados = {}
        lista_datas = []

        if parametro_json is None:
           dict_return, caminho_json = planilhas.escolher_json()
        elif parametro_json is not None:
            dict_return, caminho_json = planilhas.escolher_json(parametro_json)
        
        dict_dados = planilhas.carrega_dict(dict_return, caminho_json)
        if dict_dados is None:
            dict_dados = {}

        print(linhas_convertidas)

        cont = 0
        if (parametro_json == 2 or parametro_json == 3):
            for i in cell_list:
                if (linhas_convertidas[cont][0]):
                    data = datetime.strptime(linhas_convertidas[cont][0], mascara_data).date()
                    lista_datas.insert(cont, data)
                    print(data)
                cont += 1

        elif (parametro_json == 4 or parametro_json == 5):
            for i in cell_list:
                if (linhas_convertidas[cont][0]):
                    data = datetime.strptime(linhas_convertidas[cont][0], mascara_data).date()
                    lista_datas.insert(cont, data)

                if(linhas_convertidas[cont][2]):
                        hora_acordou = int(linhas_convertidas[cont][2][:2])
                        linhas_convertidas[cont][2] = hora_acordou

                if(linhas_convertidas[cont][3] == "Sim"):
                    linhas_convertidas[cont][3] = 1
                elif(linhas_convertidas[cont][3] == "Não"):
                    linhas_convertidas[cont][3] = 0
                
                if (linhas_convertidas[cont][4]):
                    litros_agua = int(linhas_convertidas[cont][4])
                    linhas_convertidas[cont][4] = litros_agua

                if (linhas_convertidas[cont][5]):
                    refeicoes = int(linhas_convertidas[cont][5])
                    linhas_convertidas[cont][5] = refeicoes

                if (linhas_convertidas[cont][6]):
                        horario_cama = int(linhas_convertidas[cont][6][:2])
                        linhas_convertidas[cont][6] = horario_cama
                    
                print(linhas_convertidas[cont])
                cont += 1

        k = 0
        while k < len(lista_datas):
            if(k + 1 < len(lista_datas)):
                if lista_datas[k] == lista_datas[k+1]:
                    if isinstance(lista_datas[k+1], str):
                        data = datetime.strptime(lista_datas[k+1], '%d/%m/%y')
                    else:
                        data = lista_datas[k+1]
                    data_estimada = data + timedelta(days = 1)
                    lista_datas.pop(k+1)
                    lista_datas.insert(k+1, data_estimada)
                    k = -1
                if (type(lista_datas[k]) is not str):
                    data_temp = lista_datas[k].strftime('%d/%m/%y')
                    lista_datas.pop(k)
                    lista_datas.insert(k, data_temp)
            k += 1

        cont = 0
        for i in cell_list:
            sub_dict = {"Horario que acordou": linhas_convertidas[cont][2], "Academia": linhas_convertidas[cont][3], "Litros agua" : linhas_convertidas[cont][4], "Refeicoes": linhas_convertidas[cont][5], "horario cama" : linhas_convertidas[cont][6]}
            dict_dados[lista_datas[cont]] = sub_dict
            cont += 1

        return dict_dados, caminho_json
        

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
                     "8 - Manipulação de dados\n" \
                     "9 - Converte dados\n" \
                     "10 - Transfere dados para lista\n" \
                     "0 - Sair: \n"))
    
    worksheet_gspread = planilhas.abrir_planilha()
    dados_bernardo = None
    dados_jessyka = None
    linhas_convertidas_bernardo = None
    linhas_convertidas_jessyka = None
    parametros_geral = 1
    parametros_bernardo = 2
    parametros_jessyka = 3
    parametros_int_bernardo = 4
    parametros_int_jessyka = 5
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
                dict_dados = planilhas.separa_dados(worksheet_gspread)
            md.manipulacao_dados.converte_df(dict_dados, worksheet_gspread)
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
        elif menu == 9:
            linhas_convertidas_bernardo, cell_list_bernardo = planilhas.transfere_dados_para_lista(worksheet_gspread = worksheet_gspread, parametro_json = 2)
            linhas_convertidas_jessyka, cell_list_jessyka = planilhas.transfere_dados_para_lista(worksheet_gspread = worksheet_gspread, parametro_json = parametros_jessyka)
            if(parametros_bernardo):
                dict_dados_bernardo, caminho_json = planilhas.converte_dados(linhas_convertidas = linhas_convertidas_bernardo, cell_list =  cell_list_bernardo, parametro_json = parametros_bernardo)
                planilhas.guarda_dict_json(dict_dados_bernardo, caminho_json)

            if (parametros_int_bernardo):
                dict_dados_int_bernardo, caminho_json = planilhas.converte_dados(linhas_convertidas = linhas_convertidas_bernardo, cell_list = cell_list_bernardo, parametro_json = parametros_int_bernardo)
                planilhas.guarda_dict_json(dict_dados_int_bernardo, caminho_json)

            if (parametros_jessyka):
                dict_dados_jessyka, caminho_json = planilhas.converte_dados(linhas_convertidas = linhas_convertidas_jessyka, cell_list = cell_list_jessyka, parametro_json = parametros_jessyka)
                planilhas.guarda_dict_json(dict_dados_jessyka, caminho_json)

            if(parametros_int_jessyka):
                dict_dados_int_jessyka, caminho_json = planilhas.converte_dados(linhas_convertidas = linhas_convertidas_jessyka, cell_list = cell_list_jessyka, parametro_json = parametros_int_jessyka)
                planilhas.guarda_dict_json(dict_dados_int_jessyka, caminho_json)
            break

        elif menu == 10:
            planilhas.transfere_dados_para_lista(worksheet_gspread = worksheet_gspread, parametro_json = 2)
    


  
    

    



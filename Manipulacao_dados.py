import Planilhas as pl
import pandas as pd
import matplotlib as plt

class manipulacao_dados():

    def converte_df(dict_dados_bernardo = None, dict_dados_jessyka = None, worksheet_gspread = None):
        if dict_dados_bernardo is None or dict_dados_jessyka is None or worksheet_gspread is None:
            dict_dados_bernardo, dict_dados_jessyka, worksheet_gspread = pl.planilhas.separa_dados() 
        dataframe = pd.DataFrame(worksheet_gspread.get_all_records())
        print("Planilha convertida em dataframe!")

        dataframe_bernardo = pd.DataFrame(dict_dados_bernardo)
        print(dataframe_bernardo)

        dataframe_jessyka = pd.DataFrame(dict_dados_jessyka) 
        print(dataframe_jessyka)

        return dataframe_bernardo, dataframe_jessyka
    
    def escolhe_comparacao(opcao, dataframe_bernardo = None, dataframe_jessyka = None):
        if dataframe_bernardo is None or dataframe_jessyka is None:
            dataframe_bernardo, dataframe_jessyka = manipulacao_dados.converte_df()
        
        if opcao == 1:
            return dataframe_bernardo[0:1], dataframe_jessyka[0:1]
        elif opcao == 2:
            return dataframe_bernardo[1:2], dataframe_jessyka[1:2]
        elif opcao == 3:
            return dataframe_bernardo[2:3], dataframe_jessyka[2:3]
        elif opcao == 4:
            return dataframe_bernardo[3:4], dataframe_jessyka[3:4]
        elif opcao == 5:
            return dataframe_bernardo[4:5], dataframe_jessyka[4:5]
        elif opcao == 6:
            return dataframe_bernardo[5:6], dataframe_jessyka[5:6]

    def compara_dados(dict_dados_bernardo = None, dict_dados_jessyka = None, worksheet_gspread = None):
        if dict_dados_bernardo is None:
            dict_return_bernardo, caminho_json_bernardo = pl.planilhas.escolher_json(2)
            dict_dados_bernardo = pl.planilhas.carrega_dict(dict_return_bernardo, caminho_json_bernardo)
            dict_return_jessyka, caminho_json_jessyka = pl.planilhas.escolher_json(3)
            dict_dados_jessyka = pl.planilhas.carrega_dict(dict_return_jessyka, caminho_json_jessyka)
        cont_chave = 0
        for chave in dict_dados_bernardo["Dia 1"]:
            cont_chave += 1
            print(f"{cont_chave} - {chave}")

        opcao = int(input("Insira o número referente a comparação que deseja fazer ou 0 para comparar todas: "))
        
        dataframe_bernardo, dataframe_jessyka = manipulacao_dados.converte_df(dict_dados_bernardo, dict_dados_jessyka, worksheet_gspread)

        if opcao == 0:
            i = 1
            # Refazer essa logica
            while i < 7:
                dataframe_bernardo_fracionado, dataframe_jessyka_fracionado = manipulacao_dados.escolhe_comparacao(i, dataframe_bernardo, dataframe_jessyka)
                df_comparacao_1 = pd.concat([dataframe_bernardo_fracionado, dataframe_jessyka_fracionado],  axis = 0, keys = ["Bernardo", "Jessyka"])

                dataframe_bernardo_fracionado, dataframe_jessyka_fracionado = manipulacao_dados.escolhe_comparacao(i + 1, dataframe_bernardo, dataframe_jessyka)
                df_comparacao_2 = pd.concat([dataframe_bernardo_fracionado, dataframe_jessyka_fracionado], axis = 0, keys = ["Bernardo", "Jessyka"])

                df_comparacao = pd.concat([df_comparacao_1, df_comparacao_2], axis = 0)
                print (df_comparacao)

                df_comparacao_1 = None
                df_comparacao_2 = None
                i += 1

        elif opcao == 1:
            dataframe_bernardo_fracionado, dataframe_jessyka_fracionado = manipulacao_dados.escolhe_comparacao(opcao, dataframe_bernardo, dataframe_jessyka)
            df_comparacao = pd.concat([dataframe_bernardo_fracionado, dataframe_jessyka_fracionado], axis = 0, keys= ["Bernardo", "Jessyka"])
            print(df_comparacao)
        elif opcao == 2:
            dataframe_bernardo_fracionado, dataframe_jessyka_fracionado = manipulacao_dados.escolhe_comparacao(opcao, dataframe_bernardo, dataframe_jessyka)
            df_comparacao = pd.concat([dataframe_bernardo_fracionado, dataframe_jessyka_fracionado], axis = 0, keys = ["Bernardo", "Jessyka"])
            print(df_comparacao)
        elif opcao == 3:
            dataframe_bernardo_fracionado, dataframe_jessyka_fracionado = manipulacao_dados.escolhe_comparacao(opcao, dataframe_bernardo, dataframe_jessyka)
            df_comparacao = pd.concat([dataframe_bernardo_fracionado, dataframe_jessyka_fracionado], axis = 0, keys = ["Bernardo", "Jessyka"])
            print(df_comparacao)
        elif opcao == 4:
            dataframe_bernardo_fracionado, dataframe_jessyka_fracionado = manipulacao_dados.escolhe_comparacao(opcao, dataframe_bernardo, dataframe_jessyka)
            df_comparacao = pd.concat([dataframe_bernardo_fracionado, dataframe_jessyka_fracionado], axis = 0, keys = ["Bernardo", "Jessyka"])
            print(df_comparacao)
        elif opcao == 5:
            dataframe_bernardo_fracionado, dataframe_jessyka_fracionado = manipulacao_dados.escolhe_comparacao(opcao, dataframe_bernardo, dataframe_jessyka)
            df_comparacao = pd.concat([dataframe_bernardo_fracionado, dataframe_jessyka_fracionado], axis = 0, keys = ["Bernardo", "Jessyka"])
            print(df_comparacao)
        elif opcao == 6:
            dataframe_bernardo_fracionado, dataframe_jessyka_fracionado = manipulacao_dados.escolhe_comparacao(opcao, dataframe_bernardo, dataframe_jessyka)
            df_comparacao = pd.concat([dataframe_bernardo_fracionado, dataframe_jessyka_fracionado], axis = 0, keys = ["Bernardo", "Jessyka"])
            print(df_comparacao)
        
        


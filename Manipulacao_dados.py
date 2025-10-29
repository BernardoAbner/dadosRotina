import Planilhas as pl
import pandas as pd
import matplotlib as plt



class manipulacao_dados():

    def converte_df(dict_dados = None):
        if dict_dados is None:
            dict_dados = pl.planilhas.converte_dados()
        dataframe = pd.DataFrame(dict_dados)
        print(dataframe)
        print("Planilha convertida em dataframe!")

        return dataframe
    
    def compara_df(opcao = None, dict_dados = None, dataframe_bernardo = None, dataframe_jessyka = None):
        if dataframe_bernardo == None or dataframe_jessyka == None:
            dataframe_bernardo = manipulacao_dados.converte_df()
            dataframe_jessyka = manipulacao_dados.converte_df()
    
        if (opcao is None):
            opcao = int(input("Insira o número referente a comparação que deseja fazer ou 0 para comparar todas: "))
            for chave in dict_dados["Dia 1"]:
                cont_chave += 1
                print(f"{cont_chave} - {chave}")

        cont = 0
        while (cont < 7):
            if (opcao == cont + 1):
                dataframe_bernardo_fatiado =  dataframe_bernardo[cont:cont + 1]
                dataframe_jessyka_fatiado = dataframe_jessyka[cont:cont +1]
                cont = 7
            print(f" Dataframe Bernardo: {dataframe_bernardo[cont:cont + 1]} \n Dataframe Jessyka: {dataframe_jessyka[cont:cont + 1]}")
            cont +=1

            if opcao == 0:
                lista_dataframes = []

                i = 1
                while i < 7:
                    df_comparacao_aux = pd.concat([dataframe_bernardo_fatiado, dataframe_jessyka_fatiado], axis = 0, keys = ["Bernardo", "Jessyka"])
                    lista_dataframes.append(df_comparacao_aux)
                    i += 1
                df_comparacao = pd.concat(lista_dataframes, axis = 0)
                print(df_comparacao)
                return df_comparacao
            
            elif (opcao > 0  and opcao < 7):
                df_comparacao = pd.concat([dataframe_bernardo_fatiado, dataframe_jessyka_fatiado], axis = 0, kesy = ["Bernardo", "Jessyka"])
                print(df_comparacao)
                return df_comparacao

    def cria_grafico():
        dataframe = manipulacao_dados.compara_dados()
        
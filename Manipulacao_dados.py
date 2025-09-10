import Planilhas as pl
import pandas as pd
import matplotlib as plt

class manipulacao_dados():

    def converte_df():
        
        dict_dados_bernardo, dict_dados_jessyka, worksheet_gspread  = pl.planilhas.separa_dados() 
        dataframe = pd.DataFrame(worksheet_gspread.get_all_records())
        print("Planilha convertida em dataframe!")

        dataframe_bernardo = pd.DataFrame(dict_dados_bernardo)
        print(dataframe_bernardo)

        dataframe_jessyka = pd.DataFrame(dict_dados_jessyka) 
        print(dataframe_jessyka)

        return dataframe, dataframe_bernardo, dataframe_jessyka
    
    def escolhe_comparacao():
        dataframe, dataframe_bernardo, dataframe_jessyka = manipulacao_dados.converte_df()

        cont_head = 0
        for coluna in dataframe.head():
            cont_head += 1
            print(f"{cont_head} - {coluna}")

        opcao = int(input("Insira o número referente a comparação que deseja fazer: "))
        
        if opcao == 1:
            print(dataframe_bernardo[1:2])
            return dataframe_bernardo[1:2], dataframe_jessyka[1:2]
        
        elif opcao == 2:
            print(dataframe_bernardo[2:3])
            return dataframe_bernardo[2:3], dataframe_jessyka[2:3]
        
        elif opcao == 3:
            print(dataframe_bernardo[3:4])
            return dataframe_bernardo[3:4], dataframe_jessyka[3:4]
        elif opcao == 4:
            print(dataframe_bernardo[4:5])
            return dataframe_bernardo[4:5], dataframe_jessyka[4,5]
        elif opcao == 5:
            print(dataframe_bernardo[5:6])
            return dataframe_bernardo[5:6], dataframe_jessyka[5:6]

    def compara_dados():
            
        


        opcao = 0


        
        
        '''df_comparacao_horario_acordou = pd.concat([dataframe_bernardo[1:2], dataframe_jessyka[1:2]], axis = 0, keys = ["Bernardo", "Jessyka"])
        print(df_comparacao_horario_acordou)'''
    

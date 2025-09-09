import Planilhas as pl
import pandas as pd



class manipulacao_dados():
    def converte_df():
        
        worksheet_gspread = pl.planilhas.abrir_planilha()
        dataframe = pd.DataFrame(worksheet_gspread.get_all_records())
        print("Planilha convertida em dataframe!")

        dict_dados_bernardo, dict_dados_jessyka = pl.planilhas.separa_dados()
        dataframe_bernardo  = pd.DataFrame(dict_dados_bernardo.get_all_records())
        print(dataframe_bernardo)

        dataframe_jessyka = pd.DataFrame(dict_dados_jessyka.get_all_records())
        print(dataframe_jessyka)
        print(dataframe) 




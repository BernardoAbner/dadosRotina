import Planilhas as pl
import pandas as pd

# Descobrir se tem como fazer sheet 2 e se caso tiver como, descobrir como passar dados da planilha geral para as especificas

class manipulacao_dados():
    def converte_df():
        
        worksheet_gspread = pl.planilhas.abrir_planilha()
        dataframe = pd.DataFrame(worksheet_gspread.get_all_records())
        print("Planilha convertida em dataframe!")
        print(dataframe) 




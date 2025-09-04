import Planilhas as pl
import pandas as pd

# Descobrir se tem como fazer sheet 2 e se caso tiver como, descobrir como passar dados da planilha geral para as especificas

class manipulacao_dados():
    def converte_df():
        worksheet_gspread = pl.planilhas.abrir_planilha()
        dataframe = pd.DataFrame(worksheet_gspread.get_all_records())
        print("Planilha convertida em dataframe!")
        print(dataframe) 

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


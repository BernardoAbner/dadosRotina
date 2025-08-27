import gspread
import pandas as pd


class planilhas():
    def carregar_planilha():
        gc = gspread.oauth()
        sheet = gc.open('dados-habitos')
        sheet.share('leitor-de-planilhas@dotted-signer-438321-m8.iam.gserviceaccount.com', perm_type = 'user', role = 'writer')
        worksheet = sheet.sheet1
        print ("Planilha compartilhada!")

        return gc, worksheet

    def criar_planilhas(self, gc):
        sheet_bernardo = gc.create("dados-bernardo")
        sheet_bernardo.share('leitor-de-planilhas@dotted-signer-438321-m8.iam.gserviceaccount.com', perm_type = 'user', role = 'writer')
        #sheet_bernardo.share('bernardoabnerwsp@gmail.com', perm_type = 'user', role = 'writer')
        worksheet_bernardo = sheet_bernardo.sheet1
        print("A planilha do Bernardo foi criada!")

        sheet_jessyka = gc.create("dados-jessyka")
        sheet_jessyka.share('leitor-de-planilhas@dotted-signer-438321-m8.iam.gserviceaccount.com', perm_type = 'user', role = 'writer')
        #sheet_jessyka.share('bernardoabnerwsp@gmail.com', perm_type = 'user', role = 'writer')
        worksheet_jessyka = sheet_jessyka.sheet1
        print("A planilha da Jessyka foi criada")
        print("Lendo dados...")

        return sheet_bernardo, worksheet_bernardo, sheet_jessyka, worksheet_jessyka
    

class manipulacao_dados():
    def converte_df():
        dataframe = pd.DataFrame(planilhas.carregando_planilha().worksheet.get_all_records())
        print("Planilha convertida em dataframe!")
        print(dataframe)

    def separacao_dados():
        coluna_usuario = planilhas.carregando_planilha().worksheet.row_values()
        for usuario in coluna_usuario:
            if usuario == "Bernardo":
                print("O usuário é o bernardo")
            elif usuario == "Jessyka":
                print("O usuário é a jessyka")


if __name__ == "__main__":
    planilhas.carregar_planilha()
    planilhas.criar_planilhas()
    manipulacao_dados.converte_df()
    manipulacao_dados.separacao_dados()

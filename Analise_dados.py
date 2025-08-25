import gspread
import pandas as pd

def carregando_planilha():
    gc = gspread.service_account(filename = "dotted-signer-438321-m8-336644ba4ca7.json")
    sheet = gc.open("dados-habitos")
    print ("Planilha carregada com sucesso!")

    sheet.share('eitor-de-planilhas@dotted-signer-438321-m8.iam.gserviceaccount.com', perm_type = 'user', role = 'writer')
    worksheet = sheet.sheet1

    sheet_bernardo = gc.create("dados-bernardo")
    sheet_bernardo.share('eitor-de-planilhas@dotted-signer-438321-m8.iam.gserviceaccount.com', perm_type = 'user', role = 'writer')
    sheet_bernardo.share('bernardoabnerwsp@gmail.com', perm_type = 'user', role = 'writer')
    worksheet_bernardo = sheet_bernardo.sheet1
    print("A planilha do Bernardo foi criada!")

    sheet_jessyka = gc.create("dados-jessyka")
    sheet_jessyka.share('eitor-de-planilhas@dotted-signer-438321-m8.iam.gserviceaccount.com', perm_type = 'user', role = 'writer')
    sheet_jessyka.share('bernardoabnerwsp@gmail.com', perm_type = 'user', roler = 'writer')
    worksheet_jessyka = sheet_jessyka.sheet1

    print("Lendo dados...")

    dataframe = pd.DataFrame(worksheet.get_all_records())
    print("Planilha convertida em dataframe!")
    print(dataframe)

    def manipulando_planilha():
        coluna_usuario = worksheet.row_values()
        for usuario in coluna_usuario:
            if usuario == "Bernardo":
                print("O usuário é o bernardo")


if __name__ == "__main__":
    carregando_planilha()

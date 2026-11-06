import gspread

gc = gspread.service_account(filename="./google-service-account-credentials.json")
ss = gc.open("test")
print(ss.worksheets())
ws = ss.worksheet("Hoja 1")
print(ws.col_values(2))

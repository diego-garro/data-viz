import gspread

gc = gspread.service_account(filename="./data-visualization-505105-19331e0eaa9d.json")
ss = gc.open("test")
print(ss.worksheets())
ws = ss.worksheet("Hoja 1")
print(ws.col_values(2))

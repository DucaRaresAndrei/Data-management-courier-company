import pyodbc

string_de_conectare = r"driver={SQL SERVER}; server=DESKTOP-FA5P09O\SQLEXPRESS; database=BD_Proiect; trusted_connection=YES"
conectare = pyodbc.connect(string_de_conectare)
cursor = conectare.cursor()
sql_res = cursor.execute("SELECT * FROM ConturiAdministratori")
sql_res = cursor.fetchone()

print(sql_res)

conectare.close()
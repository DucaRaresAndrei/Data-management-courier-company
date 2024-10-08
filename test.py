import pyodbc


# connect with daatbase
string_de_conectare = r"driver={SQL SERVER}; server=DESKTOP-FA5P09O\SQLEXPRESS; database=BD_Proiect; trusted_connection=YES"
conectare = pyodbc.connect(string_de_conectare)
cursor = conectare.cursor()

# # INSERARE COLET
# c_id = 1
# l_id = 3
# den = "mancare"
# g = 10
# c = 100
# dataE = "2011-02-14"
# dataL = "2011-03-14"
# plata = "Card"
# dim = "10, 10, 10"
# cod = "29265"
#
# cursor.execute("INSERT INTO Colet(CurierID, LocalizareID, Denumire, Greutate, Cost, DataExpedierii, "
#                "DataLivrarii, ModalitatePlata, Dimensiuni, Cod) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", c_id,
#                l_id, den, g, c, dataE, dataL, plata, dim, cod)
# cursor.commit()
# cursor.execute("SELECT @@IDENTITY AS colet_id")
# colet_id = cursor.fetchone()[0]

# # INSERARE EXPEDITOR
# exp_n = "Babadlasa"
# exp_p = "Anddrei"
# exp_cnp = "1242586945834"
# exp_comp = "SRL Furtuna"
# exp_add = "Str Jfhfur"
# exp_Localitate = "Onesti"
# exp_Judet = "Bacau"
# exp_tara = "Romania"
# exp_codp = "601340"
# exp_tel = "0764847384"
# exp_tip = "Expeditor"
#
# cursor.execute("INSERT INTO Clienti(Nume, Prenume, CNP, Companie, Adresa, Localitate,"
#                " Judet, Tara, CodPostal, Telefon, TipClient) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", exp_n,
#                exp_p, exp_cnp, exp_comp, exp_add, exp_Localitate, exp_Judet, exp_tara, exp_codp,
#                exp_tel, exp_tip)
# cursor.commit()
# cursor.execute("SELECT @@IDENTITY AS expeditor_id")
# expeditor_id = cursor.fetchone()[0]
#
# dest_n = "Bibuin"
# dest_p = "Andrei"
# dest_cnp = "1222586945834"
# dest_comp = "SRL Furtuna"
# dest_add = "Str Jfhfur"
# dest_Localitate = "Onesti"
# dest_Judet = "Bacau"
# dest_tara = "Romania"
# dest_codp = "603140"
# dest_tel = "0764867384"
# dest_tip = "Destinatar"
#
# # INSERARE DESTINATAR
# cursor.execute("INSERT INTO Clienti(Nume, Prenume, CNP, Companie, Adresa, Localitate,"
#                " Judet, Tara, CodPostal, Telefon, TipClient) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", dest_n,
#                dest_p, dest_cnp, dest_comp, dest_add, dest_Localitate, dest_Judet, dest_tara, dest_codp,
#                dest_tel, dest_tip)
# cursor.commit()
# cursor.execute("SELECT @@IDENTITY AS destinatar_id")
# destinatar_id = cursor.fetchone()[0]
#
# count = 0
# cursor.execute("SELECT * FROM ClientiColete")
# for row in cursor.fetchall():
#     if colet_id == row[0]:
#         count += 1
#
# if count == 0:
#     cursor.execute("INSERT INTO ClientiColete(ColetID, ClientID) VALUES (?, ?)", colet_id, expeditor_id)
#     cursor.commit()
#     cursor.execute("INSERT INTO ClientiColete(ColetID, ClientID) VALUES (?, ?)", colet_id, destinatar_id)
#     cursor.commit()
#
# print(colet_id)
# print(expeditor_id)
# print(destinatar_id)

# colet_cod = 50001
# colet_den = "PC"
#
# cursor.execute("SELECT Col.ColetID, Col.Denumire, Col.Cod, C.Nume + ' ' + C.Prenume AS Curier, Exped.Nume + ' ' +"
#                " Exped.Prenume AS Expeditor FROM Colet Col INNER JOIN Curieri C ON Col.CurierID = C.CurierID "
#                "INNER JOIN ClientiColete CC ON Col.ColetID = CC.ColetID "
#                "INNER JOIN Clienti Exped ON CC.ClientID = Exped.ClientID AND Exped.TipClient = 'Expeditor' "
#                "WHERE Col.Cod = ? AND Col.Denumire = ?", colet_cod, colet_den)
#
# expeditori = []
# for row in cursor.fetchall():
#         expeditori.append(row)
#
# cursor.execute("SELECT Col.ColetID, Col.Denumire, Dest.Nume + ' ' + Dest.Prenume AS Destinatar FROM Colet Col "
#                "INNER JOIN ClientiColete CC ON Col.ColetID = CC.ColetID "
#                "INNER JOIN Clienti Dest ON CC.ClientID = Dest.ClientID AND Dest.TipClient = 'Destinatar'"
#                "WHERE Col.Cod = ? AND Col.Denumire = ?", colet_cod, colet_den)
# destinatari = []
# for row in cursor.fetchall():
#     destinatari.append(row)
#
# for i in range(len(destinatari)):
#     print(f"Colet(Denumire & Cod): {expeditori[i][1]} {expeditori[i][2]} \nCurier: {expeditori[i][3]}\n"
#           f"Expeditor: {expeditori[i][4]}\nDestinatar: {destinatari[i][2]}")

# year = 2021
#
# cursor.execute("SELECT C.Nume + ' ' + C.Prenume AS Curier, COUNT(Col.ColetID) AS NumarColete FROM Curieri C LEFT JOIN Colet Col ON C.CurierID = Col.CurierID "
#                "GROUP BY C.CurierID, C.Nume, C.Prenume "
#                "HAVING COUNT(Col.ColetID) = (SELECT TOP 1 COUNT(Col.ColetID) FROM Colet Col2 GROUP BY Col2.DataLivrarii  "
#                "HAVING YEAR(Col2.DataLivrarii) BETWEEN ? AND GETDATE() ORDER BY COUNT(Col.ColetID) DESC)", year)
# row = cursor.fetchall()
# print(row)

# close connection
conectare.close()

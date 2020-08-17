import mysql.connector


def insertVariblesIntoTable(denomination, raison_sociale, responsable, activites, produits, adresse_usine, gouvernorat, delegation, telephone_siege_usine, fax_siege_usine, email, URL, regime, pays_du_participant_etranger, entree_en_production, capital_en_DT, emploi):
    try:      # BD connection

        mydb = mysql.connector.connect(host='localhost',
                                             database='annuaire',
                                             user='nesrine',
                                             password='aei321')
        cursor = mydb.cursor()
        # create query
        mysql_insert_query = """ INSERT INTO profil ( denomination, raison_sociale, responsable, activites, produits, adresse_usine, gouvernorat, delegation, telephone_siege_usine, fax_siege_usine, email, URL, regime, pays_du_participant_etranger, entree_en_production, capital_en_DT, emploi)
         VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s,%s, %s,%s, %s,%s, %s) """

        recordtuple = (denomination, raison_sociale, responsable, activites, produits, adresse_usine, gouvernorat, delegation, telephone_siege_usine, fax_siege_usine, email, URL, regime, pays_du_participant_etranger, entree_en_production, capital_en_DT, emploi)
        cursor.execute(mysql_insert_query, recordtuple)
        mydb.commit()
        print("Record inserted successfully into Laptop table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if (mydb.is_connected()):
            cursor.close()
            mydb.close()
            print("MySQL connection is closed")



insertVariblesIntoTable('ABDENNADHER DESIGN', 'ABDENNADHER DESIGN', 'Habib Abdennadher', 'Sièges - Meubles de Bureau et Magasin.', "Bureaux - Autres meubles de bureau et de magasin - Sièges d'ameublement.", "RTE C 39 LOTISSEMENT ABDI KHODJA - 2097 - BOUM'HAL", 'Ben Arous', 'Boumhal', '(216) - 71 216 020 / 71 433 375', '(216) - 71 216 040', 'a.design@gnet.tn', 'http://www.a-design.com.tn', 'Non totalement exportatrice', '', '01/06/2004', '1\xa0127\xa0000', '60')
# insertVariblesIntoTable(3, 'MacBook Pro', 2499, '2019-06-20')


"""
for d in range(185):
  sql = "INSERT INTO profil ( Dénomination, Raison Sociale,Responsable,Activités,Produits,Adresse usine,Gouvernorat,Délégation,Téléphone siège/usine,Fax siège/usine,E-mail,URL,Régime,Pays du Participant Etranger,Entrée en production,Capital en DT,Emploi) VALUES (%s, %s)"


"""

"""
 <table>
 	<tr>
 		<th>Denomination</th> 		
 		<th>Raison sociale</th>
 		<th>responsable</th>
 		<th>Activités</th>
 		<th>Produits</th>
 		<th>Adresse usine</th>
 		<th>Gouvernorat</th>
 		<th>Délégation</th>
 		<th>Téléphone siège/usine</th>
 		<th>Fax siège/usine</th>
 		<th>Email</th>
 		<th>URL</th>
 		<th>Régime</th>
 		<th>Pays du participant étranger</th>
 		<th>Entrée en production</th>
 		<th>Capital en DT</th>
 		<th>Emploi</th>

 	</tr>
 	<tr *ngFor="let element of liste">
     <td>{{element.denomination}}</td>
     <td>{{element.raison_sociale}}</td>
 		<td>{{element.responsable}}</td>
 		<td>{{element.activites}}</td>
 		<td>{{element.produits}}</td>
 		<td>{{element.adresse_usine}}</td>
 		<td>{{element.gouvernorat}}</td>
 		<td>{{element.delegation}}</td>
 		<td>{{element.telephone_siege_usine}}</td>
 		<td>{{element.fax_siege_usine}}</td>
 		<td>{{element.email}}</td>
 		<td>{{element.URL}}</td>
 		<td>{{element.regime}}</td>
 		<td>{{element.pays_du_participant_etranger}}</td>
 		<td>{{element.entree_en_production}}</td>
 		<td>{{element.capital_en_DT}}</td>
 		<td>{{element.emploi}}</td>


 	</tr>
 </table>   """
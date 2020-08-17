import requests
from datetime import datetime
from bs4 import BeautifulSoup
import mysql.connector

# insertion to database
def insertVariblesIntoTable(id, denomination, raison_sociale, responsable, activites, produits, adresse_usine, gouvernorat, delegation, telephone_siege_usine, fax_siege_usine, email, URL, regime, pays_du_participant_etranger, entree_en_production, capital_en_DT, emploi):
    try:      # BD connection
        mydb = mysql.connector.connect(host='localhost',
                                         database='annuaire',
                                         user='nesrine',
                                         password='aei321')
        cursor = mydb.cursor()
        # create query
        mysql_insert_query = """ INSERT INTO profil ( id, denomination, raison_sociale, responsable, activites, produits, adresse_usine, gouvernorat, delegation, telephone_siege_usine, fax_siege_usine, email, URL, regime, pays_du_participant_etranger, entree_en_production, capital_en_DT, emploi)
         VALUES (%s, %s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s,%s, %s,%s, %s,%s, %s) """
        values = (id, denomination, raison_sociale, responsable, activites, produits, adresse_usine, gouvernorat, delegation, telephone_siege_usine, fax_siege_usine, email, URL, regime, pays_du_participant_etranger, entree_en_production, capital_en_DT, emploi)
        cursor.execute(mysql_insert_query, values)
        mydb.commit()
        print("Record inserted successfully into Laptop table")
    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))
    finally:
        if (mydb.is_connected()):
            cursor.close()
            mydb.close()
            print("MySQL connection is closed")

 # extract id from onclick of every Etse
def ident(list):
    for i in range(len(list)):
        j = 0
        if list[i] != None:
            while list[i][j] != "'":
                j = j + 1
            list[i] = list[i][j + 29:len(list[i]) - 1]


def extract_data(mylist):
    for i in range(len(mylist)):
        j = 0
        if mylist[i] != None:
            while mylist[i][j] != ">":
                j = j + 1
            if mylist[i].find('a href=""') != -1 or mylist[i].find('a href="mailto:">') != -1:
                mylist[i] = ""
            elif mylist[i].find('mailto:') != -1:
                if mylist[i].find('.com.tn') != -1:
                    mylist[i] = mylist[i][mylist[i].find('mailto:') + 7: mylist[i].find('.com.tn"') + 7]
                elif mylist[i].find('.tn') != -1:
                    mylist[i] = mylist[i][mylist[i].find('mailto:') + 7: mylist[i].find('.tn"') + 3]
                elif mylist[i].find('.fr') != -1:
                    mylist[i] = mylist[i][mylist[i].find('mailto:') + 7: mylist[i].find('.fr"') + 3]
                elif mylist[i].find('.com') != -1:
                    mylist[i] = mylist[i] = mylist[i][mylist[i].find('mailto:') + 7: mylist[i].find('.com"') + 4]
                elif mylist[i].find('.it') != -1:
                    mylist[i] = mylist[i] = mylist[i][mylist[i].find('mailto:') + 7: mylist[i].find('.it"') + 3]
                elif mylist[i].find('.biz') != -1:
                    mylist[i] = mylist[i] = mylist[i][mylist[i].find('mailto:') + 7: mylist[i].find('.biz"') + 4]
            elif mylist[i].find('http') != -1:
                if mylist[i].find('.tn') != -1:
                    mylist[i] = mylist[i][mylist[i].find('http') + 7: mylist[i].find('.tn"') + 3]
                elif mylist[i].find('.com') != -1:
                    mylist[i] = mylist[i][mylist[i].find('http') + 7: mylist[i].find('.com"') + 4]
                elif mylist[i].find('.net') != -1:
                    mylist[i] = mylist[i][mylist[i].find('http') + 7: mylist[i].find('.net"') + 4]
            else:
                mylist[i] = mylist[i][j + 1:len(mylist[i]) - 6]

# access urls from form to page having Etse
with requests.Session() as s:
    # enter form with specified parameters
    r = s.get('http://www.tunisieindustrie.nat.tn/fr/dbi.asp?secteur=07&branche=&produit=&Denomination=&Gouvernorat=&delegation=&pays=&regime=&ent_prd=&cap1=&cap2=&emp1=&emp2=&action=search')
    links = []
    if r.ok:
        soup = BeautifulSoup(r.text, "html.parser")
        for link in soup.find_all('tr'):
            click = link.get('onclick')
            if click is None:
                continue
            links.append(click)  # add content of "onclick" to the list links only for the first page
    # the following code: consult all the pages and add content of onclisk to the same list "links"
    for i in range(6):
        url_next = "http://www.tunisieindustrie.nat.tn/fr/dbi.asp?action=search&pagenum="+str(i+2)
        rn = s.get(url_next)
        soup = BeautifulSoup(rn.text, "html.parser")
        for link in soup.find_all('tr'):
            click = link.get('onclick')
            if click is None:
                continue
            links.append(click)
    temp_links = links
    ident(temp_links)
    # print(temp_links)
# create links using ids extracted above then here is the final access to information of every enterprise
    for l in range(len(temp_links)):
        url_fin = "http://www.tunisieindustrie.nat.tn/fr/dbi.asp?action=result&ident=" + temp_links[l]
        rf = s.get(url_fin)
        soup = BeautifulSoup(rf.text, "html.parser")
        table = soup.find("table")
        data = []
        for link_f in table.find_all('tr'):
            var = link_f.find_all('td')
            data.append(str(var[1]))
        extract_data(data)
        # date_dt2 = datetime.strptime(data[14], '%d/%m/%Y')
        #insertVariblesIntoTable(l, data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12], data[13], data[14], data[15], data[16])
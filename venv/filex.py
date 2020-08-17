import requests
from bs4 import BeautifulSoup




def nbPage():
    data = []

    rows = soup.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])
    d = str(data[1])
    res = [int(s) for s in d.split() if s.isdigit()]
    i = res[1]
    return i
# access urls from form to page having Etse
with requests.Session() as s:
    # enter form with specified parameters
    r = s.get('http://www.tunisieindustrie.nat.tn/fr/dbi.asp?secteur=07&branche=&produit=&Denomination=&Gouvernorat=&delegation=&pays=&regime=&ent_prd=&cap1=&cap2=&emp1=&emp2=&action=search')
    links = []
    if r.ok:
        soup = BeautifulSoup(r.text, "html.parser")
        for link in soup.find_all('tr'):
            click = link.get('onclick')
        x = nbPage()
        print(x)
"""
  data = []
    table = soup.find('table', attrs={'class':'one'})
    table_body = table.find('tbody')

    rows = soup.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])
    print(data[1])
    d = str(data[1])
    print(type(d))
    res = [int(s) for s in d.split() if s.isdigit()]
    print(res)
    i = res[1]
    print(type(i))

"""

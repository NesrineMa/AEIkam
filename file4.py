import requests
from bs4 import BeautifulSoup



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
    # the following code: consult all the pages and add content of onclick to the same list "links"
    i = 0
    while True:
        url_next = "http://www.tunisieindustrie.nat.tn/fr/dbi.asp?action=search&pagenum="+str(i+2)
        rn = s.get(url_next)
        soup = BeautifulSoup(rn.text, "html.parser")
        for link in soup.find_all('tr'):
            click = link.get('onclick')
            if click is None:
                continue
            links.append(click)

    comment = soup.table.tr.td.b.string
    print(comment)
    temp_links = links

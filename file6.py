from bs4 import BeautifulSoup

markup = """
<table class="one" border="0">
  <tr>
    <td width="100%" class="tabtd"><b>185 Enregistrement(s) trouvé(s)</b></td>
  </tr>
  <tr>
    <td width="100%" class="tabtd">Page <b>2</b> de <b>7</b> Cliquer sur l'une des entreprises pour avoir plus de détails</td>
  </tr>  
</table>"""
soup = BeautifulSoup(markup,'html.parser')
comment = soup.table.tr.td.b.string
print(comment)

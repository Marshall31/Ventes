import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

qte = données['qte']
prix = données['prix']

figure = px.pie(données, values=qte, names='produit', title='ventes par produit')
figure2 = px.pie(données, values=qte*prix, names='produit', title='chiffre d\'affaires par produit')
#figure2 = px.pie(données, values='prix', names='produit', title='chiffre d\'affaires par produit')


figure.write_html('ventes-par-roduit.html')
figure2.write_html('chiffre-affaires-par-roduit.html')

print('ventes-et-chiffre-affaires-par-roduit.html généré avec succès !')

#a. les ventes par produit,
#b. le chiffre d'affaires par produit.
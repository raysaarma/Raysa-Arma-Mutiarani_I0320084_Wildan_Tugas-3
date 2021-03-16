#Dictionary

Biodata={'Nama':'Raysa Arma Mutiarani',
         'Hobi1':'Menonton',
         'Hobi2':'Memasak',
         'Hobi3':'Jogging',
         'Instagram':'raysaarmaa',
         'Twitter':'raysaarmaa',
         'Line':'reysoo',
         'Lagu Kesukaan1':'Dont wanna miss a thing',
         'Lagu Kesukaan2':'Yesterday',
         'Lagu Kesukaan3':'Grow old with you',
         'Makanan Favorit1':'Mie',
         'Makanan Favorit2':'Lalapan',
         'Makanan Favorit3':'Pecel'}
Biodata['Hobi2']= 'Makan'
Biodata['Line']= 'raysaarmaa'
del Biodata['Makanan Favorit1']
del Biodata['Makanan Favorit2']
Biodata2={'Hobi4':'Memasak'}
Biodata.update(Biodata2)
print(Biodata)
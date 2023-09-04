from PyQt5 import uic

with open('anaekranUI.py', 'w', encoding='utf-8') as fout:

    uic.compileUi('anaekran.ui',fout)


with open('rezervasyonUI.py', 'w', encoding='utf-8') as fout:

    uic.compileUi('OdaAramaUI.ui',fout)

with open('odalarUI.py', 'w', encoding='utf-8') as fout:

    uic.compileUi('odalar.ui',fout)

with open('odaBilgiUI.py', 'w', encoding='utf-8') as fout:

    uic.compileUi('odaBilgi.ui',fout)

with open('musteriEkleUI.py', 'w', encoding='utf-8') as fout:

    uic.compileUi('musteriEkle.ui',fout)

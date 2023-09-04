import openpyxl
import time
import xlsxwriter
import os 

def excel_oku(dosya_adi):
    # Excel dosyasını aç
    workbook = openpyxl.load_workbook(dosya_adi)
    
    # İlk çalışma sayfasını seç
    sheet = workbook.get_sheet_by_name("Allgemein_Liste")
    
    # Satırları ve başlıkları oku
    satirlar = []
    basliklar = []
    
    for row in sheet.iter_rows(max_col=10,max_row=481):
        satir = []
        
        for cell in row:
            satir.append(cell.value)
        
        # Başlıkları ayır
        if not basliklar:
            basliklar = satir
        else:
            satirlar.append(satir)

    # Dosyayı kapat
    workbook.close()
    
    return  satirlar

def addtodb(satirlar):
    import sqlite3
    liste=[]
    con=sqlite3.connect("database")
    curs=con.cursor()
    for satir in satirlar:
        if satir[4]==None and satir[5]==None and satir[6]==None:
            continue
        haus=satir[4]
        blok=satir[5]
        odaAdi=satir[6]+"- "+satir[7]
        sozluk={"EZ/D":1,"EZ":1,"DZ/D":2,"DZ":2,"DBZ":3,"DBZ/D":3,"VBZ":4,"VBZ/D":4,"FBZ":5,"FBZ/D":5}
        """EZ/D	1 kisilik dus ve wc li oda
EZ	1 kisilik oda1
DZ/D	2 kisilik dus ve wc li oda
DZ	2 kisilik oda
3BZ/D	3 kisilik dus ve wc li oda
3BZ	2 kisilik oda
4BZ/D	4 kisilik dus ve wc li oda
4BZ	4 kisilik oda
5BZ	5 kisilik oda"""
        kat=satir[3]
        try:kapasite=sozluk[satir[7]]
        except:continue
        print(haus,blok,odaAdi,kat)      
        curs.execute("SELECT * FROM odalar Where haus = ? and blok= ? and odaAdi= ?",(haus,blok,odaAdi))
        data=curs.fetchall()
        if len(data)!=0: liste.append(data)
        else:
            curs.execute("INSERT INTO odalar Values(?,?,?,?,?,?)",(haus,blok,odaAdi,kat,kapasite,0))
            con.commit()
    print(liste)

satirlar=excel_oku("Kopie von Belegungs für Jede TAGUNG(1).xlsx")
addtodb(satirlar)


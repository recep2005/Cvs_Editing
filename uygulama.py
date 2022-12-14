import csv

beforeCvs = input("Düzenlenecek Cvs Adı Nedir? ")
newVerdor=input("Yeni Vendor Ne Olsun?")
newVariant=input("Yeni Variant Inventory Tracker Ne Olsun?")
saveCvs= input("Yeni Dosya Adı Ne olsun? ")
rate=input("Artış Oranı Nedir? ")
       
with open(saveCvs+'_editing.csv', mode='w',newline='') as yeni_dosya:
    yeni_yazici = csv.writer(yeni_dosya)
    with open(beforeCvs+'.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count==0:
                line_count += 1
            else:
                if row[3]!="" and newVerdor!="":
                    row[3]=newVerdor
                if row[16]!="" and newVariant!="":
            
                    row[16]=newVariant


                if row[10]=="":

                    if row[20]!="":
                        row[20]=round(float(row[20])*(1+(float(rate)/100.00)),2)
                    if row[21]!="":
                        row[21]=round(float(row[21])*(1+(float(rate)/100.00)),2)
                else:
                    if row[22]!="":
                        row[22]=round(float(row[22])*(1+(float(rate)/100.00)),2)
                    if row[23]!="":
                        row[23]=round(float(row[23])*(1+(float(rate)/100.00)),2)                    


            yeni_yazici.writerow(row) 

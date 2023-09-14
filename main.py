import sqlite3
from tkinter import *
import random
import datetime

pencere = Tk()                              # pencere oluşturduk
pencere.configure(background='white')
pencere.title("Kütüphane Uygulaması")           # pencereye başlık verdik
pencere.geometry("1200x600")                #penceremize boyut verdik

kitap_txt_dosyasi = open("kitapbilgiler.txt","a",encoding="utf-8")
ogrenci_txt_dosyasi = open("Ödünç bilgileri.txt","a",encoding="utf-8")
#_____________________________________________________________________________________________________
# kitap tanıtım ve işlemlerinin yapılacağı sınıfi
class pencere_islemleri():
    def __init__(self):
        self.kitap_ekle_butonu
        self.odunc_ver_butonu

        self.başlık = Label(text="İşlem Seçiniz",fg = "red",font=("open sans","30","underline"),bg="white")
        self.başlık.place(x=470,y=50)             # ekranda gözükecek bir başlık oluşturduk ve yer verdik pencerede
        # BUTONLARIMIZI OLUŞTURUYORUZ 
        #----------------------------------------------------------------------------------------------------
        self.kitap_listeleme_sekmesi = Button(text="Kitapları Listele", command=self.kitap_listele_butonu, bg = "green",bd="20",font = ("Comic Sans MS", 10, "bold"))
        self.kitap_listeleme_sekmesi.place(x=415,y=150)
        #----------------------------------------------------------------------------------------------------
        self.odunc_ver_sekmesi = Button(text="Ödünç Ver", command=self.odunc_ver_butonu, bg = "green",bd="20",font = ("Comic Sans MS", 10, "bold"))
        self.odunc_ver_sekmesi.place(x=620,y=150)
        #-----------------------------------------------------------------------------------------------------
        self.iade_al_sekmesi = Button(text="İade Al", command=self.iade_al_butonu, bg = "green",bd="20",font = ("Comic Sans MS", 10, "bold"))
        self.iade_al_sekmesi.place(x=790,y=150)
        #-----------------------------------------------------------------------------------------------------
        self.cikis = Button(text="Çıkış Yap", command=self.cikis_yap, bg = "red",bd="20",font = ("Comic Sans MS", 10, "bold"))
        self.cikis.place(x=470,y=350)
        #----------------------------------------------------------------------------------------------------
        self.kitap_ekleme_sekmesi = Button(text="Kitap Ekle", command=self.kitap_ekle_butonu, bg = "green",bd="20", font = ("Comic Sans MS", 10, "bold"))
        self.kitap_ekleme_sekmesi.place(x=250,y=150)
        #----------------------------------------------------------------------------------------------------
        
    def kitap_ekle_butonu(self):
        self.başlık.destroy()
        self.kitap_ekleme_sekmesi.destroy()
        self.kitap_listeleme_sekmesi.destroy()
        self.odunc_ver_sekmesi.destroy()
        self.iade_al_sekmesi.destroy()
        self.cikis.destroy()

        self.baslik1 = Label(text = "Kitap Ekle",fg = "red",font=("open sans","30","underline"))
        self.baslik1.place(x=470,y=50)

        self.text1 = Label(text = "Kitap İsmi:",fg = "black",font=("open sans", "15","normal"))
        self.text1.place(x=315,y=150)

        self.text2 = Label(text = "Yazar:",fg = "black",font=("open sans", "15","normal"))
        self.text2.place(x=350,y=200)

        

        veri_eklemek_icin = veriTabanı()
        veri_eklemek_icin.kitap_bilgi_ekle()

    def odunc_ver_butonu(self):
        self.başlık.destroy()
        self.kitap_ekleme_sekmesi.destroy()
        self.kitap_listeleme_sekmesi.destroy()
        self.odunc_ver_sekmesi.destroy()
        self.iade_al_sekmesi.destroy()
        self.cikis.destroy()
        
        self.baslik1 = Label(text = "Ödünç Ver",fg = "red",font=("open sans","30","underline"))
        self.baslik1.place(x=470,y=50)

        self.text1 = Label(text = "Kitap İd:",fg = "black",font=("open sans", "15","normal"))
        self.text1.place(x=315,y=150)

        self.text2 = Label(text = "TC:",fg = "black",font=("open sans", "15","normal"))
        self.text2.place(x=350,y=200)

        

        veri_kaydetmek_icin = odunc_ver_sınıfı()
        veri_kaydetmek_icin.odunc_sayfasi()

    def iade_al_butonu(self):
        self.başlık.destroy()
        self.kitap_ekleme_sekmesi.destroy()
        self.kitap_listeleme_sekmesi.destroy()
        self.odunc_ver_sekmesi.destroy()
        self.iade_al_sekmesi.destroy()
        self.cikis.destroy()

        self.baslik1 = Label(text = "İade Al",fg = "red",font=("open sans","30","underline"))
        self.baslik1.place(x=470,y=50)

        self.text1 = Label(text = "Kitap İd:",fg = "black",font=("open sans", "15","normal"))
        self.text1.place(x=315,y=150)

        self.text2 = Label(text = "TC:",fg = "black",font=("open sans", "15","normal"))
        self.text2.place(x=350,y=200)

        self.text3 = Label(text = "Kitap İsmi:",fg = "black",font=("open sans", "15","normal"))
        self.text3.place(x=300,y=250)

        self.text3 = Label(text = "Yazar İsmi:",fg = "black",font=("open sans", "15","normal"))
        self.text3.place(x=300,y=300)

        

        iade_verisi_icin = iade_al_sinifi()
        iade_verisi_icin.iade_sayfasi()

    def kitap_listele_butonu(self):
        self.başlık.destroy()
        self.kitap_ekleme_sekmesi.destroy()
        self.kitap_listeleme_sekmesi.destroy()
        self.odunc_ver_sekmesi.destroy()
        self.iade_al_sekmesi.destroy()
        self.cikis.destroy()
        
        listeleme_icin = kitap_islemleri()
        listeleme_icin.kitap_listele()
        listeleme_icin.kitap_ara()

        

    def cikis_yap(self):
        pencere.destroy()

#_____________________________________________________________________________________________________
class veriTabanı():
    def __init__(self):
        self.con = sqlite3.connect("bilgiler.db")
        self.cursor = self.con.cursor()

        self.id = random.randint(1,100000000)

        

    def kitap_bilgi_ekle(self):
        self.giris1 = Entry(font=("Comic Sans MS", "15","normal"))
        self.giris1.place(x=420,y=150,width = 250, height = 30)

        self.giris2 = Entry(font=("Comic Sans MS", "15","normal"))
        self.giris2.place(x=420,y=200,width = 250, height = 30)

        def veri_kaydet():
            kitap_ismi_gir = self.giris1.get()
            yazar_gir = self.giris2.get()
            if kitap_ismi_gir == "" or yazar_gir == "":
                uyarı = Label(text = "Lütfen boş bırakmayınız!!",font=("Verdana 13 bold"),background="black",fg ="red")
                uyarı.place(x=400,y=400)
                
            else:
                uyarı = Label(text = "Başarılı bir şekilde kaydedildi!!",font=("Verdana 13 bold"),background="black",fg ="red")
                uyarı.place(x=400,y=400)
                
                self.cursor.execute("CREATE TABLE IF NOT EXISTS bilgiler (Kitapİsmi TEXT,Yazar TEXT,id INTEGER PRIMARY KEY)")
                self.con.commit()

                self.cursor.execute("INSERT INTO bilgiler (Kitapİsmi, Yazar, id) VALUES(?,?,?)",(kitap_ismi_gir, yazar_gir,self.id))
                self.con.commit()
                self.con.close()
                
                siralama_icin = kitap_islemleri()  #kompozisyon
                id_listesi = []
                id_listesi = siralama_icin.veri_sirala()
                print(id_listesi)


                kitap_txt_dosyasi.write("\n"+str(self.id))
                kitap_txt_dosyasi.write("/"+kitap_ismi_gir+"/")
                kitap_txt_dosyasi.write(yazar_gir)

        self.eklendi_butonu = Button(text="Kayıt Et",command=veri_kaydet,bg="red",bd="10")
        self.eklendi_butonu.place(x=500,y=250)

#----------------------------------------------------------------------------------------------------

class kitap_islemleri(veriTabanı,pencere_islemleri):
    #veritabanından listeler için gerekli bilgileri çek
    __id_listesi = []          #kapsülleme yaparak veriyi private yaptık
    kitap_bilgileri = []
    kitap_isimleri = []
    yazar_isimleri = []
    
    def __init__(self):
        kitap_txt_dosyasi = open("kitapbilgiler.txt","r",encoding="utf-8")
        self.tum_satirlar = kitap_txt_dosyasi.readlines()
        for i in range(len(self.tum_satirlar)):
            x=self.tum_satirlar[i].split("/")
            self.__id_listesi += [x[0]]
            self.kitap_bilgileri += [x[1]+" "+x[2]]
            self.kitap_isimleri += [x[1]]
            self.yazar_isimleri += [x[2]]
    
    def getIdlist(self):
        return self.__id_listesi
        
    def veri_sirala(self): #insertion sort
        for i in range(1,len(self.__id_listesi)):
            key = int(self.__id_listesi[i])
            j = i - 1

            while j >= 0 and key < int(self.__id_listesi[j]):
                self.__id_listesi[j+1] = self.__id_listesi[j]
                j -= 1
            self.__id_listesi[j+1] = key
        return self.__id_listesi


    def kitap_listele(self):
        Lb1 = Listbox(pencere,height=10,width=50,font="Times 20 bold",bd="7px",relief="groove",bg="green",fg="white")
        Lb1.place(x=100,y=100)
        a = 1
        
        
        for i in self.kitap_bilgileri:
            Lb1.insert(a, i)
            a+=1

        Lb1.pack()

    def kitap_ara(self):
        self.kitap_ara_entry = Entry(font=("Comic Sans MS", "15","normal"))
        self.kitap_ara_entry.place(x=420,y=450,width = 250, height = 30)

        def ara():
            if self.kitap_ara_entry.get() in self.kitap_isimleri:
                self.text1 = Label(text = "   Aradığınız kitap bulunmaktadır    ",fg = "white",bg="green",font=("open sans", "15","normal"))
                self.text1.place(x=341,y=390)

            else:
                self.text1 = Label(text = "Aradığınız kitap bulunmamaktadır!  ",fg = "white",bg="red",font=("open sans", "15","normal"))
                self.text1.place(x=340,y=390)

        self.ara_buton = Button(text="Ara",command=ara,bg="red",bd="10")
        self.ara_buton.place(x=520,y=500)

    

#----------------------------------------------------------------------------------------------------
class odunc_ver_sınıfı(kitap_islemleri):
    def __init__(self):
        super().__init__()
        self.tarih = "00.00.00"
        self.tc_liste = []
        self.id_liste2 = []

        self.id_listesi = self.getIdlist() #Kapsülleme yapılmış veriyi çekmek için bu metodu çağırdık
        
    def odunc_sayfasi(self):
        self.verilen_kitap_id = Entry(font=("Comic Sans MS", "15","normal"))
        self.verilen_kitap_id.place(x=420,y=150,width = 250, height = 30)

        self.kitap_alan_tc = Entry(font=("Comic Sans MS", "15","normal"))
        self.kitap_alan_tc.place(x=420,y=200,width = 250, height = 30)

        def odunc_ver():
            self.verilen_kitap_id = self.verilen_kitap_id.get()
            self.kitap_alan_tc = self.kitap_alan_tc.get()

            if self.verilen_kitap_id == "" or self.kitap_alan_tc == "":
                uyarı = Label(text = "Lütfen boş bırakmayınız!!",font=("Verdana 13 bold"),background="black",fg ="red")
                uyarı.place(x=400,y=400)
                
            else:
                uyarı = Label(text = "Başarılı bir ödünç verildi!!",font=("Verdana 13 bold"),background="black",fg ="red")
                uyarı.place(x=400,y=400)
                
                self.tarih = datetime.datetime.now()
                Tarih = str(self.tarih.day)+"."+str(self.tarih.month)+"."+str(self.tarih.year)
                
                uyarı2 = Label(text = str(Tarih)+" tarihinde ödünç verildi!",font=("Verdana 13 bold"),background="black",fg ="white")
                uyarı2.place(x=350,y=350)
                
                
                for i in range(len(self.id_listesi)):
                    #kitapbilgiler.txt 'den sil
                    if self.id_listesi[i] == self.verilen_kitap_id:
                        a = self.id_listesi[i]+"/"+self.kitap_isimleri[i]+"/"+self.yazar_isimleri[i]

                        with open("kitapbilgiler.txt", "r", encoding="utf-8") as f:
                            b = f.readlines()
                        with open("kitapbilgiler.txt", "w", encoding="utf-8") as f:
                            for c in b:
                                if c != a:
                                    f.write(c)


                        ogrenci_txt_dosyasi.seek(0)
                        ogrenci_txt_dosyasi.write("\n")
                        ogrenci_txt_dosyasi.write(str(self.kitap_alan_tc)+" ")
                        ogrenci_txt_dosyasi.write(str(self.verilen_kitap_id))
   
                        #kitap_bilgiler ve diğer listelerden sil
                        self.id_listesi.pop(i)
                        self.kitap_bilgileri.pop(i)
                        self.yazar_isimleri.pop(i)
                        
                        print("Ödünç verdikten sonra yeni id listesi = ",self.veri_sirala())

        self.odunc_ver_butonu = Button(text="Ödünç Ver",command=odunc_ver,bg="red",bd="10")
        self.odunc_ver_butonu.place(x=500,y=250)

        
    def veri_sirala(self): #Abstract method-1
        for i in range(1,len(self.id_listesi)):
            key = int(self.id_listesi[i])
            j = i - 1

            while j >= 0 and key < int(self.id_listesi[j]):
                self.id_listesi[j+1] = self.id_listesi[j]
                j -= 1
            self.id_listesi[j+1] = key
        return self.id_listesi
#----------------------------------------------------------------------------------------------------
# iade alınan kitabın id'sini gir. iade eden kişinin TC'sini gir. Ve bunları ödünç listesinden sil.
class iade_al_sinifi(kitap_islemleri):
    def __init__(self):
        super().__init__()
        self.tarih = "00.00.00"

        self.id_listesi = self.getIdlist() #Kapsülleme yapılmış veriyi çekmek için bu metodu çağırdık
        
    def iade_sayfasi(self):
        self.alınan_kitap_id = Entry(font=("Comic Sans MS", "15","normal"))
        self.alınan_kitap_id.place(x=420,y=150,width = 250, height = 30)

        self.kitap_veren_tc = Entry(font=("Comic Sans MS", "15","normal"))
        self.kitap_veren_tc.place(x=420,y=200,width = 250, height = 30)

        self.iade_kitap_ismi = Entry(font=("Comic Sans MS", "15","normal"))
        self.iade_kitap_ismi.place(x=420,y=250,width = 250, height = 30)

        self.iade_yazar_ismi = Entry(font=("Comic Sans MS", "15","normal"))
        self.iade_yazar_ismi.place(x=420,y=300,width = 250, height = 30)

        def iade_et():
            self.alınan_kitap_id = self.alınan_kitap_id.get()
            self.kitap_veren_tc = self.kitap_veren_tc.get()
            self.iade_kitap_ismi = self.iade_kitap_ismi.get()
            self.iade_yazar_ismi = self.iade_yazar_ismi.get()

            if self.alınan_kitap_id == "" or self.kitap_veren_tc == "" or self.iade_kitap_ismi=="" or self.iade_yazar_ismi=="":
                uyarı = Label(text = "Lütfen boş bırakmayınız!!",font=("Verdana 13 bold"),background="black",fg ="red")
                uyarı.place(x=400,y=400)
                
            else:
                uyarı = Label(text = "Başarılı bir şekilde iade alındı!!",font=("Verdana 13 bold"),background="black",fg ="red")
                uyarı.place(x=400,y=400)

                #kitapbilgiler.txt ekleme
                kitap_txt_dosyasi.seek(0)
                kitap_txt_dosyasi.write(str(self.alınan_kitap_id))
                kitap_txt_dosyasi.write("/"+self.iade_kitap_ismi+"/")
                kitap_txt_dosyasi.write(self.iade_yazar_ismi)
                kitap_txt_dosyasi.write("\n")

                

                #Ödünç listesinden sil
                a = self.kitap_veren_tc+" "+self.alınan_kitap_id
                with open("Ödünç bilgileri.txt", "r", encoding="utf-8") as f:
                    b = f.readlines()
                with open("Ödünç bilgileri.txt", "w", encoding="utf-8") as f:
                    for c in b:
                        if (c.strip("\n")) != a:
                            f.write(c)

                print("İade aldıktan sonra yeni id listesi = ",self.veri_sirala())

        self.odunc_ver_butonu = Button(text="İade Et",command=iade_et,bg="red",bd="10")
        self.odunc_ver_butonu.place(x=500,y=350)


    def veri_sirala(self): #Abstract method-2
        for i in range(1,len(self.id_listesi)):
            key = int(self.id_listesi[i])
            j = i - 1

            while j >= 0 and key < int(self.id_listesi[j]):
                self.id_listesi[j+1] = self.id_listesi[j]
                j -= 1
            self.id_listesi[j+1] = key
        return self.id_listesi
#----------------------------------------------------------------------------------------------------

pencere_ac = pencere_islemleri()    #pencere üzerinde ki eklentileri ekleyebilmek için oluşturduğumuz pencere sınıfını çağırıyoruz

pencere.mainloop()
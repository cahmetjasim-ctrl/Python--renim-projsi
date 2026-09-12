

isim = input("isimini gir")
soyisim = input("soy isimini  gir")
print(int(input("yaşını gir")))

isim = "ahmo"
alinan_isim = input ('isim')
if  alinan_isim == isim:
    print('doğrulandı')
elif alinan_isim == 'mehmet': 
    print('yaklaştınıız')
else:
    print('doğrulanmadı')

sayi = 0

while sayi < 10:
    print(sayi)
    sayi = sayi +1

balanğic = 0

while balanğic < 5:
    balanğic = balanğic + 1
    print(balanğic)

pazar_list = ['armut','erik','patlıucan','dut','armut','armut']

print(pazar_list[:])

pazar_listesı = ['domates','muz','elma','marul']
pazar_listesı.append('salata')

alısverıs_list = ['ayakabı','hırka']

print(pazar_listesı + alısverıs_list)

ins_ta = ['instegram']
print(ins_ta[1:2])

#balan = 0

#while balan < 10:
    #if balan % 2 == 0:
       # print(balan)
        #balan = balan + 1
        #continue

    
list_elman = ['elma','kiraz', 'artmut']

for item in list_elman:
    print(item)

    liste = ['elma','mamo','cacık']
    print(liste[0])
    


   # ada_satin = ['hırka','ada']
   # print(dir(ada_satin))

liste = ['elma','kiraz','armut']

for item in liste:
    print(item)

    sayi_liste = [1,2,3,4,5,6]
total = 0
for sayi in sayi_liste: 
 total = total + sayi
print(total)

sayi_listesi = [1,2,3,4,5,6,7,8,9,10]
for rakam in sayi_listesi:
  print(rakam)

  print(list(range(10)))

  for item in range(20):
    print(item)

    ahmet = "ahmet"
    print(ahmet[0])

    liste = ['elma','cacık','meo']
    print(liste[2])

    liste_eleman = ['cac','ar','kir']
    print(liste_eleman[1:3])

tanng_liste = ['paz','sal']
tanng_liste.append('carS')
print(tanng_liste)

person = {
   'isim': 'ahmet',
   'soy_isim': 'çiftçi',
   'yas': '15'
}

person['color'] = 'red'
print(type(person))
print(person['isim'])
#print(person) istediği zamna bunu çalıştr üstkimi çalıştrmak istemezsen bu kodda tüm hepsini çıııartııyor
print(person.items())

person_2 = dict(isim='mhmet', soyisim='çiftçi', yas=15)

print(person_2)

person_3 = {
    "isim": "mami",
    "soyisim": "demir oğli",
    "yas": 20
}

if "yemek" in person_3:
  print("person_3['yemek']")
else:
  print("içinde kiyde value bulunmadı!")

  print(dir(person_3))

  print(help(person_3.get))

  print(person_3.get("isim", False))

  print(person_3.values())

  sayi_listsi: list[int] = [10,20,30,40,50]
  for sayi in sayi_listsi:
    print(sayi)

    new = {
      "ismin": "ahmo",
      "soy_isism": "demir",
      "yas": 25
    }

  new["color"] = "pink"
  print(new)

  new = dict(isim="ahmo", soy_isim="demir", yas=25)

  if "yemek" in  new:
    print(new["yemek"])
  elif "yemek" in new:
   print(new.get("yemek", "bu value bulunmadı"))
  else:
    print("bu value bulunmadı")

    print(dir(new))

    for anahtar, key in new.items():
      print(anahtar, "=", key)


rakam_listesi = [1,2,3,4,5]
total = 0
for rakam in rakam_listesi:
        total = total + rakam
print(total)

rakam_sayimi = [1,2,3,4,5,6,7,8,9,10]
for sayi in rakam_sayimi:
   print(sayi)

   isim = "ahmet"


   ssss = 0

while ssss < 10:
        ssss = ssss + 1
        if ssss % 2 != 0 :
            continue
        print(ssss)

rakam_sayımis = [1,2,3,4,]
total = 0
for rakım in rakam_sayımis:
           total = total + rakım
print(total)

#(reng) = fonkisoyonu reng fonksiyonu
sayma_listesi = [1,2,3,4,5,6,7,8,9,10]
for sayım in sayma_listesi:
    print(sayım)

while True:
    gggg = input("isim giriniz")
    if gggg == 'cıkıs':
            break
    print(gggg)

iiii = "ahmet"
aaaa = input('isim')
if isim == aaaa:
    print("doğrulandı")
elif aaaa == "memo":
    print("yaklaştınıız")
else:
    print("yanlış")

new = dict(isim = "ahmet",soy_isim = "çiftçi",yas=12)
print(type(new))

print(new.get("isim",False))
print(new.values())

akabı_listesi = ["nıke" , "adidas","puma" ]
pazarlistesi = ["muz","portakal" , "çilek", "patlıcan"]
print(akabı_listesi + pazarlistesi)
akabı_listesi.append("abibas")
print(akabı_listesi)

tag = {
    "isim": "jasim",
    "soy_isim": "demirci",
    "yas": "28"
}

tag["color"] = "red"

get = dict(isim = "ahmet", soy_isim = "çiftçi", yas= 12, araba = "BMW")
print(type(get))
print(get)

print(type(tag))
print(tag)
print(dir(tag))
print(get.values())


if "araba" in tag:
    print(tag["araba"])
else:
    print("bu veri yani kiy ile value bulunamadı")
 
 
print(get["soy_isim"])

while True:
    asla = input('isim giriniz lütfen')
    if asla == 'ahmet':
        break
    print(asla)

isim = "ahmet"
isim = input("isim giriniiz")
if isim == "ahmet":
            print("dğrulandı")
elif isim == "ahmo":
            print("yaklaştınz")
else:
            print("yanlış doğrulanmadı")


lan = [5,5]
total = 0
for toplam in lan:
    total = total + toplam
    print(total)

    print(help(tag.get))

    isim = "oguzhan"
    print(isim[2])

    lag = ["araba","motor","otobüs"]
    for lang in lag:
        print(lang)

    rengg = [1,2,3,4,5,6,7,8,9,10]
    for ki in rengg:
        print(ki)

        basla = 0
        while basla < 10:
            basla = basla + 1
            if basla % 2 != 0:
                continue
            print(basla)

#bu kod parantesizi çalışmaz kare paretezle 0 rıncı indeks numarasında başlar ve 9 kadar gider
            print(list(range(10)))

           

            isim = ()
            print(type(isim))

            sayilar = (1,2,3,4,5)
            print(sayilar)

            sayilar =(1,2,3,4,5,6,7,8)
            sayilar_liste = [1,2,3,4,5,6,7,8,9,10,11,12,113]
            print(sayilar[3])
            print(sayilar[3])

            sayiilar = (1,)
            print(type(sayilar))

            for i in sayilar:
                print(i)
    #tuplarda ekleme yapılmaz o yüzden hata verir
        #new_tuple = ("ahmet", "çiftçi", 15)
        #new_tuple[3] = "ismail"

        sayilar = 1,2,3,4,5,6,
print(sayilar)


import sys

isism_lisesi = ["ahmet", "ali","sayi", True, False,123.123]
tuple_lisstesi = ("ahmt","ali","sayi", True, False,123.123)
print(sys.getsizeof(isism_lisesi))
print(sys.getsizeof(tuple_lisstesi))

print(dir(sys))
print(sys.getsizeof)


sayyylir = (1,2,3,4,5,6,7,8,9,10)
sayyylir_listesi = [1,2,4,5,3,4,6]
print(sayyylir[3])
print(sayyylir[5])

saylar = (1, )
print(type(saylar))

print(dir(saylar))


print(dir(sayyylir))
   
   # print(help(sys.getsizeof()))

alınacaklar = set()
print(dir(alınacaklar))

print(help(alınacaklar.add))

alınacaklar.add("elma")
alınacaklar.add("itap")
alınacaklar.add("araba")
alınacaklar.add("araba")
print(alınacaklar)

alınacaklar.remove("elma")
print(alınacaklar)

alınacaklar.clear()
print(alınacaklar)

#burada set() vereck çünkü set() boş bir küme oluşturur ve discard() metodu ile silmeye çalıtırız ama set() boş olduğu için hata vermez ve çalşır
alınacaklar.discard("bmw")
print(alınacaklar)

alınacaklar = set(["elma","armut","kiraz","elmma"])
print(alınacaklar)

alnanalar = {"araba", "helikopter", "uçak", "tren"}
print(type(alnanalar))

tek_sayilar = set([1,3, 5, 7, 9])
cift_sayilar = set([2,4,6,8])
print(tek_sayilar.union(cift_sayilar))

tek_ssayilar = set([1,3,5,7,9])
cift_sayilarrr = set([2,4,6,8,])
asall_sayyilar = set ([2,3,5,7])
print(tek_ssayilar.intersection(asall_sayyilar))

def toplama():
    print('yıldız')
toplama()

def sorunlu():
    print('miss')
print(sorunlu)

def hesap():
    print('akıcı')
    return 'yooo'
x = hesap()
print(x)

def matamatikk(b,d):
    return b + d
x = matamatikk(2,4)
print(x)

def matamatik(a , d = 2):
    return a + d
x = matamatik(1)
print(x)

def sorun( a,ş=3 ):
   """
   burada sadece  okuyamayanlar için
   """
   return a + ş
help(sorun)
x = sorun(2)
print(x)

def mantık(x,y):
    return x + y
top = mantık(y=1, x=4)
print(top)

def fonksiyon(*args,**kwargs):
    print(args)
    print(kwargs)
fonksiyon(1,2,3,4,5, y=2, t=3)

def valo(t,c, *args,**kwargs):
    print(args)
    print(kwargs)
valo(1,2,3,4,5,6,7,8,9 , y=1,e=1)

def ccc(a,b, *args,**kwargs):
    print(args)
    print(kwargs)

fff=ccc(1,2,4,6,7,8)
print(fff)

def rrr(a,b, *args,**kwargs):
    print(args)
    print(kwargs)
    return 20

ddd=rrr(1,2,4,6,7,8)
print(ddd)

def mat(*args,**kwargs):
    mat = 0
    for eleman in args:
        mat = mat + eleman
    return mat
hes = mat(1,2,3,4,5)
print(hes)

def faktariyel(x):
    if x == 1:
        return 1
    else:
        return(x * faktariyel(x-1))
sonuc = faktariyel(5)
print(sonuc)

def faktariyel(x):
    if x == 1:
        return 1
    else:
        return(x  * faktariyel(x-1))
sonuc = faktariyel(3)
print(sonuc)


isim_sssm = ["B","C","K","D","E","F","Ç"]
isim_sssm.sort(key=lambda x: x.split(' ')[-1].lower())
print(isim_sssm)



bslamak = 0
while bslamak < 10:
     bslamak = bslamak +1
     if bslamak % 2 == 0:
         continue
     print(bslamak)


     issss_mm = ["bursa","ahmet","okan"]
     issss_mm.sort(key = lambda x: x.split(' ')[-1].lower())
     print(issss_mm)


     def fak(c):
         if c == 1:
             return 1
         else:
             return(c  * fak(c-1))
sonuc = fak(2)
print(sonuc)

im = (1,2,3,4,5,6)
print(im)

darkines = 1,2,3,4,5
print(darkines)

syillar = (1,2,3,4,5)
syillar_liste = [1,2,3,4,5,7,]
print(syillar[4])
print(syillar[4])

sayma = (1, )
print(type(sayma))

amo = {
    "isim" : "ahmet",
    "isim_soy" : "çiftçi",
    "yas" : 25
    }
print(type(amo))

nam = dict(isim="ahmet",soyisim="muzafer",yas=22)
print(nam)

isimm = ["amo","elao","hasan hüseyin"]
isimm.sort(key = lambda v: v.split(' ')[-1].lower())
print(isimm)

isimmm = "ahmet"
isimmm =  input("isim")
if isimmm == "ahmet":
    print("tamm doğru")
elif isimmm == "ahmo":
    print("yaklaştnız")
else:
    print("yanlış")

    yyy_liste = [1,2,3,4,5,6,7,8,9,10]
    ddd_liste = list(filter(lambda x:(x  % 2  == 0) , yyy_liste))
    print(ddd_liste)

    print((filter(lambda x:(x  % 2  == 0) , yyy_liste)))

    turk = {"memo","kk"}

    turk.add("as")
    turk.add("mehmet")
    turk.add("ali")
    turk.add("yut")
    turk.add("asya")



    print(turk)



listeleme = [1,2,3,4,5,6,7,9]
liste_alım = list(filter(lambda x: (x % 2 == 0),listeleme))
print(filter(lambda x: (x % 2 == 0),listeleme)) # bu eleman filterın kimliğini yani objecti gösteriyo printe böyle yaptımızda
print(liste_alım)

listeleme = [1,2,3,4,5,6,7,8]

yyy_lissst = list(map(lambda x: x *2, listeleme))

kle = [1,2,3,4,5,]

kll_ayara = map(lambda v: v % 2 == 0, kle)
print(map(lambda v: v % 2 == 0, kle))

#print(map(lambda x: x *2, listeleme))
print(yyy_lissst)

#print(type(yyy_lissst))

fflteer_liste = [1,2,3,4,5,6,7,8,9]
fil_liste = (filter(lambda x: x % 2 == 0 , fflteer_liste))
print(type(fil_liste))


# not: kwargs yani ** yıldız sembolü yanlızca ama yanlızca tuple ve sözcük içindir tuple () bu sembol sözcük ise {} semboldür tuple başına "" koymna gerek yoktur ama "" sözcükte bu geçerli 

#def anlmi(a,b,c,d,g,t):
    #return a+b+c+d+g+t

#an = anlmi() hata alır!


def zkz(a,b,c,d):
    return a+b+c+d
ank = zkz(1,2,3,4)



def sssks(a,b,c,d):
    return a+ b+ c+ d
sayiii = [1,2,3,4,]
sayı = sssks(*sayiii)   
print(sayı)

def ads(*mm):
    print(mm)

ads(1,2,3,4,5,6)


#def ads(**m):
    #print(m)

#ads(1,2,3,4,5,6) hata verceğiiçin çalışmaz kwargs sadece sözcük içindir! ha birde unutmadan sözcük {} sembolüyle belli olur kwargs tuple ve sözcük

def sssc(**asö):
    print(asö)

sssc(isim = "ahmet", soy = "cc")

def ammm(*mk):
    print(mk)

ammm(8)


def scsd(**hss):
    print(hss)

scsd(isim="amo",soyisim = "çi", yas = 22)

def anne(*abi,**baba):
    print(abi)
    print(baba)

anne(1,2,3,4,5,6 , isim = "ahmet" , soy = "çiftçi" , yas = 15, meslek = "yazılım inşallah")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
scdr = input("isim gir")
scdr = input("soyismini gir")
print(int(input("yaşını gir lütfen")))

ahmet = input("ismi gir")
pasword = input("şifreyi gir")

print(ahmet == "ahmt" and pasword == "123456")


ism = input("isimi gir lütfen ")
şifr = input("şifreyi gir")

print(ism == "ahmet" or pasword == "12345567" )


isim = ("hamet")
alinan_degr_i = input("isim giriniiz")

if isim == alinan_degr_i:
    print("doğrulandı")
elif alinan_degr_i == "ahmet":
    print("isime çoooooooooook yaklaştınız efndim 😊")
else:
    print("isim yanlış")

#sayi = 0 
#while sayi < 5 : 
   # print(sayi) 
    #sayi = sayi + 1
    #print("ilem tamamlandi")

#sayı = 1
#while sayı <= 10:
    print(sayı)
    sayı = sayı + 1
#else:
    #print("olmaz")

#baslangic = 0
#while baslangic < 10 :
    # if baslangic % 2 == 0 :
     #    continue
   #  baslangic = baslangic + 1

#basla = 0 
#while basla < 10 : 
    #if basla % 2 != 0:
   #  continue
   # basla = basla + 1
    #print(basla)

    while True:
        ism = input("isim giriniz")
        if ism == "jasim":
            break
        print(ism)

class Person:
    def speak(self):
        pass

    def eat(self):
        pass

class Person:
    def speak(self):
        print(f"{self.name} konuşuyor")


    def eat(self):
        print(f"{self.name} yedi")


adam1 = Person()
adam2 = Person()
adam3 = Person()

print(id(adam1))
print(id(adam2))
print(id(adam3))

class Person:
    def speak(self):
        print(f"{self.name} koonumak")

    def eat(self):
        print(f"{self.name} yemeği yedi")


şahis1 = Person()
şahis1.name = "Ahemt"
şahis1.speak()
şahis1.eat()


class Person:
    def speak(self):
        print(f"{self.name}  konuşmaaa ")

    def eat(self):
        print(f"{self.name} yemek yimeee")


ada1 = Person()
ada1.name = "Ahmet"
ada1.speak()
ada1.eat()


ada2 = Person()
ada2.name = "mehmet"
ada2.speak()
ada2.eat()


class Person:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(f"{self.name} konuştu")

    def eat(self):
        print(f"{self.name} yediii")


akka1 = Person(name = "ahmet")
akka1.speak()
akka1.eat()

akka2 = Person(name = "meo")
akka2.speak()
akka2.eat()

 
class Person:
    def __init__(self,name,surname):
       self.name = name
       self.surname = surname

    def speak(self):
        print(f"{self.name}{self.surname} konuştu")


    def eat(self):
        print(f"{self.name}{self.surname} yedi")


kişi1 = Person(name = "Ali", surname= "ümeyir erdoğan")
kişi1.speak()
kişi1.eat()

#class Person:
   # def __init__(self,first_name,last_name):
       # self.name = first_name
        #self.surname = last_name

#amo = Person()

class Person:
    def __init__(self):
        pass
top = Person()

class Person:
    def __init__(self,first_name,last_name):
        self.name= first_name
        self.surname = last_name

amo = Person("ahmet", "ali")
print(amo.name)
print(amo.surname)
ame = Person("ali", "ahmo")
print(ame.name)
print(ame.surname)

class Person:
    def __init__(self,first_name,last_name):
        self.name = first_name
        self.surname = last_name

amt = Person("ahmo", "ali")
aho = Person("muhamet", "muz")
print(id(amt))
print(id(aho))



class Person:
    def __init__(self,first_name,last_name):
        self.name = first_name
        self.surname = last_name
        self.şozluk = {}

att = Person("ahmet",  "muhamet")
att.şozluk["yazılım"] = "defter"
print(att.şozluk)
asd = Person("ahmo", "ahmet")
print(asd.şozluk)

class Person:
    sds = {}

    def __init__(self,first_name,last_name):
     self.name = first_name
     self.surname = last_name

adf = Person("ahmet",  "muhamet")
adf.sds["kitap"] = "yazılım"
print(adf.sds)
kkc = Person("ahmet", "ali")
print(kkc.sds)


class atış:
    def __init__(self,isim,soyisim):
        self.isim = isim
        self.soyisim = soyisim

    def şart(self):
        print(f"merhaba eyer benele bir anlaşmaya gelmeek istiyorsanız lütfen isminizi söyleyin benim adım {self.isim} tanıştıma memun oldum")

    def tanitma(self):
        print(f"ism {self.isim} soy ismim {self.soyisim} bu benim ")

    def para(self):
        print(f"1.000000000000000000000000000000000000000000000000000000 ben trilyonerim {self.isim}")

vic = atış("ahmet",  "mehmet")
vic.şart()
vic.tanitma()
vic.para()


class adam:
    def __init__(self,isim,soyisim):
        self.isim = isim
        self.soyisim = soyisim

    def atom(self):
        print(f"ben kimim {self.isim} soyismim {self.soyisim}")

    def atack(self):
        print(f"ismim {self.isim}")

#class comart(adam):
    pass
#degr = comart()


class amo:
    def __init__(self,ahmet,çiftçi):
        self.isim = ahmet
        self.soyisim = çiftçi

    def isimler(self):
        print(f" bunlar benim isimi {self.ahmet} {self.çiftçi}")

    def yalan(self):
        print("benim çok fazla helikopterim var")

class yalan(amo):
    pass
vat = yalan("ahmet", "furkan")
vat.yalan()

class doğru(amo):
    def dgru(self):
        print("ben çalışıp ekmek paramı kazanıyorum")
dek = doğru("amet", "akif")
dek.dgru()


class mmatom:
    def __init__(self,isim,soyisim):
        self.isim=isim
        self.soyisim=soyisim

    def karışık(self):
            print(f"merhab ben {self.isim}")

    def tor(self):
        print(f"merhablar hoş geldiniz")

class bu_ne(mmatom):
    def __init__(self,ism,soy,kağıt):
        self.ism = ism
        self.soy = soy
        self.kağıt = kağıt

    def mek(self):
        print(f"benim çok fazla {self.kağıt} ım var")

    def saygısız(self):
        print(f"merhaba aşğlık herif")

vetk = bu_ne("ahmet", "ayşe",  kağıt=1.000000)
vetk.mek()
vetk.saygısız()

class trk:
    def __init__(self,kişi,varlık):
        self.kişi = kişi
        self.varlık = varlık

    def anlam(self):
        print(f"merhaba ben {self.kişi}")

    def çokça(self):
        print("merhaba ben anlam")

class nerto(trk):
    def __init__(self,şahıs,kişi,elon):
        super().__init__(şahıs,kişi)
        self.elon = elon

    def arkadas(self):
        super().çokça()
        print(f"benim maşş {self.elon}")

white = nerto("ahmet", "mhmet",  elon=1000)
white.arkadas()
white.çokça()

class astra:
    def __init__(self,ahmet,ali):
        self.ahmet = ahmet
        self.ali = ali

    def yukarı(self):
        print(f"naber nasılsın {self.ahmet}")

    def artçı(self):
        print(f"merhaba nasılsın {self.ali}")

class netro(astra):
    def __init__(self,isim,soyisim,ali,kagit):
        self.isim = isim
        self.soyisim = soyisim
        self.ali = ali
        self.kagit = kagit
        
    def vmax(self):
        super().artçı()
        print(f"merhaba nasılsın ben sadece yazılımla ilgileniyorum şuan yaptığım şey sadece: yazılım adsımda {self.kagit}")

dj = netro("javascript", "python","C#", kagit=1000)
dj.vmax()

class turbo:
    def __init__(self,dolar,euro):
        self.dolar = dolar
        self.euro = euro

    def admin(self):
        print(f"bu benim isimim olabilir {self.dolar}")

    def suju(self):
        print(f"merhaba tanıştığıma çok memun oldum....")

class tekno(turbo):
    def __init__(self,ahmet,mehmet,tl,euro,dolar):
        super().__init__(tl,euro)
        self.ahmet = ahmet
        self.mehmet = mehmet
        self.dolar = dolar
       

    def kisi(self):
        print(f"merhaba ben 2 inci ahmet bana şu kadar borcun var {self.dolar}")

    def memun(self):
        print("ahmet jasim çiftçi ")

onlar = tekno("java", "bash", "CI/CD", "GO", dolar=1.0000)
onlar.kisi()

class türk:
    @staticmethod
    def cık(a,b):
        return a + b

    @staticmethod
    def top(ç,b):
        return ç - b

print(türk.cık(1,2))
print(türk.top(1,2))

class ada:
    def __init__(self,name,page):
        self.name = name
        self.page = page

    @classmethod
    def ad_sad(cls,data):
        ada = []
        for ada in data:
            print(ada)

data = [  
  { "name": "a1", "page": 60 },
  { "name": "a2", "page": 79 },
  { "name": "a3", "page": 90 }
] 

ada.ad_sad(data=data)


class saka:
    def __init__(self,name,page):
        self.name=name
        self.page = page

    @classmethod
    def for_sonuc(cls,data):
        sakas = []
        for saka in data:
            sakas.append(cls(name = saka["name"], page=saka["page"])) 
        return sakas

    data = [
        {"name": "a1", "page": 60},
        {"name": "a2", "page": 79},
        {"name": "a3", "page": 90}
    ]

sakas = saka.for_sonuc(data=data)
print(sakas[0].name)

print("biti sonunda")
    

        
    
        




























 





    


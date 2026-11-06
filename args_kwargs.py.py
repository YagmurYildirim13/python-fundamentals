def kuvvet_al(x, y): #positinal arguments hepsi tam olarak girilmeli
    return x ** y

#print(kuvvet_al(4, 3))

#def bilgi_ver(ad,soyad = "Girilmedi", yas = "Girilmedi"): #keyword argument
    return f"Ad: {ad} Soyad: {soyad} Yas: {yas}"

#print(bilgi_ver("Ali", "Calıskan"))

def bilgi_ver2(ad = "Girilmedi",soyad = "Girilmedi", yas = "Girilmedi"): #keyword argument
    return f"Ad: {ad} Soyad: {soyad} Yas: {yas}"


#print(bilgi_ver2("Ali", yas = 34))
#print(bilgi_ver2())
#rint(bilgi_ver2(soyad = "Calıskan", yas = 23))


#def topla(*args):
    #for arg in args:
        #print(args)
    

#topla(1,2,3,4,5, "Python", True)

def carp(*args):
    carpim = 1
    for arg in args:
        carpim *= arg
        return carpim
    #print(type(args))


#carp(3,4,5,6,7)
#print(carp(4,5,2,3))

def selamla(mesaj, *args):
    sonuc = ""
    sonuc += mesaj
    for arg in args:
        sonuc += arg
    return sonuc
    #print(mesaj)
    #for arg in args:
        #print(arg)

#print(selamla("Merhaba", "Nasilsin"))

def fonk(**kwargs):
    print(kwargs)

#fonk(ad = "ali", soyad = "çalışkan", yas = 34)

def fonk2(zorunlu, *args,**kwargs):
    print(zorunlu)
    print("***********")
    for arg in args:
        print(arg)
    print("***********")
    for kwarg in kwargs:
        print(kwarg)

fonk2(2,3,4,5,6,7, ad = "Ali", yas = 23)
#def fonk(x):
    #return x*x

#a = fonk(3)

#print(a)

#b = fonk
#print(b(5))

def islem_sec(islem):
    def toplama(*args):
        toplam = 0
        for arg in args:
            toplam += arg
        return toplam


    def carpma(*args):
        carpim = 1
        for arg in args:
            carpim *= arg
        return carpim
    def ortalama(*args):
        return sum(args) / len(args)

    if islem == "toplama":
        return toplama
    elif islem == "carpma":
        return carpma
    elif islem == "ortalama":
        return ortalama

#top_fonk = islem_sec("toplama")
#print(top_fonk(2,3,4,5))
#carpma_fonk = islem_sec("carpma")
#ortalama_fonk = islem_sec("ortalama")
#print(ortalama_fonk(3,4))

def kisi_sec(kisi):
    def takim_sec(takim):
        return f"{kisi} {takim} takımını tutuyor"
    return takim_sec

a = kisi_sec("Ali")
b = kisi_sec("Veli")

print(a("Fenerbahçe"))
print(b("Beşiktaş"))
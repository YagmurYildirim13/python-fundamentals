#demet = ("sarı", "mavi", "yeşil","kırmızı","siyah") #demetler listelerden farklı olarak değiştirilemeler ve nesne atılamaz
#for renk in demet:
    #print(renk)

#kume = {"sarı", "mavii", "yeşil", "kırmızı", "siyah"} #kümeler listelerden farklı olarak değiştirilemezler ve nesne atılmaz
#print(kume)

#kume.add("pembe") #add metodu ile kümeye yeni bir eleman eklenir

#kume.remove("sarı") #remove metodu ile kümede istediğimi bir elemanı silebiliriz

#kume.discard("gri") #discard metodu ile kümede istediğimiz bir elemanı silebiliriz remove metodundan farkı silmek istediğimiz eleman yoksa hata vermez
#print(kume)


#kume1 = {"sarı", "mavi", "yeşil", "kırmızı", "siyah"}
#kume2 = {"sarı", "mavi", "yeşil", "beyaz", "gri"}

#print(kume2.intersection(kume1)) #intersection metodu ile iki kümenin kesişim kümesini bulabiliriz
#print(kume2.union(kume1)) #union metodu ile iki kümenin birleşim kümesini bulabiliriz
#print(kume2.difference(kume1)) #difference metodu ile iki kümenin fark kümesini bulabiliriz

#birleşim = kume1.union(kume2)
#print(birleşim)

#print("sarı" in kume1) #in metodu ile kümenin içinde istediğimiz bir elemanın olup olmadığını kontrol edebiliriz
#print("mor" in kume1) #in metodu ile kümenin içinde istediğimiz bir elemanın olup olmadığını kontrol edebiliriz

#bosliste1 = [] #boş liste
#bosliste2 = list() #boş liste

#bosdemet = () #boş demet
#bosdemet2 = tuple() #boş demet

#boskume1 = set() #boş küme
#boskume2 = {} 
#print(type(boskume2)) #boş küme değil sözlük türğnde değişken oluşturur

#python = set("PYTHON") #
#print(python) 

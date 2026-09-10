kisi = {"isim": "Ahmet", "yas": 20, "cinsiyet": "m", "hobiler" : ["sinema", "konser", "yazılım"]}
#print(kisi["isim"])
#print(kisi["yas"])
#print(kisi["cinsiyet"])
#print(kisi["hobiler"])


#kisi["isim"] = "Ahmet" #sözlükteki bir anahtarın değerini değiştirmek için kullanılır

#kisi.update({"isim": "Ahmet", "yas": 30}) #update metodu ile sözlükteki anahtarların değerlerini değiştirebiliriz
#kisi["id"] = 12345 #sözlükte yeni bir anahtar ve değer eklemek için kullanılır
#print(kisi)
#del kisi["id"] #sözlükteki bir anahtarı ve değerini silmek için kullanılır
#print(kisi)

#for x in kisi:
    #print(x) #sözlükteki anahtarları yazdırır

#for x in kisi:
    #print(kisi[x]) #sözlükteki değerleri yazdırır

#print(kisi.keys()) #Ssözlükteli değerlerin anahtarlarını yazdırır
#print(kisi.values()) #sözlükteki değerleri yazdırır
#print(kisi.items()) #sözlükteki anahtar ve değerleri yazdırır.

#for k, v in kisi.items():
    #print(k,v) #sözlükteki anahtar ve değerleri yazdırır.

#print(kisi["id"])

print(kisi.get("id")) #sözlükteki bir anahtarın değerini almak için kullanılır. Eğer yoksa None döndürür

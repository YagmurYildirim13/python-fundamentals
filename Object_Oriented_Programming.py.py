class calisan:
    def __init__(self, name, surname, age):
        #print("init foksiyonu çalıştı")
        self.name = name
        self.surname = surname
        self.age = age
    def show_info(self):
        print(f"AD: {self.name} SOYAD: {self.surname} YAŞ: {self.age}")

calisan1 = calisan("Ali","Veli",20)
#print(calisan1.name, calisan1.surname, calisan1.age)

calisan2 = calisan("Ahmet","Yılmaz",25)
#print(calisan2.name, calisan2.surname, calisan2.age)

calisan.show_info(calisan2)

#calisan1.show_info()
#calisan2.show_info()

#calisan1 = calisan()

#calisan1.name = "Ali"
#calisan1.surname = "Veli"
#calisan1.age = 20
#print(calisan1.name)
#print(calisan1.surname)
#print(calisan1.age)
#calisan2 = calisan()
#calisan2.email = "a@b.com"
#print(calisan2.email)

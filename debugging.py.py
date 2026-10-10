#try:
    #a = 5
    #b = 0
    #if b == 7:
        #raise ZeroDivisionError
    #c = a / b
    #x = 5
    #d = x
    #isim = "Ali"
    #karakter = isim[2]

#except Exception:
    #print("Bilinmeyen bir hata oluştu")
#except ZeroDivisionError:
    #print("Bir hata oluştu")
#except NameError:
    #print("Bu değişken tanımlı değil")
#except IndexError:
    #print("Index hatası oluştu")
#except Exception:
    #print("Bilinmeyen bir hata oluştu")


#else:
    #print("ELSE BLOĞU ÇALIŞIYOR")
    #print(c)
    #print(karakter)
#finally:
    #print("Finally bloğu çalışıyor")

try:
    a = 5
    b = 2
    if b == 7:
        raise ZeroDivisionError
    c = a / b
    x = 5
    d = x
    isim = "Ali"
    karakter = isim[1]
    list_ = [1,2,3]
    m = list_[5]
except ZeroDivisionError as e:
    print(e)
except NameError as e:
    print(e)
except IndexError as e:
    print(e)
except Exception as e:
    print(e)






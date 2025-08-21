ceviri = {
    "iken": "while",
    "eğer": "if",
    "aksi": "else",
    "ve": "and",
    "veya": "or",
    "değil": "not",
    "yaz": "print",
    "girdi": "input",
    "doğru": "True",
    "yanlış": "False",
    "hiç": "None",
    "kır": "break",
    "devam": "continue"
}

def cevir(kod_satiri):
    for tr, py in ceviri.items():
        kod_satiri = kod_satiri.replace(tr, py)
    return kod_satiri

def yası(*args, sep=" ", end="\n"):
    print(*args, sep=sep, end=end)

def girdi(metin=""):
    return input(metin)

print("kamil 1.0")

while True:
    try:
        mesaj = input(">>> ")
        if mesaj.strip() == "iken doğru:":
            kod_blok = []
            while True:
                satir = input("... ")
                if satir.strip() == "":
                    break
                kod_blok.append(cevir(satir))
            
            r
            exec("while True:\n" + "\n".join("    " + satir for satir in kod_blok))
        else:
            kod = cevir(mesaj)
            exec(kod)
    except SyntaxError:
        yası("Hata: Sözdizim hatası!")
    except NameError:
        yası("Hata: Tanımsız değişken ya da fonksiyon!")
    except KeyboardInterrupt:
        yası("\nProgram sonlandırıldı.")
        break
    except Exception as e:
        yası(f"Beklenmeyen hata: {e}")

     
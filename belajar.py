print ("Welcome my bio")
print (20*"=")
nama = input("siapa nama kamu:")
umur = input ("berapa umur kamu:")
alamat = input ("dimana alamat kamu:")
print ("hello",nama,"umur kamu adalah",umur,"tahun","alamat kamu di",alamat,"sby")
print (20*"=")

nama = input("Masukkan Nama Anda = ")
dapat = 0
tidakdapat = 0
nilai = 0
def getprestasinonakademik():
    choice = input("Hai"+"apakah kamu punya pretasi?\n 1.iya\n 2.tidak\n jawaban =")
    if choice == "1":
        global dapat
        dapat = 1
        getKemampuanorangtua()

    elif choice == "2":
        dapat = 0
        getKemampuanorangtua()

def getKemampuanorangtua():
    choice = input("bagaimana keadaan orang tua kamu?\n 1.mampu\n 2.kurang mampu\n jawaban =")
    if choice == "1":
        global dapat
        dapat = dapat + 2
        getRanking10besar()

    elif choice == "2":
        dapat = dapat + 3
        getRanking10besar()

def getRanking10besar():
    choice = input("apakah kamu termasuk ranking10besar?\n 1.iya\n 2.tidak\n jawaban =")
    if choice == "1":
        global dapat
        dapat = dapat + 1
        pemilihanbeasiswa()

    elif choice == "2":
        dapat = dapat + 0
        pemilihanbeasiswa()


def pemilihanbeasiswa():
    if dapat <= 3:
        print("maaf",nama,"anda tidak mendapat beasiswa")
    elif dapat == 4:
        print("selamat",nama,"anda mendapat beasiswa")

getprestasinonakademik()
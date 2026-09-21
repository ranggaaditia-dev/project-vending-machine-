minuman = {
    1:"coca",
    2:"sprite",
    3:"Fanta",
}

makanan = { 
    4:"oreo",
    5:"taro",
    6:"cocholatos"
}

benda = {
    7:"cincin",
    8:"gelang",
    9:"anting",
    10:"kacamata"
    
}

while True:
    try:
        number = int(input("Pilih nomor : "))

        if number in minuman:
            print(f"Anda memilih minuman {minuman[number]}")
        elif number in makanan:
            print(f"Anda memilih makanan {makanan[number]}")
        elif number in benda:
            print(f"Anda memilih benda {benda[number]}")
        else:
            print("EROR")
    except ValueError:
        print("EROR!!! ANDA BUKAN MEMASUKAN ANGKA")

print("=== Selamat Datang Di Perusahaan Pintaria, Silahkan Registrasi ===")

#input registrasi username dan kata password
print("Masukkan username dan kata password")
Username = input("Masukkan username : ")
Password = input("Masukkan password : ")

while True:
    #input login username dan password
    print("==================================================")
    print("=== Silahkan Login ===")
    username = input("Masukkan nama pengguna : ")
    password = input("Masukkan kata sandi :")
    if Username == username and Password == password:
        print("=== Selamat Datang Di Perusahaan Pintaria ===")
        print("==================================================")
        
        #input jam kerja dan tarif kerja
        Jam_Kerja = float(input("Masukkan Jam Kerja = "))
        Tarif_Kerja = float(input("Masukkan Tarif Kerja = "))
        Gaji = Jam_Kerja * Tarif_Kerja
        if Jam_Kerja > 160:
            #total gaji
            Bonus = Gaji * 0.1 #Bonus 10%
            Gaji = Gaji + Bonus
            print("Anda Mendapatkan Gaji Tambahan Jadi Total Gaji Anda Adalah = ", Gaji)
            print("==================================================")
        
        else: 
            print("Anda Tidak Mendapatkan Gaji Tambahan")
            print("==================================================")
        
        print("Apakah Anda Ingin Menghitung Gaji Lagi?")
        print("1)jika iya")
        print("2)jika tidak")
        pilihan =int(input("masukan pilihan anda = "))
        
        if pilihan == 1 :
            print("program diulang")
        elif pilihan == 2 :
            print("program berhenti")
            break
        else:
            print("pilihan anda tidak valid")
            break
    else:
        print("password anda salah")
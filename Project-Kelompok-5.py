import os
os.system('cls')
# Inisialisasi variabel saldo
saldo = 200000

# Fungsi untuk meminta pengguna memasukkan kartu ATM
def insert_card() :
    input('Masukkan kartu ATM Anda dan ketik enter untuk melanjutkan : ')
    os.system('cls')

# Fungsi untuk memeriksa PIN
def check_pin() :
    i = 0
    limit = 3
    while i < limit :
        pin = input('Masukkan PIN Anda : ')
        if pin == 'si23b':  
            return True
        else :
            i += 1
            print('PIN salah. Percobaan ke-', i)
            print()
    print('Anda telah melebihi batas percobaan PIN yang salah.')
    return False

def bahasa_indo() :
    global saldo
    print('Pilihan Bahasa : Bahasa Indonesia')
    os.system('cls')
    print('-'*47)
    print('|'+'Bahasa Indonesia terpilih.'.center(45)+'|')
    print('-'*47)
    print('PILIH OPSI DI BAWAH')
    print('-'*47)
    print('|'+'1.'+'|'+' Cek saldo saya'+'|'.rjust(28))
    print('|'+'2.'+'|'+' Ambil uang saya'+'|'.rjust(27))
    print('|'+'3.'+'|'+' Tabung uang saya'+'|'.rjust(26))
    print('-'*47)
    print()
    
    option = int(input('Silahkan pilih option : '))

    if option == 1 :
        print('Saldo Anda : Rp. ', saldo)
    elif option == 2 :
        print('Saldo Anda saat ini : Rp. ', saldo)
        ambil_uang = int(input('Mau ambil berapa? : '))
        print()
        if ambil_uang <= saldo :
            saldo -= ambil_uang
            print('Saldo Anda sekarang : Rp. ', saldo)
        else :
            print('Saldo tidak mencukupi, mohon coba lagi!')
    elif option == 3 :
        print('Saldo Anda : Rp. ', saldo)
        tambah_uang = int(input('Masukkan jumlah uang yang ingin ditabung : '))
        saldo += tambah_uang
        print('Berhasil menabung : Rp. ', tambah_uang)
        print()
        print('Saldo Anda sekarang : Rp. ', saldo)
    else :
        print('Pilihan Anda salah, silahkan coba lagi!')

    lanjut = input('Lanjut transaksi? (ya / tidak) : ')
    os.system('cls')
    if lanjut.lower() == 'ya' :
        return bahasa_indo()
    elif lanjut.lower() == 'tidak' :
        print('\nTerima kasih sudah transaksi!')
        rating = input('Berikan rating (1-5) : ')
        os.system('cls')
        print('Terima kasih atas ulasan Anda. Kami menghargai masukan Anda!')
    
def bahasa_inggris() :
    global saldo
    print('Language Selection : English')
    os.system('cls')
    print('-'*47)
    print('|'+'English selected.'.center(45)+'|')
    print('-'*47)
    print('CHOOSE AN OPTION')
    print('-'*47)
    print('|'+'1.'+'|'+' Check my balance'+'|'.rjust(26))
    print('|'+'2.'+'|'+' Withdraw money'+'|'.rjust(28))
    print('|'+'3.'+'|'+' Deposit money'+'|'.rjust(29))
    print('-'*47)
    print()
    
    option = int(input('Please select an option : '))

    if option == 1 :
        print('Your balance : Rp. ', saldo)
    elif option == 2 :
        print('Your current balance : Rp. ', saldo)
        withdraw_amount = int(input('How much would you like to withdraw? : '))
        print()
        if withdraw_amount <= saldo :
            saldo -= withdraw_amount
            print('Your new balance : Rp. ', saldo)
        else :
            print('Insufficient balance, please try again!')
    elif option == 3 :
        print('Your balance : Rp. ', saldo)
        deposit_amount = int(input('Enter the amount you want to deposit : '))
        saldo += deposit_amount
        print('Successfully deposited: Rp. ', deposit_amount)
        print()
        print('Your new balance : Rp. ', saldo)
    else :
        print('Invalid choice, please try again!')

    lanjut = input('Continue trading? (yes / no) : ')
    if lanjut.lower() == 'yes' :
        return bahasa_inggris()
    if lanjut.lower() == 'no' :
        os.system('cls')
        print('\nThank you for transacting!')
        rating = input('Give a rating (1-5) : ')
        os.system('cls')
        print('Thank you for your feedback. We appreciated that!')
    
def bahasa_sulawesi() :
    global saldo
    print('Pilihan Bahasa : Bahasa Sulawesi')
    os.system('cls')
    print('-'*47)
    print('|'+'Bahasa sulawesi kita pilih.'.center(45)+'|')
    print('-'*47)
    print('TABE PILIHKI OPSI TA')
    print('-'*47)
    print('|'+'1.'+'|'+' Cek bede saldoku'+'|'.rjust(26))
    print('|'+'2.'+'|'+' Tarek kan uangku'+'|'.rjust(26))
    print('|'+'3.'+'|'+' Tabung kan ka uangku'+'|'.rjust(22))
    print('-'*47)
    print()

    option = int(input('Pilihki opsi ta : '))

    if option == 1 :
        print('Saldo ta : Rp. ', saldo)
    elif option == 2 :
        print('Saldo ta sekarang : Rp. ', saldo)
        ambil_uang = int(input('Mauki ambil berapa? : '))
        print()
        if ambil_uang <= saldo :
            saldo -= ambil_uang
            print('Saldo ta sekarang : Rp. ', saldo)
        else :
            print('Nda cukup saldota, nanti kita coba lagi!')
    elif option == 3 :
        print('Saldo ta : Rp. ', saldo)
        tambah_uang = int(input('Kasih masuk jumlah uang yang mau kita tabung : '))
        saldo += tambah_uang
        print('Berhasil kita tabung : Rp. ', tambah_uang)
        print()
        print('Saldo ta sekarang : Rp. ', saldo)
    else :
        print('Salah pilihan ta, nanti kita coba lagi!')

    lanjut = input('Mauki lanjut transaksi? (iye / tidak) : ')
    os.system('cls')
    if lanjut.lower() == 'iye' :
        return bahasa_sulawesi()
    elif lanjut.lower() == 'tidak' :
        os.system('cls')
        print('\nTerimakasih sudahki bertransaksi!')
        rating = input('Kasihki rating (1-5) : ')
        os.system('cls')
        print('Terimakasih atas ulasan ta. Kita hargai ulasan ta!')
   
# Program ATM
print('-'*47)
print('|'+'SELAMAT DATANG DI ATM'.center(45)+'|')
print('-'*47)

insert_card()  # Meminta pengguna memasukkan kartu ATM

print('-'*47)
print('|'+' PILIH BAHASA :'+'|'.rjust(31))
print('-'*47)
print('|'+'1.'+'|'+ ' Bahasa Indonesia'+'|'.rjust(26))
print('|'+'2.'+'|'+ ' English'+'|'.rjust(35))
print('|'+'3.'+'|'+ ' Sulawesi '+'|'.rjust(33))
print('-'*47)


language_option = int(input('\nSilahkan pilih bahasa : '))
os.system('cls')

if check_pin():  # Memeriksa PIN
    os.system('cls')

    if language_option == 1 :
        bahasa_indo()
    elif language_option == 2 :
        bahasa_inggris()
    elif language_option == 3 :
        bahasa_sulawesi()
    else :
        print('Pilihan bahasa tidak valid.')
else :
    print('Kartu ATM Anda diblokir karena melebihi batas percobaan PIN yang salah.')
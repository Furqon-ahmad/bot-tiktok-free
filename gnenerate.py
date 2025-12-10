import random
import string
import sys
from colorama import init, Fore, Style

# Inisialisasi Colorama
init(autoreset=True)

def generate_random_string(length=16, use_letters=True, use_digits=True, use_symbols=True):
    """
    Menghasilkan string acak dengan panjang dan karakter yang ditentukan.
    """
    # Mengumpulkan semua karakter yang diizinkan berdasarkan parameter
    characters = ''
    if use_letters:
        # Menambahkan huruf kecil (a-z) dan huruf besar (A-Z)
        characters += string.ascii_letters
    if use_digits:
        # Menambahkan angka (0-9)
        characters += string.digits
    if use_symbols:
        # Menambahkan simbol (misalnya !@#$%^&*)
        # Di sini kita gunakan string.punctuation yang mencakup banyak simbol umum
        characters += string.punctuation
    
    # Menghapus karakter yang mungkin menyebabkan masalah (misalnya spasi, kutip tunggal/ganda)
    # Anda bisa menyesuaikan ini
    characters = characters.replace(' ', '').replace("'", '').replace('"', '')

    if not characters:
        return "" # Mengembalikan string kosong jika tidak ada karakter yang dipilih
        
    # Menggunakan random.choice untuk memilih karakter secara acak sebanyak 'length'
    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string

def main():
    """
    Fungsi utama untuk interaksi dengan pengguna dan menampilkan hasil.
    """
    print(f"{Fore.CYAN}=====================================================")
    print(f"{Fore.CYAN}|    {Fore.WHITE}{Style.BRIGHT}RANDOM STRING GENERATOR (generate.py){Fore.CYAN}    |")
    print(f"{Fore.CYAN}====================================================={Style.RESET_ALL}\n")
    
    try:
        # 1. Menentukan Panjang String
        length = int(input(f"{Fore.GREEN}[?] Masukkan panjang string yang diinginkan (default: 16): {Style.RESET_ALL}") or 16)
        
        if length <= 0:
            print(f"{Fore.RED}[!] Panjang harus lebih besar dari 0.")
            sys.exit()

        # 2. Menentukan Pilihan Karakter
        use_letters = input(f"{Fore.YELLOW}[?] Sertakan huruf (a-z, A-Z)? (Y/n, default: Y): {Style.RESET_ALL}").strip().lower() != 'n'
        use_digits = input(f"{Fore.YELLOW}[?] Sertakan angka (0-9)? (Y/n, default: Y): {Style.RESET_ALL}").strip().lower() != 'n'
        use_symbols = input(f"{Fore.YELLOW}[?] Sertakan simbol (!@#$ dll)? (Y/n, default: Y): {Style.RESET_ALL}").strip().lower() != 'n'
        
        if not (use_letters or use_digits or use_symbols):
            print(f"{Fore.RED}[!] Harus memilih setidaknya satu jenis karakter!")
            sys.exit()
            
        # 3. Menghasilkan String
        random_key = generate_random_string(length, use_letters, use_digits, use_symbols)
        
        # 4. Menampilkan Hasil
        print(f"\n{Fore.CYAN}-----------------------------------------------------")
        print(f"{Fore.GREEN}[+] String Acak Berhasil Dibuat ({length} karakter):")
        print(f"{Fore.WHITE}{Style.BRIGHT}{random_key}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}-----------------------------------------------------\n")
        
    except ValueError:
        print(f"{Fore.RED}[!] Input tidak valid. Harap masukkan angka untuk panjang string.")
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Operasi dibatalkan oleh pengguna.")

if __name__ == "__main__":
    main()
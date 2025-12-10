import requests, sys, json, uuid, time, os
from colorama import init, Fore, Back, Style

# --- Setup Tampilan ---
os.system('cls' if os.name=='nt' else 'clear')
init(autoreset=True) 

# --- Konstanta & Fungsi Visual ---
API = "https://zefame-free.com/api_free.php?action=config"

# --- MODIFIKASI DIMULAI DI SINI ---
# Tentukan TOKEN RAHASIA kamu di sini
# Kamu bisa ganti dengan kombinasi huruf/angka yang unik
SECRET_TOKEN = "St44&|$Jk[um-vDvsP={f)YrG}ggFpmOMy9q" 
MAX_ATTEMPTS = 3 # Batas maksimal percobaan

def print_status(text, type='info'):
    if type == 'info':
        print(f"{Fore.CYAN}[*] {text}{Style.RESET_ALL}")
    elif type == 'success':
        print(f"{Fore.GREEN}[+] {text}{Style.RESET_ALL}")
    elif type == 'error':
        print(f"{Fore.RED}[!] {text}{Style.RESET_ALL}")
    elif type == 'wait':
        print(f"{Fore.YELLOW}[~] {text}{Style.RESET_ALL}")

def authenticate_user():
    """Meminta dan memvalidasi token akses"""
    print(f"\n{Fore.YELLOW}*** AUTHENTICATION REQUIRED ***{Style.RESET_ALL}")
    
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        # Menggunakan getpass agar input token tidak terlihat di layar
        # Namun, karena getpass membutuhkan library tambahan, kita pakai input biasa dulu.
        # Jika ingin lebih aman, install dan gunakan library 'getpass'.
        
        user_input = input(f"{Fore.YELLOW}[?] Enter Access Token ({MAX_ATTEMPTS - attempts} attempts left): {Style.RESET_ALL}").strip()
        
        if user_input == SECRET_TOKEN:
            print_status("Access Granted. Loading services...", "success")
            return True
        else:
            attempts += 1
            print_status("Invalid Token. Try again.", "error")
            
    print_status(f"Maximum attempts reached. Access denied.", "error")
    sys.exit()

# Fungsi Banner dan Countdown tetap sama (dihilangkan untuk fokus pada token)
# ...

def print_banner():
    print(f"{Fore.MAGENTA}========================================================")
    print(f"{Fore.MAGENTA}|             {Fore.WHITE}{Style.BRIGHT}TIKTOK BOOSTER INTERFACE{Fore.MAGENTA}                 |")
    print(f"{Fore.MAGENTA}|             {Fore.CYAN}Enhanced UI Version{Fore.MAGENTA}                      |")
    print(f"{Fore.MAGENTA}========================================================{Style.RESET_ALL}")
    print()

def animated_countdown(seconds):
    """Menampilkan countdown timer yang berjalan mundur"""
    try:
        seconds = int(seconds)
        while seconds > 0:
            m, s = divmod(seconds, 60)
            timer = '{:02d}:{:02d}'.format(m, s)
            sys.stdout.write(f"\r{Fore.YELLOW}[~] Cooldown: {timer} {Style.RESET_ALL}")
            sys.stdout.flush()
            time.sleep(1)
            seconds -= 1
        sys.stdout.write(f"\r{Fore.GREEN}[+] Ready for next request!             {Style.RESET_ALL}\n")
    except KeyboardInterrupt:
        sys.exit()

# --- MODIFIKASI SELESAI DI SINI ---

names = {
    229: "TikTok Views",
    228: "TikTok Followers",
    232: "TikTok Free Likes",
    235: "TikTok Free Shares",
    236: "TikTok Free Favorites"
}

# --- Logika Utama (Dengan Pengecekan Token) ---

print_banner()

# Panggil fungsi otentikasi
if not authenticate_user():
    sys.exit() # Jika otentikasi gagal, script akan keluar.

print_status("Loading configuration...", "info")

if len(sys.argv) > 1:
    with open(sys.argv[1]) as f:
        data = json.load(f)
else:
    try:
        data = requests.get(API).json()
    except Exception as e:
        print_status(f"Connection Error: {e}", "error")
        sys.exit()

services = data.get('data', {}).get('tiktok', {}).get('services', [])

print(f"\n{Fore.WHITE}{Style.BRIGHT}AVAILABLE SERVICES:{Style.RESET_ALL}")
print(f"{Fore.WHITE}--------------------------------------------------------")
print(f"{'No.':<4} | {'Service Name':<22} | {'Status':<10} | {'Rate'}")
print(f"{Fore.WHITE}--------------------------------------------------------")

for i, service in enumerate(services, 1):
    sid = service.get('id')
    name = names.get(sid, service.get('name', '').strip())
    
    if len(name) > 20: name = name[:17] + "..."
    
    rate = service.get('description', '').strip()
    if rate:
        rate = rate.replace('vues', 'views').replace('partages', 'shares').replace('favoris', 'favorites')
    
    status_text = "WORKING" if service.get('available') else "DOWN"
    status_color = Fore.GREEN if service.get('available') else Fore.RED
    
    print(f"{Fore.WHITE}{i:<4} | {Fore.YELLOW}{name:<22}{Fore.WHITE} | {status_color}{status_text:<10}{Fore.WHITE} | {Fore.CYAN}{rate}")

print(f"{Fore.WHITE}--------------------------------------------------------\n")

choice = input(f"{Fore.GREEN}[?] Select number (Enter to exit): {Style.RESET_ALL}").strip()
if not choice:
    sys.exit()

try:
    idx = int(choice)
    if idx < 1 or idx > len(services):
        print_status('Number out of range', 'error')
        sys.exit()
except ValueError:
    print_status('Invalid input', 'error')
    sys.exit()

selected = services[idx-1]
print_status(f"Selected: {names.get(selected.get('id'), 'Unknown')}", "success")

video_link = input(f"{Fore.GREEN}[?] Enter video link: {Style.RESET_ALL}")

print_status("Verifying Video ID...", "info")
try:
    id_check = requests.post("https://zefame-free.com/api_free.php?", data={"action": "checkVideoId", "link": video_link})
    video_id = id_check.json().get("data", {}).get("videoId")
    
    if not video_id:
        print_status("Failed to get Video ID. Check link.", "error")
        sys.exit()
        
    print_status(f"Parsed Video ID: {video_id}", "success")
except Exception as e:
    print_status(f"Error parsing ID: {e}", "error")
    sys.exit()

print(f"\n{Fore.MAGENTA}=== STARTING INJECTION LOOP ==={Style.RESET_ALL}")

while True:
    try:
        order = requests.post("https://zefame-free.com/api_free.php?action=order", 
                            data={"service": selected.get('id'), 
                                  "link": video_link, 
                                  "uuid": str(uuid.uuid4()), 
                                  "videoId": video_id})
        result = order.json()
        
        message = result.get('message', 'Unknown response')
        data_resp = result.get('data', {})
        
        if result.get('success') or (isinstance(data_resp, dict) and not result.get('error')):
            print_status(f"Success! {message}", "success")
        else:
            print_status(f"Response: {message}", "info")

        wait = result.get("data", {}).get("nextAvailable")
        
        if wait:
            try:
                wait = float(wait)
                current_time = time.time()
                if wait > current_time:
                    remaining = int(wait - current_time + 1)
                    animated_countdown(remaining)
                else:
                    time.sleep(2)
            except ValueError:
                pass
        else:
            time.sleep(5)
            
    except Exception as e:
        print_status(f"Loop Error: {e}", "error")
        time.sleep(5)
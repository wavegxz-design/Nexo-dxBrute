import time
import random
import string
import os
import sys
from datetime import datetime

# --- SISTEMA DE IDIOMAS ---
LANG = {
    'es': {
        'banner_by': 'By: BLACKNIXU',
        'banner_version': 'Version: v2.3 (Multi-idioma)',
        'select_lang': 'Selecciona tu idioma / Select your language',
        'spanish': 'Español',
        'english': 'English',
        'login_title': 'Inicia sesión para continuar',
        'password_prompt': 'Contraseña',
        'wrong_pass': 'Contraseña incorrecta. Intento',
        'too_many_attempts': 'Demasiados intentos fallidos. Saliendo...',
        'starting_attack': 'Iniciando ataque de fuerza bruta...',
        'generator': 'Generador',
        'target': 'OBJETIVO DE ATAQUE',
        'platform': 'Plataforma',
        'user': 'Usuario',
        'stats': 'ESTADÍSTICAS EN TIEMPO REAL',
        'total_attempts': 'Intentos totales',
        'database': 'Base de datos',
        'current_speed': 'Velocidad actual',
        'active_time': 'Tiempo activo',
        'remaining_time': 'Tiempo restante',
        'success_attempts': 'Intentos exitosos',
        'failed_attempts': 'Intentos fallidos',
        'progress': 'PROGRESO DEL ATAQUE',
        'testing_pass': 'PROBANDO CONTRASEÑA',
        'attempts_log': 'REGISTRO DE INTENTOS',
        'id_col': '#ID',
        'password_col': 'CONTRASEÑA',
        'status_col': 'ESTADO',
        'access_granted': '✓ ACCESO CONCEDIDO',
        'access_denied': '✗ ACCESO DENEGADO',
        'stop_attack': 'Detener ataque',
        'pass_found': '¡CONTRASEÑA ENCONTRADA!',
        'password': 'Contraseña',
        'generator_used': 'Generador usado',
        'attempts_made': 'Intentos realizados',
        'total_time': 'Tiempo total',
        'avg_speed': 'Velocidad promedio',
        'attack_stopped': 'Ataque detenido por el usuario',
        'select_generator': 'SELECCIONA EL GENERADOR DE CONTRASEÑAS',
        'auto_mode': 'AUTO (Todos)',
        'generator_info': 'Cada generador simula patrones de contraseñas específicos',
        'auto_info': 'AUTO probará con todos los generadores secuencialmente',
        'select_platform': 'SELECCIONA LA PLATAFORMA OBJETIVO',
        'exit': 'Salir',
        'goodbye': '¡Hasta luego!',
        'invalid_option': 'Opción inválida. Intenta de nuevo.',
        'target_user': 'Usuario objetivo',
        'target_email': 'Email objetivo',
        'email': 'Email',
        'must_enter': 'Debes ingresar un',
        'select_speed': 'SELECCIONA LA VELOCIDAD DE ATAQUE',
        'slow': 'Lenta',
        'medium': 'Media',
        'fast': 'Rápida',
        'very_fast': 'Muy Rápida',
        'extreme': 'Extrema',
        'auto_testing': 'MODO AUTO: Probando con',
    },
    'en': {
        'banner_by': 'By: BLACKNIXU',
        'banner_version': 'Version: v2.3 (Multi-language)',
        'select_lang': 'Selecciona tu idioma / Select your language',
        'spanish': 'Español',
        'english': 'English',
        'login_title': 'Login to continue',
        'password_prompt': 'Password',
        'wrong_pass': 'Wrong password. Attempt',
        'too_many_attempts': 'Too many failed attempts. Exiting...',
        'starting_attack': 'Starting brute force attack...',
        'generator': 'Generator',
        'target': 'ATTACK TARGET',
        'platform': 'Platform',
        'user': 'User',
        'stats': 'REAL-TIME STATISTICS',
        'total_attempts': 'Total attempts',
        'database': 'Database',
        'current_speed': 'Current speed',
        'active_time': 'Active time',
        'remaining_time': 'Remaining time',
        'success_attempts': 'Successful attempts',
        'failed_attempts': 'Failed attempts',
        'progress': 'ATTACK PROGRESS',
        'testing_pass': 'TESTING PASSWORD',
        'attempts_log': 'ATTEMPTS LOG',
        'id_col': '#ID',
        'password_col': 'PASSWORD',
        'status_col': 'STATUS',
        'access_granted': '✓ ACCESS GRANTED',
        'access_denied': '✗ ACCESS DENIED',
        'stop_attack': 'Stop attack',
        'pass_found': 'PASSWORD FOUND!',
        'password': 'Password',
        'generator_used': 'Generator used',
        'attempts_made': 'Attempts made',
        'total_time': 'Total time',
        'avg_speed': 'Average speed',
        'attack_stopped': 'Attack stopped by user',
        'select_generator': 'SELECT PASSWORD GENERATOR',
        'auto_mode': 'AUTO (All)',
        'generator_info': 'Each generator simulates specific password patterns',
        'auto_info': 'AUTO will test with all generators sequentially',
        'select_platform': 'SELECT TARGET PLATFORM',
        'exit': 'Exit',
        'goodbye': 'Goodbye!',
        'invalid_option': 'Invalid option. Try again.',
        'target_user': 'Target user',
        'target_email': 'Target email',
        'email': 'Email',
        'must_enter': 'You must enter a',
        'select_speed': 'SELECT ATTACK SPEED',
        'slow': 'Slow',
        'medium': 'Medium',
        'fast': 'Fast',
        'very_fast': 'Very Fast',
        'extreme': 'Extreme',
        'auto_testing': 'AUTO MODE: Testing with',
    }
}

current_lang = 'es'  # Idioma por defecto

def t(key):
    """Traduce una clave según el idioma actual"""
    return LANG[current_lang].get(key, key)

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RESET = '\033[0m'
    CLEAR = '\033[2J\033[H'

def clear_screen():
    os.system('clear' if os.name != 'nt' else 'cls')

def print_banner():
    banner = f"""
{Colors.CYAN}{Colors.BOLD}
▄▄▄▄· ▄▄▄  ▄• ▄▌▄▄▄▄▄▄▄▄ .    ·▄▄▄▄        ▄▄▄   ▄▄· ▄▄▄ .
▐█ ▀█▪▀▄ █·█▪██▌•██  ▀▄.▀·    ██▪ ██ ▪     ▀▄ █·▐█ ▌▪▀▄.▀·
▐█▀▀█▄▐▀▀▄ █▌▐█▌ ▐█.▪▐▀▀▪▄    ▐█· ▐█▌ ▄█▀▄ ▐▀▀▄ ██ ▄▄▐▀▀▪▄
██▄▪▐█▐█•█▌▐█▄█▌ ▐█▌·▐█▄▄▌    ██. ██ ▐█▌.▐▌▐█•█▌▐███▌▐█▄▄▌
·▀▀▀▀ .▀  ▀ ▀▀▀  ▀▀▀  ▀▀▀     ▀▀▀▀▀•  ▀█▄▀▪.▀  ▀·▀▀▀  ▀▀▀ 
{Colors.RESET}
{Colors.GREEN}                    ┌─────────────────────┐
                    │   {t('banner_by')}    │
                    └─────────────────────┘{Colors.RESET}
{Colors.YELLOW}                     {t('banner_version')}{Colors.RESET}
"""
    print(banner)

def select_language():
    """Selección de idioma al inicio"""
    clear_screen()
    
    lang_banner = f"""
{Colors.MAGENTA}{Colors.BOLD}
  ██████  ██████  ██    ██ ████████ ███████     ███████  ██████  ██████   ██████ ███████ 
  ██   ██ ██   ██ ██    ██    ██    ██          ██      ██    ██ ██   ██ ██      ██      
  ██████  ██████  ██    ██    ██    █████       █████   ██    ██ ██████  ██      █████   
  ██   ██ ██   ██ ██    ██    ██    ██          ██      ██    ██ ██   ██ ██      ██      
  ██████  ██   ██  ██████     ██    ███████     ██       ██████  ██   ██  ██████ ███████ 
{Colors.RESET}
    """
    print(lang_banner)
    print(f"\n{Colors.CYAN}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.CYAN}║{Colors.BOLD}{Colors.WHITE}       {t('select_lang')}            {Colors.CYAN}║{Colors.RESET}")
    print(f"{Colors.CYAN}╠═══════════════════════════════════════════════════════════╣{Colors.RESET}")
    print(f"{Colors.CYAN}║{Colors.RESET}  {Colors.GREEN}[1]{Colors.RESET} 🇪🇸 {Colors.BOLD}Español{Colors.RESET}                                            {Colors.CYAN}║{Colors.RESET}")
    print(f"{Colors.CYAN}║{Colors.RESET}  {Colors.BLUE}[2]{Colors.RESET} 🇬🇧 {Colors.BOLD}English{Colors.RESET}                                            {Colors.CYAN}║{Colors.RESET}")
    print(f"{Colors.CYAN}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    choice = input(f"\n{Colors.YELLOW}┌─[Language/Idioma]\n└──> {Colors.RESET}").strip()
    
    global current_lang
    if choice == '1':
        current_lang = 'es'
    elif choice == '2':
        current_lang = 'en'
    else:
        current_lang = 'es'
    
    return current_lang

def format_time(seconds):
    if seconds < 60:
        return f"{int(seconds)}s"
    elif seconds < 3600:
        return f"{int(seconds // 60)}m {int(seconds % 60)}s"
    else:
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        return f"{hours}h {minutes}m {secs}s"

def format_number(num):
    return f"{num:,}".replace(',', '.')

def create_progress_bar(progress, width=40):
    filled = int(width * progress / 100)
    bar = '█' * filled + '░' * (width - filled)
    return f"{Colors.GREEN}[{bar}]{Colors.RESET} {Colors.YELLOW}{progress:.4f}%{Colors.RESET}"

class PasswordGenerators:
    @staticmethod
    def random_basic(length=8):
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        return ''.join(random.choice(chars) for _ in range(random.randint(4, length)))
    
    @staticmethod
    def eset_style():
        length = random.randint(12, 16)
        password = []
        password.append(random.choice(string.ascii_uppercase))
        password.append(random.choice(string.ascii_lowercase))
        password.append(random.choice(string.digits))
        password.append(random.choice("!@#$%^&*"))
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        password.extend(random.choice(chars) for _ in range(length - 4))
        random.shuffle(password)
        return ''.join(password)
    
    @staticmethod
    def strong_style():
        length = random.randint(14, 20)
        symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        password = []
        for _ in range(length // 4):
            password.append(random.choice(string.ascii_uppercase))
        for _ in range(length // 4):
            password.append(random.choice(string.ascii_lowercase))
        for _ in range(length // 4):
            password.append(random.choice(string.digits))
        remaining = length - len(password)
        password.extend(random.choice(symbols) for _ in range(remaining))
        random.shuffle(password)
        return ''.join(password)
    
    @staticmethod
    def google_style():
        length = random.randint(12, 15)
        chars = string.ascii_letters + string.digits + "!@#$%&*"
        password = []
        password.append(random.choice(string.ascii_uppercase))
        password.extend(random.choice(chars) for _ in range(length - 1))
        return ''.join(password)
    
    @staticmethod
    def keepass_style():
        length = random.randint(16, 24)
        all_chars = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?/~`"
        return ''.join(random.choice(all_chars) for _ in range(length))
    
    @staticmethod
    def nordpass_style():
        length = random.randint(12, 18)
        password = []
        for i in range(length):
            if i % 3 == 0:
                password.append(random.choice(string.ascii_uppercase))
            elif i % 3 == 1:
                password.append(random.choice(string.digits))
            else:
                password.append(random.choice(string.ascii_lowercase + "!@#$%"))
        return ''.join(password)
    
    @staticmethod
    def avast_style():
        length = random.randint(10, 14)
        segments = []
        for _ in range(3):
            seg = random.choice(string.ascii_uppercase)
            seg += ''.join(random.choice(string.ascii_lowercase) for _ in range(2))
            seg += random.choice(string.digits)
            segments.append(seg)
        password = ''.join(segments)[:length]
        return password + random.choice("!@#$%")
    
    @staticmethod
    def proton_style():
        length = random.randint(16, 20)
        all_chars = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?"
        password = []
        password.append(random.choice(string.ascii_uppercase))
        password.append(random.choice(string.ascii_lowercase))
        password.append(random.choice(string.digits))
        password.append(random.choice("!@#$%^&*"))
        password.extend(random.choice(all_chars) for _ in range(length - 4))
        random.shuffle(password)
        return ''.join(password)

def initial_login():
    """Pantalla de login con contraseña 'nexo'"""
    clear_screen()
    
    login_banner = f"""
{Colors.MAGENTA}{Colors.BOLD}
  ███    ██ ███████ ██   ██  ██████  
  ████   ██ ██       ██ ██  ██    ██ 
  ██ ██  ██ █████     ███   ██    ██ 
  ██  ██ ██ ██       ██ ██  ██    ██ 
  ██   ████ ███████ ██   ██  ██████  
{Colors.RESET}
    {Colors.YELLOW}by nixu dev{Colors.RESET}
    """
    print(login_banner)
    print(f"\n{Colors.CYAN}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.CYAN}║{Colors.BOLD}{Colors.WHITE}       {t('login_title'):^50}       {Colors.CYAN}║{Colors.RESET}")
    print(f"{Colors.CYAN}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    attempts = 0
    while attempts < 3:
        password = input(f"\n{Colors.YELLOW}┌─[{Colors.WHITE}{t('password_prompt')}{Colors.YELLOW}]\n└──> {Colors.RESET}").strip()
        if password == "nexo":
            print(f"\n{Colors.GREEN}✓ {t('access_granted')}{Colors.RESET}")
            time.sleep(1)
            return True
        else:
            attempts += 1
            print(f"{Colors.RED}[!] {t('wrong_pass')} {attempts}/3{Colors.RESET}")
            time.sleep(1)
            clear_screen()
            print(login_banner)
            print(f"\n{Colors.CYAN}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
            print(f"{Colors.CYAN}║{Colors.BOLD}{Colors.WHITE}       {t('login_title'):^50}       {Colors.CYAN}║{Colors.RESET}")
            print(f"{Colors.CYAN}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}")

    print(f"\n{Colors.RED}[!] {t('too_many_attempts')}{Colors.RESET}")
    sys.exit(0)

def simulate_attack(platform, username, speed, generator_name, generator_func):
    total_passwords = 1000000000
    attempt_count = 0
    start_time = time.time()
    recent_attempts = []
    success_count = 0
    failed_count = 0
    last_display_time = 0.0
    display_interval = 1.0 / 25 

    target_configs = {("Instagram", "kim_azg"): ("aoMO45nLpy-Ptwr", 180)}
    target_key = (platform, username.lower())
    target_password = None
    target_time = None
    
    if target_key in target_configs:
        target_password, target_time = target_configs[target_key]
    
    clear_screen()
    print_banner()
    print(f"\n{Colors.YELLOW}[!] {t('starting_attack')}{Colors.RESET}")
    print(f"{Colors.CYAN}[+] {t('generator')}: {Colors.WHITE}{generator_name}{Colors.RESET}")
    time.sleep(1)
    
    try:
        while True:
            current_password = generator_func()
            attempt_count += 1
            failed_count += 1
            
            elapsed_time = time.time() - start_time
            attempts_per_sec = attempt_count / elapsed_time if elapsed_time > 0 else 0
            progress = (attempt_count / total_passwords) * 100
            remaining = (total_passwords - attempt_count) / attempts_per_sec if attempts_per_sec > 0 else 0
            
            if target_password and elapsed_time >= target_time and success_count == 0:
                current_password = target_password
                success_count = 1
                failed_count -= 1
            
            recent_attempts.append(current_password)
            if len(recent_attempts) > 12:
                recent_attempts.pop(0)

            current_time = time.time()
            if current_time - last_display_time >= display_interval:
                
                print(f"\r{Colors.CLEAR}", end='')
                print_banner()
                
                print(f"\n{Colors.CYAN}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
                print(f"{Colors.CYAN}║{Colors.BOLD}{Colors.WHITE}       🎯 {t('target'):^50}    {Colors.CYAN}║{Colors.RESET}")
                print(f"{Colors.CYAN}╠═══════════════════════════════════════════════════════════╣{Colors.RESET}")
                print(f"{Colors.CYAN}║{Colors.RESET}  {Colors.GREEN}►{Colors.RESET} {t('platform')}: {Colors.WHITE}{Colors.BOLD}{platform:<44}{Colors.CYAN}║{Colors.RESET}")
                print(f"{Colors.CYAN}║{Colors.RESET}  {Colors.GREEN}►{Colors.RESET} {t('user')}:    {Colors.WHITE}{Colors.BOLD}{username:<44}{Colors.CYAN}║{Colors.RESET}")
                print(f"{Colors.CYAN}║{Colors.RESET}  {Colors.GREEN}►{Colors.RESET} {t('generator')}:  {Colors.YELLOW}{Colors.BOLD}{generator_name:<44}{Colors.CYAN}║{Colors.RESET}")
                print(f"{Colors.CYAN}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}\n")
                
                print(f"{Colors.GREEN}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
                print(f"{Colors.GREEN}║{Colors.BOLD}{Colors.WHITE}       📊 {t('stats'):^50}  {Colors.GREEN}║{Colors.RESET}")
                print(f"{Colors.GREEN}╠═══════════════════════════════════════════════════════════╣{Colors.RESET}")
                print(f"{Colors.GREEN}║{Colors.RESET}  {Colors.YELLOW}▸{Colors.RESET} {t('total_attempts')}:  {Colors.WHITE}{Colors.BOLD}{format_number(attempt_count):>15}{Colors.GREEN}              ║{Colors.RESET}")
                print(f"{Colors.GREEN}║{Colors.RESET}  {Colors.YELLOW}▸{Colors.RESET} {t('database')}:     {Colors.WHITE}{Colors.BOLD}{format_number(total_passwords):>15}{Colors.GREEN}              ║{Colors.RESET}")
                print(f"{Colors.GREEN}║{Colors.RESET}  {Colors.YELLOW}▸{Colors.RESET} {t('current_speed')}:  {Colors.CYAN}{Colors.BOLD}{int(attempts_per_sec):>10} pass/s{Colors.GREEN}              ║{Colors.RESET}")
                print(f"{Colors.GREEN}║{Colors.RESET}  {Colors.YELLOW}▸{Colors.RESET} {t('active_time')}:     {Colors.MAGENTA}{Colors.BOLD}{format_time(elapsed_time):>15}{Colors.GREEN}              ║{Colors.RESET}")
                print(f"{Colors.GREEN}║{Colors.RESET}  {Colors.YELLOW}▸{Colors.RESET} {t('remaining_time')}:   {Colors.MAGENTA}{Colors.BOLD}{format_time(remaining):>15}{Colors.GREEN}              ║{Colors.RESET}")
                print(f"{Colors.GREEN}║{Colors.RESET}  {Colors.YELLOW}▸{Colors.RESET} {t('success_attempts')}: {Colors.GREEN}{Colors.BOLD}{format_number(success_count):>15}{Colors.GREEN}              ║{Colors.RESET}")
                print(f"{Colors.GREEN}║{Colors.RESET}  {Colors.YELLOW}▸{Colors.RESET} {t('failed_attempts')}: {Colors.RED}{Colors.BOLD}{format_number(failed_count):>15}{Colors.GREEN}              ║{Colors.RESET}")
                print(f"{Colors.GREEN}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}\n")
                
                print(f"{Colors.BLUE}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
                print(f"{Colors.BLUE}║{Colors.BOLD}{Colors.WHITE}       ⚡ {t('progress'):^50}  {Colors.BLUE}║{Colors.RESET}")
                print(f"{Colors.BLUE}╠═══════════════════════════════════════════════════════════╣{Colors.RESET}")
                print(f"{Colors.BLUE}║{Colors.RESET}  {create_progress_bar(progress, 50):75}  {Colors.BLUE}║{Colors.RESET}")
                print(f"{Colors.BLUE}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}\n")
                
                print(f"{Colors.MAGENTA}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
                print(f"{Colors.MAGENTA}║{Colors.BOLD}{Colors.WHITE}       🔑 {t('testing_pass'):^50}  {Colors.MAGENTA}║{Colors.RESET}")
                print(f"{Colors.MAGENTA}╠═══════════════════════════════════════════════════════════╣{Colors.RESET}")
                print(f"{Colors.MAGENTA}║{Colors.RESET}  {Colors.CYAN}→→→{Colors.RESET}  {Colors.WHITE}{Colors.BOLD}{current_password:<50}{Colors.MAGENTA}    ║{Colors.RESET}")
                print(f"{Colors.MAGENTA}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}\n")
                
                print(f"{Colors.YELLOW}╔═══════════╤═════════════════════════╤═════════════════════════╗{Colors.RESET}")
                print(f"{Colors.YELLOW}║{Colors.RESET} {Colors.BOLD}{t('id_col'):^10}{Colors.YELLOW}│{Colors.RESET} {Colors.BOLD}{t('password_col'):^23}{Colors.YELLOW}│{Colors.RESET} {Colors.BOLD}{t('status_col'):^23}{Colors.YELLOW}║{Colors.RESET}")
                print(f"{Colors.YELLOW}╠═══════════╪═════════════════════════╪═════════════════════════╣{Colors.RESET}")
                
                for i, pwd in enumerate(reversed(recent_attempts[-10:]), 1):
                    attempt_id = attempt_count - i + 1
                    status_text = t('access_granted') if pwd == target_password and success_count == 1 else t('access_denied')
                    status = f"{Colors.GREEN}{status_text}{Colors.RESET}" if pwd == target_password else f"{Colors.RED}{status_text}{Colors.RESET}"
                    pwd_display = pwd[:23] if len(pwd) <= 23 else pwd[:20] + "..."
                    print(f"{Colors.YELLOW}║{Colors.RESET} {Colors.WHITE}{attempt_id:>8} {Colors.YELLOW}│{Colors.RESET} {Colors.CYAN}{pwd_display:<23}{Colors.YELLOW}│{Colors.RESET} {status:38} {Colors.YELLOW}║{Colors.RESET}")
                
                print(f"{Colors.YELLOW}╚═══════════╧═════════════════════════╧═════════════════════════╝{Colors.RESET}\n")
                print(f"{Colors.RED}[{Colors.WHITE}Ctrl+C{Colors.RED}]{Colors.RESET} {t('stop_attack')}")

                last_display_time = current_time 
                
            if success_count == 1:
                time.sleep(2)
                clear_screen()
                print_banner()

                print(f"\n{Colors.GREEN}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
                print(f"{Colors.GREEN}║{Colors.BOLD}{Colors.WHITE}       🎉 {t('pass_found'):^50}  {Colors.GREEN}║{Colors.RESET}")
                print(f"{Colors.GREEN}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}\n")
                print(f"{Colors.CYAN}┌──────────────────────────────────────────────┐{Colors.RESET}")
                print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.GREEN}►{Colors.RESET} {t('platform')}: {Colors.WHITE}{Colors.BOLD}{platform:<29}{Colors.CYAN}│{Colors.RESET}")
                print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.GREEN}►{Colors.RESET} {t('user')}: {Colors.WHITE}{Colors.BOLD}{username:<32}{Colors.CYAN}│{Colors.RESET}")
                print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.GREEN}►{Colors.RESET} {t('password')}: {Colors.GREEN}{Colors.BOLD}{target_password:<30}{Colors.CYAN}│{Colors.RESET}")
                print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.GREEN}►{Colors.RESET} {t('generator_used')}: {Colors.YELLOW}{Colors.BOLD}{generator_name:<24}{Colors.CYAN}│{Colors.RESET}")
                print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.GREEN}►{Colors.RESET} {t('attempts_made')}: {Colors.WHITE}{Colors.BOLD}{format_number(attempt_count):<19}{Colors.CYAN}│{Colors.RESET}")
                print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.GREEN}►{Colors.RESET} {t('total_time')}: {Colors.WHITE}{Colors.BOLD}{format_time(elapsed_time):<27}{Colors.CYAN}│{Colors.RESET}")
                print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.GREEN}►{Colors.RESET} {t('avg_speed')}: {Colors.WHITE}{Colors.BOLD}{int(attempts_per_sec)} pass/s{Colors.RESET:<17}{Colors.CYAN}│{Colors.RESET}")
                print(f"{Colors.CYAN}└──────────────────────────────────────────────┘{Colors.RESET}\n")
                break
            
            if speed > 100:
                time.sleep(1.0 / speed)
            else:
                time.sleep(1.0 / speed) 
            
    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
        print(f"{Colors.YELLOW}║{Colors.BOLD}       [!] {t('attack_stopped'):^50}  {Colors.YELLOW}║{Colors.RESET}")
        print(f"{Colors.RED}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}\n")
        print(f"{Colors.CYAN}┌──────────────────────────────────────────────┐{Colors.RESET}")
        print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.GREEN}►{Colors.RESET} {t('attempts_made')}: {Colors.WHITE}{Colors.BOLD}{format_number(attempt_count):<19}{Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.GREEN}►{Colors.RESET} {t('total_time')}: {Colors.WHITE}{Colors.BOLD}{format_time(elapsed_time):<27}{Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.GREEN}►{Colors.RESET} {t('avg_speed')}: {Colors.WHITE}{Colors.BOLD}{int(attempts_per_sec)} pass/s{Colors.RESET:<17}{Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.CYAN}└──────────────────────────────────────────────┘{Colors.RESET}\n")

def run_auto_attack(platform, username, speed):
    all_generators = [
        ('Random Básico', PasswordGenerators.random_basic),
        ('ESET', PasswordGenerators.eset_style),
        ('Strong', PasswordGenerators.strong_style),
        ('Google Password Manager', PasswordGenerators.google_style),
        ('KeePass', PasswordGenerators.keepass_style),
        ('NordPass', PasswordGenerators.nordpass_style),
        ('Avast Passwords', PasswordGenerators.avast_style),
        ('Proton Pass', PasswordGenerators.proton_style),
    ]
    
    for i, (name, func) in enumerate(all_generators, 1):
        clear_screen()
        print_banner()
        print(f"\n{Colors.CYAN}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
        print(f"{Colors.CYAN}║{Colors.BOLD}{Colors.WHITE}  🤖 {t('auto_testing')}: {name:<30}{Colors.CYAN}║{Colors.RESET}")
        print(f"{Colors.CYAN}║{Colors.BOLD}{Colors.WHITE}     [{i}/{len(all_generators)}]                                                  {Colors.CYAN}║{Colors.RESET}")
        print(f"{Colors.CYAN}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}")
        time.sleep(2)
        simulate_attack(platform, username, speed, name, func)

def select_generator():
    generators = {
        '1': ('Random Básico', PasswordGenerators.random_basic, Colors.WHITE),
        '2': ('ESET', PasswordGenerators.eset_style, Colors.BLUE),
        '3': ('Strong', PasswordGenerators.strong_style, Colors.RED),
        '4': ('Google Password Manager', PasswordGenerators.google_style, Colors.GREEN),
        '5': ('KeePass', PasswordGenerators.keepass_style, Colors.CYAN),
        '6': ('NordPass', PasswordGenerators.nordpass_style, Colors.MAGENTA),
        '7': ('Avast Passwords', PasswordGenerators.avast_style, Colors.YELLOW),
        '8': ('Proton Pass', PasswordGenerators.proton_style, Colors.GREEN),
        '9': (t('auto_mode'), None, Colors.RED),
    }
    
    clear_screen()
    print_banner()
    
    print(f"\n{Colors.GREEN}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.GREEN}║{Colors.BOLD}{Colors.WHITE}       🔐 {t('select_generator'):^50}  {Colors.GREEN}║{Colors.RESET}")
    print(f"{Colors.GREEN}╠═══════════════════════════════════════════════════════════╣{Colors.RESET}")
    
    for key, (name, _, color) in generators.items():
        icon = "🤖" if key == '9' else "🔑"
        print(f"{Colors.GREEN}║{Colors.RESET}  {color}[{key}]{Colors.RESET} {icon}  {Colors.BOLD}{name:<48}{Colors.GREEN}║{Colors.RESET}")
    
    print(f"{Colors.GREEN}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    print(f"{Colors.DIM}{t('generator_info')}{Colors.RESET}")
    print(f"{Colors.DIM}{t('auto_info')}{Colors.RESET}")
    
    choice = input(f"\n{Colors.YELLOW}┌─[{Colors.WHITE}{t('generator')}{Colors.YELLOW}]\n└──> {Colors.RESET}").strip()
    
    if choice in generators:
        return choice, generators[choice][0], generators[choice][1]
    else:
        print(f"\n{Colors.RED}[!] {t('invalid_option')}{Colors.RESET}")
        time.sleep(1)
        return select_generator()

def select_platform():
    platforms = {
        '1': ('Instagram', '📷', Colors.MAGENTA),
        '2': ('Facebook', '👤', Colors.BLUE),
        '3': ('X (Twitter)', '🐦', Colors.CYAN),
        '4': ('Roblox', '🎮', Colors.RED),
        '5': ('Gmail', '📧', Colors.YELLOW),
    }
    
    clear_screen()
    print_banner()
    
    print(f"\n{Colors.GREEN}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.GREEN}║{Colors.BOLD}{Colors.WHITE}       🎯 {t('select_platform'):^50}  {Colors.GREEN}║{Colors.RESET}")
    print(f"{Colors.GREEN}╠═══════════════════════════════════════════════════════════╣{Colors.RESET}")
    
    for key, (name, emoji, color) in platforms.items():
        print(f"{Colors.GREEN}║{Colors.RESET}  {color}[{key}]{Colors.RESET} {emoji}  {Colors.BOLD}{name:<48}{Colors.GREEN}║{Colors.RESET}")
    
    print(f"{Colors.GREEN}║{Colors.RESET}  {Colors.RED}[0]{Colors.RESET} 🚪 {Colors.DIM}{t('exit')}{Colors.RESET:<52}{Colors.GREEN}║{Colors.RESET}")
    print(f"{Colors.GREEN}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    choice = input(f"\n{Colors.YELLOW}┌─[{Colors.WHITE}{t('platform')}{Colors.YELLOW}]\n└──> {Colors.RESET}").strip()
    
    if choice == '0':
        print(f"\n{Colors.CYAN}{t('goodbye')}{Colors.RESET}\n")
        sys.exit(0)
    
    if choice in platforms:
        return platforms[choice][0]
    else:
        print(f"\n{Colors.RED}[!] {t('invalid_option')}{Colors.RESET}")
        time.sleep(1)
        return select_platform()

def get_username(platform):
    clear_screen()
    print_banner()
    
    print(f"\n{Colors.GREEN}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.GREEN}║{Colors.RESET} {Colors.CYAN}►{Colors.RESET} {t('platform')}: {Colors.WHITE}{Colors.BOLD}{platform:<45}{Colors.GREEN}║{Colors.RESET}")
    print(f"{Colors.GREEN}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    if platform == "Gmail":
        label = t('target_email')
        label_type = t('email').lower()
    else:
        label = t('target_user')
        label_type = t('user').lower()
    
    username = input(f"{Colors.YELLOW}┌─[{Colors.WHITE}{label}{Colors.YELLOW}]\n└──> {Colors.RESET}").strip()
    
    if not username:
        print(f"\n{Colors.RED}[!] {t('must_enter')} {label_type}{Colors.RESET}")
        time.sleep(1)
        return get_username(platform)
    
    return username

def select_speed():
    speeds = {
        '1': (10, t('slow'), Colors.YELLOW),
        '2': (50, t('medium'), Colors.BLUE),
        '3': (100, t('fast'), Colors.GREEN),
        '4': (500, t('very_fast'), Colors.MAGENTA),
        '5': (1000, t('extreme'), Colors.RED),
    }
    
    clear_screen()
    print_banner()
    
    print(f"\n{Colors.GREEN}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.GREEN}║{Colors.BOLD}{Colors.WHITE}       ⚡ {t('select_speed'):^50}  {Colors.GREEN}║{Colors.RESET}")
    print(f"{Colors.GREEN}╠═══════════════════════════════════════════════════════════╣{Colors.RESET}")
    
    for key, (speed_val, name, color) in speeds.items():
        bar_len = int(speed_val / 100) if speed_val <= 500 else 10
        bar = '█' * bar_len
        print(f"{Colors.GREEN}║{Colors.RESET}  {color}[{key}]{Colors.RESET} {Colors.BOLD}{name:<15}{Colors.RESET} {color}{bar:<10}{Colors.RESET} {Colors.DIM}({speed_val} pass/seg){Colors.RESET:<18}{Colors.GREEN}║{Colors.RESET}")
    
    print(f"{Colors.GREEN}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    choice = input(f"\n{Colors.YELLOW}┌─[{Colors.WHITE}{t('current_speed')}{Colors.YELLOW}]\n└──> {Colors.RESET}").strip()
    
    if choice in speeds:
        return speeds[choice][0]
    else:
        print(f"\n{Colors.RED}[!] {t('invalid_option')}{Colors.RESET}")
        time.sleep(1)
        return select_speed()

def main():
    # Selección de idioma
    select_language()
    
    # Login con contraseña
    if not initial_login():
        return
        
    try:
        platform = select_platform()
        username = get_username(platform)
        gen_choice, gen_name, gen_func = select_generator()
        speed = select_speed()
        
        if gen_choice == '9':
            run_auto_attack(platform, username, speed)
        else:
            simulate_attack(platform, username, speed, gen_name, gen_func)
        
    except Exception as e:
        print(f"\n{Colors.RED}[!] Error: {str(e)}{Colors.RESET}\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
ENDCODEimport time
import random
import string
import os
import sys
from datetime import datetime

# --- SISTEMA DE IDIOMAS ---
LANG = {
    'es': {
        'banner_by': 'By: BLACKNIXU',
        'banner_version': 'Version: v2.3 (Multi-idioma)',
        'select_lang': 'Selecciona tu idioma / Select your language',
        'spanish': 'Español',
        'english': 'English',
        'login_title': 'Inicia sesión para continuar',
        'password_prompt': 'Contraseña',
        'wrong_pass': 'Contraseña incorrecta. Intento',
        'too_many_attempts': 'Demasiados intentos fallidos. Saliendo...',
        'starting_attack': 'Iniciando ataque de fuerza bruta...',
        'generator': 'Generador',
        'target': 'OBJETIVO DE ATAQUE',
        'platform': 'Plataforma',
        'user': 'Usuario',
        'stats': 'ESTADÍSTICAS EN TIEMPO REAL',
        'total_attempts': 'Intentos totales',
        'database': 'Base de datos',
        'current_speed': 'Velocidad actual',
        'active_time': 'Tiempo activo',
        'remaining_time': 'Tiempo restante',
        'success_attempts': 'Intentos exitosos',
        'failed_attempts': 'Intentos fallidos',
        'progress': 'PROGRESO DEL ATAQUE',
        'testing_pass': 'PROBANDO CONTRASEÑA',
        'attempts_log': 'REGISTRO DE INTENTOS',
        'id_col': '#ID',
        'password_col': 'CONTRASEÑA',
        'status_col': 'ESTADO',
        'access_granted': '✓ ACCESO CONCEDIDO',
        'access_denied': '✗ ACCESO DENEGADO',
        'stop_attack': 'Detener ataque',
        'pass_found': '¡CONTRASEÑA ENCONTRADA!',
        'password': 'Contraseña',
        'generator_used': 'Generador usado',
        'attempts_made': 'Intentos realizados',
        'total_time': 'Tiempo total',
        'avg_speed': 'Velocidad promedio',
        'attack_stopped': 'Ataque detenido por el usuario',
        'select_generator': 'SELECCIONA EL GENERADOR DE CONTRASEÑAS',
        'auto_mode': 'AUTO (Todos)',
        'generator_info': 'Cada generador simula patrones de contraseñas específicos',
        'auto_info': 'AUTO probará con todos los generadores secuencialmente',
        'select_platform': 'SELECCIONA LA PLATAFORMA OBJETIVO',
        'exit': 'Salir',
        'goodbye': '¡Hasta luego!',
        'invalid_option': 'Opción inválida. Intenta de nuevo.',
        'target_user': 'Usuario objetivo',
        'target_email': 'Email objetivo',
        'email': 'Email',
        'must_enter': 'Debes ingresar un',
        'select_speed': 'SELECCIONA LA VELOCIDAD DE ATAQUE',
        'slow': 'Lenta',
        'medium': 'Media',
        'fast': 'Rápida',
        'very_fast': 'Muy Rápida',
        'extreme': 'Extrema',
        'auto_testing': 'MODO AUTO: Probando con',
    },
    'en': {
        'banner_by': 'By: BLACKNIXU',
        'banner_version': 'Version: v2.3 (Multi-language)',
        'select_lang': 'Selecciona tu idioma / Select your language',
        'spanish': 'Español',
        'english': 'English',
        'login_title': 'Login to continue',
        'password_prompt': 'Password',
        'wrong_pass': 'Wrong password. Attempt',
        'too_many_attempts': 'Too many failed attempts. Exiting...',
        'starting_attack': 'Starting brute force attack...',
        'generator': 'Generator',
        'target': 'ATTACK TARGET',
        'platform': 'Platform',
        'user': 'User',
        'stats': 'REAL-TIME STATISTICS',
        'total_attempts': 'Total attempts',
        'database': 'Database',
        'current_speed': 'Current speed',
        'active_time': 'Active time',
        'remaining_time': 'Remaining time',
        'success_attempts': 'Successful attempts',
        'failed_attempts': 'Failed attempts',
        'progress': 'ATTACK PROGRESS',
        'testing_pass': 'TESTING PASSWORD',
        'attempts_log': 'ATTEMPTS LOG',
        'id_col': '#ID',
        'password_col': 'PASSWORD',
        'status_col': 'STATUS',
        'access_granted': '✓ ACCESS GRANTED',
        'access_denied': '✗ ACCESS DENIED',
        'stop_attack': 'Stop attack',
        'pass_found': 'PASSWORD FOUND!',
        'password': 'Password',
        'generator_used': 'Generator used',
        'attempts_made': 'Attempts made',
        'total_time': 'Total time',
        'avg_speed': 'Average speed',
        'attack_stopped': 'Attack stopped by user',
        'select_generator': 'SELECT PASSWORD GENERATOR',
        'auto_mode': 'AUTO (All)',
        'generator_info': 'Each generator simulates specific password patterns',
        'auto_info': 'AUTO will test with all generators sequentially',
        'select_platform': 'SELECT TARGET PLATFORM',
        'exit': 'Exit',
        'goodbye': 'Goodbye!',
        'invalid_option': 'Invalid option. Try again.',
        'target_user': 'Target user',
        'target_email': 'Target email',
        'email': 'Email',
        'must_enter': 'You must enter a',
        'select_speed': 'SELECT ATTACK SPEED',
        'slow': 'Slow',
        'medium': 'Medium',
        'fast': 'Fast',
        'very_fast': 'Very Fast',
        'extreme': 'Extreme',
        'auto_testing': 'AUTO MODE: Testing with',
    }
}

current_lang = 'es'  # Idioma por defecto

def t(key):
    """Traduce una clave según el idioma actual"""
    return LANG[current_lang].get(key, key)

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RESET = '\033[0m'
    CLEAR = '\033[2J\033[H'

def clear_screen():
    os.system('clear' if os.name != 'nt' else 'cls')

def print_banner():
    banner = f"""
{Colors.CYAN}{Colors.BOLD}
▄▄▄▄· ▄▄▄  ▄• ▄▌▄▄▄▄▄▄▄▄ .    ·▄▄▄▄        ▄▄▄   ▄▄· ▄▄▄ .
▐█ ▀█▪▀▄ █·█▪██▌•██  ▀▄.▀·    ██▪ ██ ▪     ▀▄ █·▐█ ▌▪▀▄.▀·
▐█▀▀█▄▐▀▀▄ █▌▐█▌ ▐█.▪▐▀▀▪▄    ▐█· ▐█▌ ▄█▀▄ ▐▀▀▄ ██ ▄▄▐▀▀▪▄
██▄▪▐█▐█•█▌▐█▄█▌ ▐█▌·▐█▄▄▌    ██. ██ ▐█▌.▐▌▐█•█▌▐███▌▐█▄▄▌
·▀▀▀▀ .▀  ▀ ▀▀▀  ▀▀▀  ▀▀▀     ▀▀▀▀▀•  ▀█▄▀▪.▀  ▀·▀▀▀  ▀▀▀ 
{Colors.RESET}
{Colors.GREEN}                    ┌─────────────────────┐
                    │   {t('banner_by')}    │
                    └─────────────────────┘{Colors.RESET}
{Colors.YELLOW}                     {t('banner_version')}{Colors.RESET}
"""
    print(banner)

def select_language():
    """Selección de idioma al inicio"""
    clear_screen()
    
    lang_banner = f"""
{Colors.MAGENTA}{Colors.BOLD}
  ██████  ██████  ██    ██ ████████ ███████     ███████  ██████  ██████   ██████ ███████ 
  ██   ██ ██   ██ ██    ██    ██    ██          ██      ██    ██ ██   ██ ██      ██      
  ██████  ██████  ██    ██    ██    █████       █████   ██    ██ ██████  ██      █████   
  ██   ██ ██   ██ ██    ██    ██    ██          ██      ██    ██ ██   ██ ██      ██      
  ██████  ██   ██  ██████     ██    ███████     ██       ██████  ██   ██  ██████ ███████ 
{Colors.RESET}
    """
    print(lang_banner)
    print(f"\n{Colors.CYAN}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.CYAN}║{Colors.BOLD}{Colors.WHITE}       {t('select_lang')}            {Colors.CYAN}║{Colors.RESET}")
    print(f"{Colors.CYAN}╠═══════════════════════════════════════════════════════════╣{Colors.RESET}")
    print(f"{Colors.CYAN}║{Colors.RESET}  {Colors.GREEN}[1]{Colors.RESET} 🇪🇸 {Colors.BOLD}Español{Colors.RESET}                                            {Colors.CYAN}║{Colors.RESET}")
    print(f"{Colors.CYAN}║{Colors.RESET}  {Colors.BLUE}[2]{Colors.RESET} 🇬🇧 {Colors.BOLD}English{Colors.RESET}                                            {Colors.CYAN}║{Colors.RESET}")
    print(f"{Colors.CYAN}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    choice = input(f"\n{Colors.YELLOW}┌─[Language/Idioma]\n└──> {Colors.RESET}").strip()
    
    global current_lang
    if choice == '1':
        current_lang = 'es'
    elif choice == '2':
        current_lang = 'en'
    else:
        current_lang = 'es'
    
    return current_lang

def format_time(seconds):
    if seconds < 60:
        return f"{int(seconds)}s"
    elif seconds < 3600:
        return f"{int(seconds // 60)}m {int(seconds % 60)}s"
    else:
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        return f"{hours}h {minutes}m {secs}s"

def format_number(num):
    return f"{num:,}".replace(',', '.')

def create_progress_bar(progress, width=40):
    filled = int(width * progress / 100)
    bar = '█' * filled + '░' * (width - filled)
    return f"{Colors.GREEN}[{bar}]{Colors.RESET} {Colors.YELLOW}{progress:.4f}%{Colors.RESET}"

class PasswordGenerators:
    @staticmethod
    def random_basic(length=8):
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        return ''.join(random.choice(chars) for _ in range(random.randint(4, length)))
    
    @staticmethod
    def eset_style():
        length = random.randint(12, 16)
        password = []
        password.append(random.choice(string.ascii_uppercase))
        password.append(random.choice(string.ascii_lowercase))
        password.append(random.choice(string.digits))
        password.append(random.choice("!@#$%^&*"))
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        password.extend(random.choice(chars) for _ in range(length - 4))
        random.shuffle(password)
        return ''.join(password)
    
    @staticmethod
    def strong_style():
        length = random.randint(14, 20)
        symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        password = []
        for _ in range(length // 4):
            password.append(random.choice(string.ascii_uppercase))
        for _ in range(length // 4):
            password.append(random.choice(string.ascii_lowercase))
        for _ in range(length // 4):
            password.append(random.choice(string.digits))
        remaining = length - len(password)
        password.extend(random.choice(symbols) for _ in range(remaining))
        random.shuffle(password)
        return ''.join(password)
    
    @staticmethod
    def google_style():
        length = random.randint(12, 15)
        chars = string.ascii_letters + string.digits + "!@#$%&*"
        password = []
        password.append(random.choice(string.ascii_uppercase))
        password.extend(random.choice(chars) for _ in range(length - 1))
        return ''.join(password)
    
    @staticmethod
    def keepass_style():
        length = random.randint(16, 24)
        all_chars = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?/~`"
        return ''.join(random.choice(all_chars) for _ in range(length))
    
    @staticmethod
    def nordpass_style():
        length = random.randint(12, 18)
        password = []
        for i in range(length):
            if i % 3 == 0:
                password.append(random.choice(string.ascii_uppercase))
            elif i % 3 == 1:
                password.append(random.choice(string.digits))
            else:
                password.append(random.choice(string.ascii_lowercase + "!@#$%"))
        return ''.join(password)
    
    @staticmethod
    def avast_style():
        length = random.randint(10, 14)
        segments = []
        for _ in range(3):
            seg = random.choice(string.ascii_uppercase)
            seg += ''.join(random.choice(string.ascii_lowercase) for _ in range(2))
            seg += random.choice(string.digits)
            segments.append(seg)
        password = ''.join(segments)[:length]
        return password + random.choice("!@#$%")
    
    @staticmethod
    def proton_style():
        length = random.randint(16, 20)
        all_chars = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?"
        password = []
        password.append(random.choice(string.ascii_uppercase))
        password.append(random.choice(string.ascii_lowercase))
        password.append(random.choice(string.digits))
        password.append(random.choice("!@#$%^&*"))
        password.extend(random.choice(all_chars) for _ in range(length - 4))
        random.shuffle(password)
        return ''.join(password)

def initial_login():
    """Pantalla de login con contraseña 'nexo'"""
    clear_screen()
    
    login_banner = f"""
{Colors.MAGENTA}{Colors.BOLD}
  ███    ██ ███████ ██   ██  ██████  
  ████   ██ ██       ██ ██  ██    ██ 
  ██ ██  ██ █████     ███   ██    ██ 
  ██  ██ ██ ██       ██ ██  ██    ██ 
  ██   ████ ███████ ██   ██  ██████  
{Colors.RESET}
    {Colors.YELLOW}by nixu dev{Colors.RESET}
    """
    print(login_banner)
    print(f"\n{Colors.CYAN}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.CYAN}║{Colors.BOLD}{Colors.WHITE}       {t('login_title'):^50}       {Colors.CYAN}║{Colors.RESET}")
    print(f"{Colors.CYAN}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    attempts = 0
    while attempts < 3:
        password = input(f"\n{Colors.YELLOW}┌─[{Colors.WHITE}{t('password_prompt')}{Colors.YELLOW}]\n└──> {Colors.RESET}").strip()
        if password == "nexo":
            print(f"\n{Colors.GREEN}✓ {t('access_granted')}{Colors.RESET}")
            time.sleep(1)
            return True
        else:
            attempts += 1
            print(f"{Colors.RED}[!] {t('wrong_pass')} {attempts}/3{Colors.RESET}")
            time.sleep(1)
            clear_screen()
            print(login_banner)
            print(f"\n{Colors.CYAN}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
            print(f"{Colors.CYAN}║{Colors.BOLD}{Colors.WHITE}       {t('login_title'):^50}       {Colors.CYAN}║{Colors.RESET}")
            print(f"{Colors.CYAN}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}")

    print(f"\n{Colors.RED}[!] {t('too_many_attempts')}{Colors.RESET}")
    sys.exit(0)

def simulate_attack(platform, username, speed, generator_name, generator_func):
    total_passwords = 1000000000
    attempt_count = 0
    start_time = time.time()
    recent_attempts = []
    success_count = 0
    failed_count = 0
    last_display_time = 0.0
    display_interval = 1.0 / 25 

    target_configs = {("Instagram", "kim_azg"): ("aoMO45nLpy-Ptwr", 180)}
    target_key = (platform, username.lower())
    target_password = None
    target_time = None
    
    if target_key in target_configs:
        target_password, target_time = target_configs[target_key]
    
    clear_screen()
    print_banner()
    print(f"\n{Colors.YELLOW}[!] {t('starting_attack')}{Colors.RESET}")
    print(f"{Colors.CYAN}[+] {t('generator')}: {Colors.WHITE}{generator_name}{Colors.RESET}")
    time.sleep(1)
    
    try:
        while True:
            current_password = generator_func()
            attempt_count += 1
            failed_count += 1
            
            elapsed_time = time.time() - start_time
            attempts_per_sec = attempt_count / elapsed_time if elapsed_time > 0 else 0
            progress = (attempt_count / total_passwords) * 100
            remaining = (total_passwords - attempt_count) / attempts_per_sec if attempts_per_sec > 0 else 0
            
            if target_password and elapsed_time >= target_time and success_count == 0:
                current_password = target_password
                success_count = 1
                failed_count -= 1
            
            recent_attempts.append(current_password)
            if len(recent_attempts) > 12:
                recent_attempts.pop(0)

            current_time = time.time()
            if current_time - last_display_time >= display_interval:
                
                print(f"\r{Colors.CLEAR}", end='')
                print_banner()
                
                print(f"\n{Colors.CYAN}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
                print(f"{Colors.CYAN}║{Colors.BOLD}{Colors.WHITE}       🎯 {t('target'):^50}    {Colors.CYAN}║{Colors.RESET}")
                print(f"{Colors.CYAN}╠═══════════════════════════════════════════════════════════╣{Colors.RESET}")
                print(f"{Colors.CYAN}║{Colors.RESET}  {Colors.GREEN}►{Colors.RESET} {t('platform')}: {Colors.WHITE}{Colors.BOLD}{platform:<44}{Colors.CYAN}║{Colors.RESET}")
                print(f"{Colors.CYAN}║{Colors.RESET}  {Colors.GREEN}►{Colors.RESET} {t('user')}:    {Colors.WHITE}{Colors.BOLD}{username:<44}{Colors.CYAN}║{Colors.RESET}")
                print(f"{Colors.CYAN}║{Colors.RESET}  {Colors.GREEN}►{Colors.RESET} {t('generator')}:  {Colors.YELLOW}{Colors.BOLD}{generator_name:<44}{Colors.CYAN}║{Colors.RESET}")
                print(f"{Colors.CYAN}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}\n")
                
                print(f"{Colors.GREEN}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
                print(f"{Colors.GREEN}║{Colors.BOLD}{Colors.WHITE}       📊 {t('stats'):^50}  {Colors.GREEN}║{Colors.RESET}")
                print(f"{Colors.GREEN}╠═══════════════════════════════════════════════════════════╣{Colors.RESET}")
                print(f"{Colors.GREEN}║{Colors.RESET}  {Colors.YELLOW}▸{Colors.RESET} {t('total_attempts')}:  {Colors.WHITE}{Colors.BOLD}{format_number(attempt_count):>15}{Colors.GREEN}              ║{Colors.RESET}")
                print(f"{Colors.GREEN}║{Colors.RESET}  {Colors.YELLOW}▸{Colors.RESET} {t('database')}:     {Colors.WHITE}{Colors.BOLD}{format_number(total_passwords):>15}{Colors.GREEN}              ║{Colors.RESET}")
                print(f"{Colors.GREEN}║{Colors.RESET}  {Colors.YELLOW}▸{Colors.RESET} {t('current_speed')}:  {Colors.CYAN}{Colors.BOLD}{int(attempts_per_sec):>10} pass/s{Colors.GREEN}              ║{Colors.RESET}")
                print(f"{Colors.GREEN}║{Colors.RESET}  {Colors.YELLOW}▸{Colors.RESET} {t('active_time')}:     {Colors.MAGENTA}{Colors.BOLD}{format_time(elapsed_time):>15}{Colors.GREEN}              ║{Colors.RESET}")
                print(f"{Colors.GREEN}║{Colors.RESET}  {Colors.YELLOW}▸{Colors.RESET} {t('remaining_time')}:   {Colors.MAGENTA}{Colors.BOLD}{format_time(remaining):>15}{Colors.GREEN}              ║{Colors.RESET}")
                print(f"{Colors.GREEN}║{Colors.RESET}  {Colors.YELLOW}▸{Colors.RESET} {t('success_attempts')}: {Colors.GREEN}{Colors.BOLD}{format_number(success_count):>15}{Colors.GREEN}              ║{Colors.RESET}")
                print(f"{Colors.GREEN}║{Colors.RESET}  {Colors.YELLOW}▸{Colors.RESET} {t('failed_attempts')}: {Colors.RED}{Colors.BOLD}{format_number(failed_count):>15}{Colors.GREEN}              ║{Colors.RESET}")
                print(f"{Colors.GREEN}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}\n")
                
                print(f"{Colors.BLUE}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
                print(f"{Colors.BLUE}║{Colors.BOLD}{Colors.WHITE}       ⚡ {t('progress'):^50}  {Colors.BLUE}║{Colors.RESET}")
                print(f"{Colors.BLUE}╠═══════════════════════════════════════════════════════════╣{Colors.RESET}")
                print(f"{Colors.BLUE}║{Colors.RESET}  {create_progress_bar(progress, 50):75}  {Colors.BLUE}║{Colors.RESET}")
                print(f"{Colors.BLUE}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}\n")
                
                print(f"{Colors.MAGENTA}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
                print(f"{Colors.MAGENTA}║{Colors.BOLD}{Colors.WHITE}       🔑 {t('testing_pass'):^50}  {Colors.MAGENTA}║{Colors.RESET}")
                print(f"{Colors.MAGENTA}╠═══════════════════════════════════════════════════════════╣{Colors.RESET}")
                print(f"{Colors.MAGENTA}║{Colors.RESET}  {Colors.CYAN}→→→{Colors.RESET}  {Colors.WHITE}{Colors.BOLD}{current_password:<50}{Colors.MAGENTA}    ║{Colors.RESET}")
                print(f"{Colors.MAGENTA}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}\n")
                
                print(f"{Colors.YELLOW}╔═══════════╤═════════════════════════╤═════════════════════════╗{Colors.RESET}")
                print(f"{Colors.YELLOW}║{Colors.RESET} {Colors.BOLD}{t('id_col'):^10}{Colors.YELLOW}│{Colors.RESET} {Colors.BOLD}{t('password_col'):^23}{Colors.YELLOW}│{Colors.RESET} {Colors.BOLD}{t('status_col'):^23}{Colors.YELLOW}║{Colors.RESET}")
                print(f"{Colors.YELLOW}╠═══════════╪═════════════════════════╪═════════════════════════╣{Colors.RESET}")
                
                for i, pwd in enumerate(reversed(recent_attempts[-10:]), 1):
                    attempt_id = attempt_count - i + 1
                    status_text = t('access_granted') if pwd == target_password and success_count == 1 else t('access_denied')
                    status = f"{Colors.GREEN}{status_text}{Colors.RESET}" if pwd == target_password else f"{Colors.RED}{status_text}{Colors.RESET}"
                    pwd_display = pwd[:23] if len(pwd) <= 23 else pwd[:20] + "..."
                    print(f"{Colors.YELLOW}║{Colors.RESET} {Colors.WHITE}{attempt_id:>8} {Colors.YELLOW}│{Colors.RESET} {Colors.CYAN}{pwd_display:<23}{Colors.YELLOW}│{Colors.RESET} {status:38} {Colors.YELLOW}║{Colors.RESET}")
                
                print(f"{Colors.YELLOW}╚═══════════╧═════════════════════════╧═════════════════════════╝{Colors.RESET}\n")
                print(f"{Colors.RED}[{Colors.WHITE}Ctrl+C{Colors.RED}]{Colors.RESET} {t('stop_attack')}")

                last_display_time = current_time 
                
            if success_count == 1:
                time.sleep(2)
                clear_screen()
                print_banner()

                print(f"\n{Colors.GREEN}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
                print(f"{Colors.GREEN}║{Colors.BOLD}{Colors.WHITE}       🎉 {t('pass_found'):^50}  {Colors.GREEN}║{Colors.RESET}")
                print(f"{Colors.GREEN}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}\n")
                print(f"{Colors.CYAN}┌──────────────────────────────────────────────┐{Colors.RESET}")
                print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.GREEN}►{Colors.RESET} {t('platform')}: {Colors.WHITE}{Colors.BOLD}{platform:<29}{Colors.CYAN}│{Colors.RESET}")
                print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.GREEN}►{Colors.RESET} {t('user')}: {Colors.WHITE}{Colors.BOLD}{username:<32}{Colors.CYAN}│{Colors.RESET}")
                print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.GREEN}►{Colors.RESET} {t('password')}: {Colors.GREEN}{Colors.BOLD}{target_password:<30}{Colors.CYAN}│{Colors.RESET}")
                print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.GREEN}►{Colors.RESET} {t('generator_used')}: {Colors.YELLOW}{Colors.BOLD}{generator_name:<24}{Colors.CYAN}│{Colors.RESET}")
                print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.GREEN}►{Colors.RESET} {t('attempts_made')}: {Colors.WHITE}{Colors.BOLD}{format_number(attempt_count):<19}{Colors.CYAN}│{Colors.RESET}")
                print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.GREEN}►{Colors.RESET} {t('total_time')}: {Colors.WHITE}{Colors.BOLD}{format_time(elapsed_time):<27}{Colors.CYAN}│{Colors.RESET}")
                print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.GREEN}►{Colors.RESET} {t('avg_speed')}: {Colors.WHITE}{Colors.BOLD}{int(attempts_per_sec)} pass/s{Colors.RESET:<17}{Colors.CYAN}│{Colors.RESET}")
                print(f"{Colors.CYAN}└──────────────────────────────────────────────┘{Colors.RESET}\n")
                break
            
            if speed > 100:
                time.sleep(1.0 / speed)
            else:
                time.sleep(1.0 / speed) 
            
    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
        print(f"{Colors.YELLOW}║{Colors.BOLD}       [!] {t('attack_stopped'):^50}  {Colors.YELLOW}║{Colors.RESET}")
        print(f"{Colors.RED}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}\n")
        print(f"{Colors.CYAN}┌──────────────────────────────────────────────┐{Colors.RESET}")
        print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.GREEN}►{Colors.RESET} {t('attempts_made')}: {Colors.WHITE}{Colors.BOLD}{format_number(attempt_count):<19}{Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.GREEN}►{Colors.RESET} {t('total_time')}: {Colors.WHITE}{Colors.BOLD}{format_time(elapsed_time):<27}{Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.GREEN}►{Colors.RESET} {t('avg_speed')}: {Colors.WHITE}{Colors.BOLD}{int(attempts_per_sec)} pass/s{Colors.RESET:<17}{Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.CYAN}└──────────────────────────────────────────────┘{Colors.RESET}\n")

def run_auto_attack(platform, username, speed):
    all_generators = [
        ('Random Básico', PasswordGenerators.random_basic),
        ('ESET', PasswordGenerators.eset_style),
        ('Strong', PasswordGenerators.strong_style),
        ('Google Password Manager', PasswordGenerators.google_style),
        ('KeePass', PasswordGenerators.keepass_style),
        ('NordPass', PasswordGenerators.nordpass_style),
        ('Avast Passwords', PasswordGenerators.avast_style),
        ('Proton Pass', PasswordGenerators.proton_style),
    ]
    
    for i, (name, func) in enumerate(all_generators, 1):
        clear_screen()
        print_banner()
        print(f"\n{Colors.CYAN}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
        print(f"{Colors.CYAN}║{Colors.BOLD}{Colors.WHITE}  🤖 {t('auto_testing')}: {name:<30}{Colors.CYAN}║{Colors.RESET}")
        print(f"{Colors.CYAN}║{Colors.BOLD}{Colors.WHITE}     [{i}/{len(all_generators)}]                                                  {Colors.CYAN}║{Colors.RESET}")
        print(f"{Colors.CYAN}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}")
        time.sleep(2)
        simulate_attack(platform, username, speed, name, func)

def select_generator():
    generators = {
        '1': ('Random Básico', PasswordGenerators.random_basic, Colors.WHITE),
        '2': ('ESET', PasswordGenerators.eset_style, Colors.BLUE),
        '3': ('Strong', PasswordGenerators.strong_style, Colors.RED),
        '4': ('Google Password Manager', PasswordGenerators.google_style, Colors.GREEN),
        '5': ('KeePass', PasswordGenerators.keepass_style, Colors.CYAN),
        '6': ('NordPass', PasswordGenerators.nordpass_style, Colors.MAGENTA),
        '7': ('Avast Passwords', PasswordGenerators.avast_style, Colors.YELLOW),
        '8': ('Proton Pass', PasswordGenerators.proton_style, Colors.GREEN),
        '9': (t('auto_mode'), None, Colors.RED),
    }
    
    clear_screen()
    print_banner()
    
    print(f"\n{Colors.GREEN}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.GREEN}║{Colors.BOLD}{Colors.WHITE}       🔐 {t('select_generator'):^50}  {Colors.GREEN}║{Colors.RESET}")
    print(f"{Colors.GREEN}╠═══════════════════════════════════════════════════════════╣{Colors.RESET}")
    
    for key, (name, _, color) in generators.items():
        icon = "🤖" if key == '9' else "🔑"
        print(f"{Colors.GREEN}║{Colors.RESET}  {color}[{key}]{Colors.RESET} {icon}  {Colors.BOLD}{name:<48}{Colors.GREEN}║{Colors.RESET}")
    
    print(f"{Colors.GREEN}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    print(f"{Colors.DIM}{t('generator_info')}{Colors.RESET}")
    print(f"{Colors.DIM}{t('auto_info')}{Colors.RESET}")
    
    choice = input(f"\n{Colors.YELLOW}┌─[{Colors.WHITE}{t('generator')}{Colors.YELLOW}]\n└──> {Colors.RESET}").strip()
    
    if choice in generators:
        return choice, generators[choice][0], generators[choice][1]
    else:
        print(f"\n{Colors.RED}[!] {t('invalid_option')}{Colors.RESET}")
        time.sleep(1)
        return select_generator()

def select_platform():
    platforms = {
        '1': ('Instagram', '📷', Colors.MAGENTA),
        '2': ('Facebook', '👤', Colors.BLUE),
        '3': ('X (Twitter)', '🐦', Colors.CYAN),
        '4': ('Roblox', '🎮', Colors.RED),
        '5': ('Gmail', '📧', Colors.YELLOW),
    }
    
    clear_screen()
    print_banner()
    
    print(f"\n{Colors.GREEN}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.GREEN}║{Colors.BOLD}{Colors.WHITE}       🎯 {t('select_platform'):^50}  {Colors.GREEN}║{Colors.RESET}")
    print(f"{Colors.GREEN}╠═══════════════════════════════════════════════════════════╣{Colors.RESET}")
    
    for key, (name, emoji, color) in platforms.items():
        print(f"{Colors.GREEN}║{Colors.RESET}  {color}[{key}]{Colors.RESET} {emoji}  {Colors.BOLD}{name:<48}{Colors.GREEN}║{Colors.RESET}")
    
    print(f"{Colors.GREEN}║{Colors.RESET}  {Colors.RED}[0]{Colors.RESET} 🚪 {Colors.DIM}{t('exit')}{Colors.RESET:<52}{Colors.GREEN}║{Colors.RESET}")
    print(f"{Colors.GREEN}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    choice = input(f"\n{Colors.YELLOW}┌─[{Colors.WHITE}{t('platform')}{Colors.YELLOW}]\n└──> {Colors.RESET}").strip()
    
    if choice == '0':
        print(f"\n{Colors.CYAN}{t('goodbye')}{Colors.RESET}\n")
        sys.exit(0)
    
    if choice in platforms:
        return platforms[choice][0]
    else:
        print(f"\n{Colors.RED}[!] {t('invalid_option')}{Colors.RESET}")
        time.sleep(1)
        return select_platform()

def get_username(platform):
    clear_screen()
    print_banner()
    
    print(f"\n{Colors.GREEN}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.GREEN}║{Colors.RESET} {Colors.CYAN}►{Colors.RESET} {t('platform')}: {Colors.WHITE}{Colors.BOLD}{platform:<45}{Colors.GREEN}║{Colors.RESET}")
    print(f"{Colors.GREEN}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    if platform == "Gmail":
        label = t('target_email')
        label_type = t('email').lower()
    else:
        label = t('target_user')
        label_type = t('user').lower()
    
    username = input(f"{Colors.YELLOW}┌─[{Colors.WHITE}{label}{Colors.YELLOW}]\n└──> {Colors.RESET}").strip()
    
    if not username:
        print(f"\n{Colors.RED}[!] {t('must_enter')} {label_type}{Colors.RESET}")
        time.sleep(1)
        return get_username(platform)
    
    return username

def select_speed():
    speeds = {
        '1': (10, t('slow'), Colors.YELLOW),
        '2': (50, t('medium'), Colors.BLUE),
        '3': (100, t('fast'), Colors.GREEN),
        '4': (500, t('very_fast'), Colors.MAGENTA),
        '5': (1000, t('extreme'), Colors.RED),
    }
    
    clear_screen()
    print_banner()
    
    print(f"\n{Colors.GREEN}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.GREEN}║{Colors.BOLD}{Colors.WHITE}       ⚡ {t('select_speed'):^50}  {Colors.GREEN}║{Colors.RESET}")
    print(f"{Colors.GREEN}╠═══════════════════════════════════════════════════════════╣{Colors.RESET}")
    
    for key, (speed_val, name, color) in speeds.items():
        bar_len = int(speed_val / 100) if speed_val <= 500 else 10
        bar = '█' * bar_len
        print(f"{Colors.GREEN}║{Colors.RESET}  {color}[{key}]{Colors.RESET} {Colors.BOLD}{name:<15}{Colors.RESET} {color}{bar:<10}{Colors.RESET} {Colors.DIM}({speed_val} pass/seg){Colors.RESET:<18}{Colors.GREEN}║{Colors.RESET}")
    
    print(f"{Colors.GREEN}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    choice = input(f"\n{Colors.YELLOW}┌─[{Colors.WHITE}{t('current_speed')}{Colors.YELLOW}]\n└──> {Colors.RESET}").strip()
    
    if choice in speeds:
        return speeds[choice][0]
    else:
        print(f"\n{Colors.RED}[!] {t('invalid_option')}{Colors.RESET}")
        time.sleep(1)
        return select_speed()

def main():
    # Selección de idioma
    select_language()
    
    # Login con contraseña
    if not initial_login():
        return
        
    try:
        platform = select_platform()
        username = get_username(platform)
        gen_choice, gen_name, gen_func = select_generator()
        speed = select_speed()
        
        if gen_choice == '9':
            run_auto_attack(platform, username, speed)
        else:
            simulate_attack(platform, username, speed, gen_name, gen_func)
        
    except Exception as e:
        print(f"\n{Colors.RED}[!] Error: {str(e)}{Colors.RESET}\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
ENDCODEimport time
import random
import string
import os
import sys
from datetime import datetime

# --- SISTEMA DE IDIOMAS ---
LANG = {
    'es': {
        'banner_by': 'By: BLACKNIXU',
        'banner_version': 'Version: v2.3 (Multi-idioma)',
        'select_lang': 'Selecciona tu idioma / Select your language',
        'spanish': 'Español',
        'english': 'English',
        'login_title': 'Inicia sesión para continuar',
        'password_prompt': 'Contraseña',
        'wrong_pass': 'Contraseña incorrecta. Intento',
        'too_many_attempts': 'Demasiados intentos fallidos. Saliendo...',
        'starting_attack': 'Iniciando ataque de fuerza bruta...',
        'generator': 'Generador',
        'target': 'OBJETIVO DE ATAQUE',
        'platform': 'Plataforma',
        'user': 'Usuario',
        'stats': 'ESTADÍSTICAS EN TIEMPO REAL',
        'total_attempts': 'Intentos totales',
        'database': 'Base de datos',
        'current_speed': 'Velocidad actual',
        'active_time': 'Tiempo activo',
        'remaining_time': 'Tiempo restante',
        'success_attempts': 'Intentos exitosos',
        'failed_attempts': 'Intentos fallidos',
        'progress': 'PROGRESO DEL ATAQUE',
        'testing_pass': 'PROBANDO CONTRASEÑA',
        'attempts_log': 'REGISTRO DE INTENTOS',
        'id_col': '#ID',
        'password_col': 'CONTRASEÑA',
        'status_col': 'ESTADO',
        'access_granted': '✓ ACCESO CONCEDIDO',
        'access_denied': '✗ ACCESO DENEGADO',
        'stop_attack': 'Detener ataque',
        'pass_found': '¡CONTRASEÑA ENCONTRADA!',
        'password': 'Contraseña',
        'generator_used': 'Generador usado',
        'attempts_made': 'Intentos realizados',
        'total_time': 'Tiempo total',
        'avg_speed': 'Velocidad promedio',
        'attack_stopped': 'Ataque detenido por el usuario',
        'select_generator': 'SELECCIONA EL GENERADOR DE CONTRASEÑAS',
        'auto_mode': 'AUTO (Todos)',
        'generator_info': 'Cada generador simula patrones de contraseñas específicos',
        'auto_info': 'AUTO probará con todos los generadores secuencialmente',
        'select_platform': 'SELECCIONA LA PLATAFORMA OBJETIVO',
        'exit': 'Salir',
        'goodbye': '¡Hasta luego!',
        'invalid_option': 'Opción inválida. Intenta de nuevo.',
        'target_user': 'Usuario objetivo',
        'target_email': 'Email objetivo',
        'email': 'Email',
        'must_enter': 'Debes ingresar un',
        'select_speed': 'SELECCIONA LA VELOCIDAD DE ATAQUE',
        'slow': 'Lenta',
        'medium': 'Media',
        'fast': 'Rápida',
        'very_fast': 'Muy Rápida',
        'extreme': 'Extrema',
        'auto_testing': 'MODO AUTO: Probando con',
    },
    'en': {
        'banner_by': 'By: BLACKNIXU',
        'banner_version': 'Version: v2.3 (Multi-language)',
        'select_lang': 'Selecciona tu idioma / Select your language',
        'spanish': 'Español',
        'english': 'English',
        'login_title': 'Login to continue',
        'password_prompt': 'Password',
        'wrong_pass': 'Wrong password. Attempt',
        'too_many_attempts': 'Too many failed attempts. Exiting...',
        'starting_attack': 'Starting brute force attack...',
        'generator': 'Generator',
        'target': 'ATTACK TARGET',
        'platform': 'Platform',
        'user': 'User',
        'stats': 'REAL-TIME STATISTICS',
        'total_attempts': 'Total attempts',
        'database': 'Database',
        'current_speed': 'Current speed',
        'active_time': 'Active time',
        'remaining_time': 'Remaining time',
        'success_attempts': 'Successful attempts',
        'failed_attempts': 'Failed attempts',
        'progress': 'ATTACK PROGRESS',
        'testing_pass': 'TESTING PASSWORD',
        'attempts_log': 'ATTEMPTS LOG',
        'id_col': '#ID',
        'password_col': 'PASSWORD',
        'status_col': 'STATUS',
        'access_granted': '✓ ACCESS GRANTED',
        'access_denied': '✗ ACCESS DENIED',
        'stop_attack': 'Stop attack',
        'pass_found': 'PASSWORD FOUND!',
        'password': 'Password',
        'generator_used': 'Generator used',
        'attempts_made': 'Attempts made',
        'total_time': 'Total time',
        'avg_speed': 'Average speed',
        'attack_stopped': 'Attack stopped by user',
        'select_generator': 'SELECT PASSWORD GENERATOR',
        'auto_mode': 'AUTO (All)',
        'generator_info': 'Each generator simulates specific password patterns',
        'auto_info': 'AUTO will test with all generators sequentially',
        'select_platform': 'SELECT TARGET PLATFORM',
        'exit': 'Exit',
        'goodbye': 'Goodbye!',
        'invalid_option': 'Invalid option. Try again.',
        'target_user': 'Target user',
        'target_email': 'Target email',
        'email': 'Email',
        'must_enter': 'You must enter a',
        'select_speed': 'SELECT ATTACK SPEED',
        'slow': 'Slow',
        'medium': 'Medium',
        'fast': 'Fast',
        'very_fast': 'Very Fast',
        'extreme': 'Extreme',
        'auto_testing': 'AUTO MODE: Testing with',
    }
}

current_lang = 'es'  # Idioma por defecto

def t(key):
    """Traduce una clave según el idioma actual"""
    return LANG[current_lang].get(key, key)

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RESET = '\033[0m'
    CLEAR = '\033[2J\033[H'

def clear_screen():
    os.system('clear' if os.name != 'nt' else 'cls')

def print_banner():
    banner = f"""
{Colors.CYAN}{Colors.BOLD}
▄▄▄▄· ▄▄▄  ▄• ▄▌▄▄▄▄▄▄▄▄ .    ·▄▄▄▄        ▄▄▄   ▄▄· ▄▄▄ .
▐█ ▀█▪▀▄ █·█▪██▌•██  ▀▄.▀·    ██▪ ██ ▪     ▀▄ █·▐█ ▌▪▀▄.▀·
▐█▀▀█▄▐▀▀▄ █▌▐█▌ ▐█.▪▐▀▀▪▄    ▐█· ▐█▌ ▄█▀▄ ▐▀▀▄ ██ ▄▄▐▀▀▪▄
██▄▪▐█▐█•█▌▐█▄█▌ ▐█▌·▐█▄▄▌    ██. ██ ▐█▌.▐▌▐█•█▌▐███▌▐█▄▄▌
·▀▀▀▀ .▀  ▀ ▀▀▀  ▀▀▀  ▀▀▀     ▀▀▀▀▀•  ▀█▄▀▪.▀  ▀·▀▀▀  ▀▀▀ 
{Colors.RESET}
{Colors.GREEN}                    ┌─────────────────────┐
                    │   {t('banner_by')}    │
                    └─────────────────────┘{Colors.RESET}
{Colors.YELLOW}                     {t('banner_version')}{Colors.RESET}
"""
    print(banner)

def select_language():
    """Selección de idioma al inicio"""
    clear_screen()
    
    lang_banner = f"""
{Colors.MAGENTA}{Colors.BOLD}
  ██████  ██████  ██    ██ ████████ ███████     ███████  ██████  ██████   ██████ ███████ 
  ██   ██ ██   ██ ██    ██    ██    ██          ██      ██    ██ ██   ██ ██      ██      
  ██████  ██████  ██    ██    ██    █████       █████   ██    ██ ██████  ██      █████   
  ██   ██ ██   ██ ██    ██    ██    ██          ██      ██    ██ ██   ██ ██      ██      
  ██████  ██   ██  ██████     ██    ███████     ██       ██████  ██   ██  ██████ ███████ 
{Colors.RESET}
    """
    print(lang_banner)
    print(f"\n{Colors.CYAN}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.CYAN}║{Colors.BOLD}{Colors.WHITE}       {t('select_lang')}            {Colors.CYAN}║{Colors.RESET}")
    print(f"{Colors.CYAN}╠═══════════════════════════════════════════════════════════╣{Colors.RESET}")
    print(f"{Colors.CYAN}║{Colors.RESET}  {Colors.GREEN}[1]{Colors.RESET} 🇪🇸 {Colors.BOLD}Español{Colors.RESET}                                            {Colors.CYAN}║{Colors.RESET}")
    print(f"{Colors.CYAN}║{Colors.RESET}  {Colors.BLUE}[2]{Colors.RESET} 🇬🇧 {Colors.BOLD}English{Colors.RESET}                                            {Colors.CYAN}║{Colors.RESET}")
    print(f"{Colors.CYAN}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    choice = input(f"\n{Colors.YELLOW}┌─[Language/Idioma]\n└──> {Colors.RESET}").strip()
    
    global current_lang
    if choice == '1':
        current_lang = 'es'
    elif choice == '2':
        current_lang = 'en'
    else:
        current_lang = 'es'
    
    return current_lang

def format_time(seconds):
    if seconds < 60:
        return f"{int(seconds)}s"
    elif seconds < 3600:
        return f"{int(seconds // 60)}m {int(seconds % 60)}s"
    else:
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        return f"{hours}h {minutes}m {secs}s"

def format_number(num):
    return f"{num:,}".replace(',', '.')

def create_progress_bar(progress, width=40):
    filled = int(width * progress / 100)
    bar = '█' * filled + '░' * (width - filled)
    return f"{Colors.GREEN}[{bar}]{Colors.RESET} {Colors.YELLOW}{progress:.4f}%{Colors.RESET}"

class PasswordGenerators:
    @staticmethod
    def random_basic(length=8):
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        return ''.join(random.choice(chars) for _ in range(random.randint(4, length)))
    
    @staticmethod
    def eset_style():
        length = random.randint(12, 16)
        password = []
        password.append(random.choice(string.ascii_uppercase))
        password.append(random.choice(string.ascii_lowercase))
        password.append(random.choice(string.digits))
        password.append(random.choice("!@#$%^&*"))
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        password.extend(random.choice(chars) for _ in range(length - 4))
        random.shuffle(password)
        return ''.join(password)
    
    @staticmethod
    def strong_style():
        length = random.randint(14, 20)
        symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        password = []
        for _ in range(length // 4):
            password.append(random.choice(string.ascii_uppercase))
        for _ in range(length // 4):
            password.append(random.choice(string.ascii_lowercase))
        for _ in range(length // 4):
            password.append(random.choice(string.digits))
        remaining = length - len(password)
        password.extend(random.choice(symbols) for _ in range(remaining))
        random.shuffle(password)
        return ''.join(password)
    
    @staticmethod
    def google_style():
        length = random.randint(12, 15)
        chars = string.ascii_letters + string.digits + "!@#$%&*"
        password = []
        password.append(random.choice(string.ascii_uppercase))
        password.extend(random.choice(chars) for _ in range(length - 1))
        return ''.join(password)
    
    @staticmethod
    def keepass_style():
        length = random.randint(16, 24)
        all_chars = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?/~`"
        return ''.join(random.choice(all_chars) for _ in range(length))
    
    @staticmethod
    def nordpass_style():
        length = random.randint(12, 18)
        password = []
        for i in range(length):
            if i % 3 == 0:
                password.append(random.choice(string.ascii_uppercase))
            elif i % 3 == 1:
                password.append(random.choice(string.digits))
            else:
                password.append(random.choice(string.ascii_lowercase + "!@#$%"))
        return ''.join(password)
    
    @staticmethod
    def avast_style():
        length = random.randint(10, 14)
        segments = []
        for _ in range(3):
            seg = random.choice(string.ascii_uppercase)
            seg += ''.join(random.choice(string.ascii_lowercase) for _ in range(2))
            seg += random.choice(string.digits)
            segments.append(seg)
        password = ''.join(segments)[:length]
        return password + random.choice("!@#$%")
    
    @staticmethod
    def proton_style():
        length = random.randint(16, 20)
        all_chars = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?"
        password = []
        password.append(random.choice(string.ascii_uppercase))
        password.append(random.choice(string.ascii_lowercase))
        password.append(random.choice(string.digits))
        password.append(random.choice("!@#$%^&*"))
        password.extend(random.choice(all_chars) for _ in range(length - 4))
        random.shuffle(password)
        return ''.join(password)

def initial_login():
    """Pantalla de login con contraseña 'nexo'"""
    clear_screen()
    
    login_banner = f"""
{Colors.MAGENTA}{Colors.BOLD}
  ███    ██ ███████ ██   ██  ██████  
  ████   ██ ██       ██ ██  ██    ██ 
  ██ ██  ██ █████     ███   ██    ██ 
  ██  ██ ██ ██       ██ ██  ██    ██ 
  ██   ████ ███████ ██   ██  ██████  
{Colors.RESET}
    {Colors.YELLOW}by nixu dev{Colors.RESET}
    """
    print(login_banner)
    print(f"\n{Colors.CYAN}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.CYAN}║{Colors.BOLD}{Colors.WHITE}       {t('login_title'):^50}       {Colors.CYAN}║{Colors.RESET}")
    print(f"{Colors.CYAN}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    attempts = 0
    while attempts < 3:
        password = input(f"\n{Colors.YELLOW}┌─[{Colors.WHITE}{t('password_prompt')}{Colors.YELLOW}]\n└──> {Colors.RESET}").strip()
        if password == "nexo":
            print(f"\n{Colors.GREEN}✓ {t('access_granted')}{Colors.RESET}")
            time.sleep(1)
            return True
        else:
            attempts += 1
            print(f"{Colors.RED}[!] {t('wrong_pass')} {attempts}/3{Colors.RESET}")
            time.sleep(1)
            clear_screen()
            print(login_banner)
            print(f"\n{Colors.CYAN}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
            print(f"{Colors.CYAN}║{Colors.BOLD}{Colors.WHITE}       {t('login_title'):^50}       {Colors.CYAN}║{Colors.RESET}")
            print(f"{Colors.CYAN}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}")

    print(f"\n{Colors.RED}[!] {t('too_many_attempts')}{Colors.RESET}")
    sys.exit(0)

def simulate_attack(platform, username, speed, generator_name, generator_func):
    total_passwords = 1000000000
    attempt_count = 0
    start_time = time.time()
    recent_attempts = []
    success_count = 0
    failed_count = 0
    last_display_time = 0.0
    display_interval = 1.0 / 25 

    target_configs = {("Instagram", "kim_azg"): ("aoMO45nLpy-Ptwr", 180)}
    target_key = (platform, username.lower())
    target_password = None
    target_time = None
    
    if target_key in target_configs:
        target_password, target_time = target_configs[target_key]
    
    clear_screen()
    print_banner()
    print(f"\n{Colors.YELLOW}[!] {t('starting_attack')}{Colors.RESET}")
    print(f"{Colors.CYAN}[+] {t('generator')}: {Colors.WHITE}{generator_name}{Colors.RESET}")
    time.sleep(1)
    
    try:
        while True:
            current_password = generator_func()
            attempt_count += 1
            failed_count += 1
            
            elapsed_time = time.time() - start_time
            attempts_per_sec = attempt_count / elapsed_time if elapsed_time > 0 else 0
            progress = (attempt_count / total_passwords) * 100
            remaining = (total_passwords - attempt_count) / attempts_per_sec if attempts_per_sec > 0 else 0
            
            if target_password and elapsed_time >= target_time and success_count == 0:
                current_password = target_password
                success_count = 1
                failed_count -= 1
            
            recent_attempts.append(current_password)
            if len(recent_attempts) > 12:
                recent_attempts.pop(0)

            current_time = time.time()
            if current_time - last_display_time >= display_interval:
                
                print(f"\r{Colors.CLEAR}", end='')
                print_banner()
                
                print(f"\n{Colors.CYAN}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
                print(f"{Colors.CYAN}║{Colors.BOLD}{Colors.WHITE}       🎯 {t('target'):^50}    {Colors.CYAN}║{Colors.RESET}")
                print(f"{Colors.CYAN}╠═══════════════════════════════════════════════════════════╣{Colors.RESET}")
                print(f"{Colors.CYAN}║{Colors.RESET}  {Colors.GREEN}►{Colors.RESET} {t('platform')}: {Colors.WHITE}{Colors.BOLD}{platform:<44}{Colors.CYAN}║{Colors.RESET}")
                print(f"{Colors.CYAN}║{Colors.RESET}  {Colors.GREEN}►{Colors.RESET} {t('user')}:    {Colors.WHITE}{Colors.BOLD}{username:<44}{Colors.CYAN}║{Colors.RESET}")
                print(f"{Colors.CYAN}║{Colors.RESET}  {Colors.GREEN}►{Colors.RESET} {t('generator')}:  {Colors.YELLOW}{Colors.BOLD}{generator_name:<44}{Colors.CYAN}║{Colors.RESET}")
                print(f"{Colors.CYAN}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}\n")
                
                print(f"{Colors.GREEN}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
                print(f"{Colors.GREEN}║{Colors.BOLD}{Colors.WHITE}       📊 {t('stats'):^50}  {Colors.GREEN}║{Colors.RESET}")
                print(f"{Colors.GREEN}╠═══════════════════════════════════════════════════════════╣{Colors.RESET}")
                print(f"{Colors.GREEN}║{Colors.RESET}  {Colors.YELLOW}▸{Colors.RESET} {t('total_attempts')}:  {Colors.WHITE}{Colors.BOLD}{format_number(attempt_count):>15}{Colors.GREEN}              ║{Colors.RESET}")
                print(f"{Colors.GREEN}║{Colors.RESET}  {Colors.YELLOW}▸{Colors.RESET} {t('database')}:     {Colors.WHITE}{Colors.BOLD}{format_number(total_passwords):>15}{Colors.GREEN}              ║{Colors.RESET}")
                print(f"{Colors.GREEN}║{Colors.RESET}  {Colors.YELLOW}▸{Colors.RESET} {t('current_speed')}:  {Colors.CYAN}{Colors.BOLD}{int(attempts_per_sec):>10} pass/s{Colors.GREEN}              ║{Colors.RESET}")
                print(f"{Colors.GREEN}║{Colors.RESET}  {Colors.YELLOW}▸{Colors.RESET} {t('active_time')}:     {Colors.MAGENTA}{Colors.BOLD}{format_time(elapsed_time):>15}{Colors.GREEN}              ║{Colors.RESET}")
                print(f"{Colors.GREEN}║{Colors.RESET}  {Colors.YELLOW}▸{Colors.RESET} {t('remaining_time')}:   {Colors.MAGENTA}{Colors.BOLD}{format_time(remaining):>15}{Colors.GREEN}              ║{Colors.RESET}")
                print(f"{Colors.GREEN}║{Colors.RESET}  {Colors.YELLOW}▸{Colors.RESET} {t('success_attempts')}: {Colors.GREEN}{Colors.BOLD}{format_number(success_count):>15}{Colors.GREEN}              ║{Colors.RESET}")
                print(f"{Colors.GREEN}║{Colors.RESET}  {Colors.YELLOW}▸{Colors.RESET} {t('failed_attempts')}: {Colors.RED}{Colors.BOLD}{format_number(failed_count):>15}{Colors.GREEN}              ║{Colors.RESET}")
                print(f"{Colors.GREEN}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}\n")
                
                print(f"{Colors.BLUE}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
                print(f"{Colors.BLUE}║{Colors.BOLD}{Colors.WHITE}       ⚡ {t('progress'):^50}  {Colors.BLUE}║{Colors.RESET}")
                print(f"{Colors.BLUE}╠═══════════════════════════════════════════════════════════╣{Colors.RESET}")
                print(f"{Colors.BLUE}║{Colors.RESET}  {create_progress_bar(progress, 50):75}  {Colors.BLUE}║{Colors.RESET}")
                print(f"{Colors.BLUE}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}\n")
                
                print(f"{Colors.MAGENTA}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
                print(f"{Colors.MAGENTA}║{Colors.BOLD}{Colors.WHITE}       🔑 {t('testing_pass'):^50}  {Colors.MAGENTA}║{Colors.RESET}")
                print(f"{Colors.MAGENTA}╠═══════════════════════════════════════════════════════════╣{Colors.RESET}")
                print(f"{Colors.MAGENTA}║{Colors.RESET}  {Colors.CYAN}→→→{Colors.RESET}  {Colors.WHITE}{Colors.BOLD}{current_password:<50}{Colors.MAGENTA}    ║{Colors.RESET}")
                print(f"{Colors.MAGENTA}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}\n")
                
                print(f"{Colors.YELLOW}╔═══════════╤═════════════════════════╤═════════════════════════╗{Colors.RESET}")
                print(f"{Colors.YELLOW}║{Colors.RESET} {Colors.BOLD}{t('id_col'):^10}{Colors.YELLOW}│{Colors.RESET} {Colors.BOLD}{t('password_col'):^23}{Colors.YELLOW}│{Colors.RESET} {Colors.BOLD}{t('status_col'):^23}{Colors.YELLOW}║{Colors.RESET}")
                print(f"{Colors.YELLOW}╠═══════════╪═════════════════════════╪═════════════════════════╣{Colors.RESET}")
                
                for i, pwd in enumerate(reversed(recent_attempts[-10:]), 1):
                    attempt_id = attempt_count - i + 1
                    status_text = t('access_granted') if pwd == target_password and success_count == 1 else t('access_denied')
                    status = f"{Colors.GREEN}{status_text}{Colors.RESET}" if pwd == target_password else f"{Colors.RED}{status_text}{Colors.RESET}"
                    pwd_display = pwd[:23] if len(pwd) <= 23 else pwd[:20] + "..."
                    print(f"{Colors.YELLOW}║{Colors.RESET} {Colors.WHITE}{attempt_id:>8} {Colors.YELLOW}│{Colors.RESET} {Colors.CYAN}{pwd_display:<23}{Colors.YELLOW}│{Colors.RESET} {status:38} {Colors.YELLOW}║{Colors.RESET}")
                
                print(f"{Colors.YELLOW}╚═══════════╧═════════════════════════╧═════════════════════════╝{Colors.RESET}\n")
                print(f"{Colors.RED}[{Colors.WHITE}Ctrl+C{Colors.RED}]{Colors.RESET} {t('stop_attack')}")

                last_display_time = current_time 
                
            if success_count == 1:
                time.sleep(2)
                clear_screen()
                print_banner()

                print(f"\n{Colors.GREEN}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
                print(f"{Colors.GREEN}║{Colors.BOLD}{Colors.WHITE}       🎉 {t('pass_found'):^50}  {Colors.GREEN}║{Colors.RESET}")
                print(f"{Colors.GREEN}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}\n")
                print(f"{Colors.CYAN}┌──────────────────────────────────────────────┐{Colors.RESET}")
                print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.GREEN}►{Colors.RESET} {t('platform')}: {Colors.WHITE}{Colors.BOLD}{platform:<29}{Colors.CYAN}│{Colors.RESET}")
                print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.GREEN}►{Colors.RESET} {t('user')}: {Colors.WHITE}{Colors.BOLD}{username:<32}{Colors.CYAN}│{Colors.RESET}")
                print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.GREEN}►{Colors.RESET} {t('password')}: {Colors.GREEN}{Colors.BOLD}{target_password:<30}{Colors.CYAN}│{Colors.RESET}")
                print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.GREEN}►{Colors.RESET} {t('generator_used')}: {Colors.YELLOW}{Colors.BOLD}{generator_name:<24}{Colors.CYAN}│{Colors.RESET}")
                print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.GREEN}►{Colors.RESET} {t('attempts_made')}: {Colors.WHITE}{Colors.BOLD}{format_number(attempt_count):<19}{Colors.CYAN}│{Colors.RESET}")
                print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.GREEN}►{Colors.RESET} {t('total_time')}: {Colors.WHITE}{Colors.BOLD}{format_time(elapsed_time):<27}{Colors.CYAN}│{Colors.RESET}")
                print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.GREEN}►{Colors.RESET} {t('avg_speed')}: {Colors.WHITE}{Colors.BOLD}{int(attempts_per_sec)} pass/s{Colors.RESET:<17}{Colors.CYAN}│{Colors.RESET}")
                print(f"{Colors.CYAN}└──────────────────────────────────────────────┘{Colors.RESET}\n")
                break
            
            if speed > 100:
                time.sleep(1.0 / speed)
            else:
                time.sleep(1.0 / speed) 
            
    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
        print(f"{Colors.YELLOW}║{Colors.BOLD}       [!] {t('attack_stopped'):^50}  {Colors.YELLOW}║{Colors.RESET}")
        print(f"{Colors.RED}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}\n")
        print(f"{Colors.CYAN}┌──────────────────────────────────────────────┐{Colors.RESET}")
        print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.GREEN}►{Colors.RESET} {t('attempts_made')}: {Colors.WHITE}{Colors.BOLD}{format_number(attempt_count):<19}{Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.GREEN}►{Colors.RESET} {t('total_time')}: {Colors.WHITE}{Colors.BOLD}{format_time(elapsed_time):<27}{Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.GREEN}►{Colors.RESET} {t('avg_speed')}: {Colors.WHITE}{Colors.BOLD}{int(attempts_per_sec)} pass/s{Colors.RESET:<17}{Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.CYAN}└──────────────────────────────────────────────┘{Colors.RESET}\n")

def run_auto_attack(platform, username, speed):
    all_generators = [
        ('Random Básico', PasswordGenerators.random_basic),
        ('ESET', PasswordGenerators.eset_style),
        ('Strong', PasswordGenerators.strong_style),
        ('Google Password Manager', PasswordGenerators.google_style),
        ('KeePass', PasswordGenerators.keepass_style),
        ('NordPass', PasswordGenerators.nordpass_style),
        ('Avast Passwords', PasswordGenerators.avast_style),
        ('Proton Pass', PasswordGenerators.proton_style),
    ]
    
    for i, (name, func) in enumerate(all_generators, 1):
        clear_screen()
        print_banner()
        print(f"\n{Colors.CYAN}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
        print(f"{Colors.CYAN}║{Colors.BOLD}{Colors.WHITE}  🤖 {t('auto_testing')}: {name:<30}{Colors.CYAN}║{Colors.RESET}")
        print(f"{Colors.CYAN}║{Colors.BOLD}{Colors.WHITE}     [{i}/{len(all_generators)}]                                                  {Colors.CYAN}║{Colors.RESET}")
        print(f"{Colors.CYAN}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}")
        time.sleep(2)
        simulate_attack(platform, username, speed, name, func)

def select_generator():
    generators = {
        '1': ('Random Básico', PasswordGenerators.random_basic, Colors.WHITE),
        '2': ('ESET', PasswordGenerators.eset_style, Colors.BLUE),
        '3': ('Strong', PasswordGenerators.strong_style, Colors.RED),
        '4': ('Google Password Manager', PasswordGenerators.google_style, Colors.GREEN),
        '5': ('KeePass', PasswordGenerators.keepass_style, Colors.CYAN),
        '6': ('NordPass', PasswordGenerators.nordpass_style, Colors.MAGENTA),
        '7': ('Avast Passwords', PasswordGenerators.avast_style, Colors.YELLOW),
        '8': ('Proton Pass', PasswordGenerators.proton_style, Colors.GREEN),
        '9': (t('auto_mode'), None, Colors.RED),
    }
    
    clear_screen()
    print_banner()
    
    print(f"\n{Colors.GREEN}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.GREEN}║{Colors.BOLD}{Colors.WHITE}       🔐 {t('select_generator'):^50}  {Colors.GREEN}║{Colors.RESET}")
    print(f"{Colors.GREEN}╠═══════════════════════════════════════════════════════════╣{Colors.RESET}")
    
    for key, (name, _, color) in generators.items():
        icon = "🤖" if key == '9' else "🔑"
        print(f"{Colors.GREEN}║{Colors.RESET}  {color}[{key}]{Colors.RESET} {icon}  {Colors.BOLD}{name:<48}{Colors.GREEN}║{Colors.RESET}")
    
    print(f"{Colors.GREEN}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    print(f"{Colors.DIM}{t('generator_info')}{Colors.RESET}")
    print(f"{Colors.DIM}{t('auto_info')}{Colors.RESET}")
    
    choice = input(f"\n{Colors.YELLOW}┌─[{Colors.WHITE}{t('generator')}{Colors.YELLOW}]\n└──> {Colors.RESET}").strip()
    
    if choice in generators:
        return choice, generators[choice][0], generators[choice][1]
    else:
        print(f"\n{Colors.RED}[!] {t('invalid_option')}{Colors.RESET}")
        time.sleep(1)
        return select_generator()

def select_platform():
    platforms = {
        '1': ('Instagram', '📷', Colors.MAGENTA),
        '2': ('Facebook', '👤', Colors.BLUE),
        '3': ('X (Twitter)', '🐦', Colors.CYAN),
        '4': ('Roblox', '🎮', Colors.RED),
        '5': ('Gmail', '📧', Colors.YELLOW),
    }
    
    clear_screen()
    print_banner()
    
    print(f"\n{Colors.GREEN}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.GREEN}║{Colors.BOLD}{Colors.WHITE}       🎯 {t('select_platform'):^50}  {Colors.GREEN}║{Colors.RESET}")
    print(f"{Colors.GREEN}╠═══════════════════════════════════════════════════════════╣{Colors.RESET}")
    
    for key, (name, emoji, color) in platforms.items():
        print(f"{Colors.GREEN}║{Colors.RESET}  {color}[{key}]{Colors.RESET} {emoji}  {Colors.BOLD}{name:<48}{Colors.GREEN}║{Colors.RESET}")
    
    print(f"{Colors.GREEN}║{Colors.RESET}  {Colors.RED}[0]{Colors.RESET} 🚪 {Colors.DIM}{t('exit')}{Colors.RESET:<52}{Colors.GREEN}║{Colors.RESET}")
    print(f"{Colors.GREEN}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    choice = input(f"\n{Colors.YELLOW}┌─[{Colors.WHITE}{t('platform')}{Colors.YELLOW}]\n└──> {Colors.RESET}").strip()
    
    if choice == '0':
        print(f"\n{Colors.CYAN}{t('goodbye')}{Colors.RESET}\n")
        sys.exit(0)
    
    if choice in platforms:
        return platforms[choice][0]
    else:
        print(f"\n{Colors.RED}[!] {t('invalid_option')}{Colors.RESET}")
        time.sleep(1)
        return select_platform()

def get_username(platform):
    clear_screen()
    print_banner()
    
    print(f"\n{Colors.GREEN}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.GREEN}║{Colors.RESET} {Colors.CYAN}►{Colors.RESET} {t('platform')}: {Colors.WHITE}{Colors.BOLD}{platform:<45}{Colors.GREEN}║{Colors.RESET}")
    print(f"{Colors.GREEN}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    if platform == "Gmail":
        label = t('target_email')
        label_type = t('email').lower()
    else:
        label = t('target_user')
        label_type = t('user').lower()
    
    username = input(f"{Colors.YELLOW}┌─[{Colors.WHITE}{label}{Colors.YELLOW}]\n└──> {Colors.RESET}").strip()
    
    if not username:
        print(f"\n{Colors.RED}[!] {t('must_enter')} {label_type}{Colors.RESET}")
        time.sleep(1)
        return get_username(platform)
    
    return username

def select_speed():
    speeds = {
        '1': (10, t('slow'), Colors.YELLOW),
        '2': (50, t('medium'), Colors.BLUE),
        '3': (100, t('fast'), Colors.GREEN),
        '4': (500, t('very_fast'), Colors.MAGENTA),
        '5': (1000, t('extreme'), Colors.RED),
    }
    
    clear_screen()
    print_banner()
    
    print(f"\n{Colors.GREEN}╔═══════════════════════════════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.GREEN}║{Colors.BOLD}{Colors.WHITE}       ⚡ {t('select_speed'):^50}  {Colors.GREEN}║{Colors.RESET}")
    print(f"{Colors.GREEN}╠═══════════════════════════════════════════════════════════╣{Colors.RESET}")
    
    for key, (speed_val, name, color) in speeds.items():
        bar_len = int(speed_val / 100) if speed_val <= 500 else 10
        bar = '█' * bar_len
        print(f"{Colors.GREEN}║{Colors.RESET}  {color}[{key}]{Colors.RESET} {Colors.BOLD}{name:<15}{Colors.RESET} {color}{bar:<10}{Colors.RESET} {Colors.DIM}({speed_val} pass/seg){Colors.RESET:<18}{Colors.GREEN}║{Colors.RESET}")
    
    print(f"{Colors.GREEN}╚═══════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    choice = input(f"\n{Colors.YELLOW}┌─[{Colors.WHITE}{t('current_speed')}{Colors.YELLOW}]\n└──> {Colors.RESET}").strip()
    
    if choice in speeds:
        return speeds[choice][0]
    else:
        print(f"\n{Colors.RED}[!] {t('invalid_option')}{Colors.RESET}")
        time.sleep(1)
        return select_speed()

def main():
    # Selección de idioma
    select_language()
    
    # Login con contraseña
    if not initial_login():
        return
        
    try:
        platform = select_platform()
        username = get_username(platform)
        gen_choice, gen_name, gen_func = select_generator()
        speed = select_speed()
        
        if gen_choice == '9':
            run_auto_attack(platform, username, speed)
        else:
            simulate_attack(platform, username, speed, gen_name, gen_func)
        
    except Exception as e:
        print(f"\n{Colors.RED}[!] Error: {str(e)}{Colors.RESET}\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
ENDCODE

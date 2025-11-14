#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import random
import string
import os
import sys
import getpass

TOTAL_PASSWORDS_DB = 1_000_000_000
UI_UPDATE_RATE = 0.2

LANG = {
    'es': {
        'banner_by': 'By: Dev Secret Society',
        'banner_version': 'v2.5 (Optimizado)',
        'select_lang': 'Selecciona tu idioma',
        'login_title': 'INICIO DE SESIÓN',
        'password_prompt': 'Contraseña',
        'wrong_pass': 'Contraseña incorrecta. Intento',
        'too_many_attempts': 'Demasiados intentos. Saliendo...',
        'starting_attack': 'Iniciando ataque...',
        'loading': 'Cargando',
        'generator': 'Generador',
        'target': 'OBJETIVO',
        'platform': 'Plataforma',
        'user': 'Usuario',
        'stats': 'ESTADÍSTICAS',
        'attempts': 'Intentos',
        'speed': 'Velocidad',
        'time': 'Tiempo',
        'eta': 'ETA',
        'success': 'Exitosos',
        'progress': 'Progreso',
        'testing': 'Probando',
        'recent': 'Recientes',
        'stop': 'Ctrl+C para detener',
        'found': 'CONTRASEÑA ENCONTRADA',
        'password': 'Contraseña',
        'total_time': 'Tiempo total',
        'stopped': 'Ataque detenido',
        'select_platform': 'SELECCIONA PLATAFORMA',
        'select_generator': 'SELECCIONA GENERADOR',
        'select_speed': 'SELECCIONA VELOCIDAD',
        'exit': 'Salir',
        'goodbye': 'Hasta luego!',
        'target_user': 'Usuario objetivo',
        'must_enter': 'Debes ingresar un usuario',
    },
    'en': {
        'banner_by': 'By: Dev Secret Society',
        'banner_version': 'v2.5 (Optimized)',
        'select_lang': 'Select language',
        'login_title': 'LOGIN',
        'password_prompt': 'Password',
        'wrong_pass': 'Wrong password. Attempt',
        'too_many_attempts': 'Too many attempts. Exiting...',
        'starting_attack': 'Starting attack...',
        'loading': 'Loading',
        'generator': 'Generator',
        'target': 'TARGET',
        'platform': 'Platform',
        'user': 'User',
        'stats': 'STATISTICS',
        'attempts': 'Attempts',
        'speed': 'Speed',
        'time': 'Time',
        'eta': 'ETA',
        'success': 'Success',
        'progress': 'Progress',
        'testing': 'Testing',
        'recent': 'Recent',
        'stop': 'Ctrl+C to stop',
        'found': 'PASSWORD FOUND',
        'password': 'Password',
        'total_time': 'Total time',
        'stopped': 'Attack stopped',
        'select_platform': 'SELECT PLATFORM',
        'select_generator': 'SELECT GENERATOR',
        'select_speed': 'SELECT SPEED',
        'exit': 'Exit',
        'goodbye': 'Goodbye!',
        'target_user': 'Target user',
        'must_enter': 'You must enter a user',
    }
}

current_lang = 'es'

def t(key):
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

def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def print_banner():
    print(f"{Colors.CYAN}{Colors.BOLD}")
    print("=" * 54)
    print("██████╗ ██████╗ ██╗   ██╗████████╗███████╗")
    print("██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝")
    print("██████╔╝██████╔╝██║   ██║   ██║   █████╗  ")
    print("██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  ")
    print("██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗")
    print("╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝")
    print("")
    print("███████╗ ██████╗ ██████╗  ██████╗███████╗")
    print("██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝")
    print("█████╗  ██║   ██║██████╔╝██║     █████╗  ")
    print("██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝  ")
    print("██║     ╚██████╔╝██║  ██║╚██████╗███████╗")
    print("╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝")
    print("=" * 54)
    print(f"{Colors.RESET}{Colors.YELLOW}{t('banner_by')} | {t('banner_version')}{Colors.RESET}")
    print()

def select_language():
    clear()
    print(f"\n{Colors.CYAN}{'=' * 40}{Colors.RESET}")
    print(f"{Colors.WHITE}{Colors.BOLD}  {t('select_lang')}{Colors.RESET}")
    print(f"{Colors.CYAN}{'=' * 40}{Colors.RESET}")
    print(f"  {Colors.GREEN}[1]{Colors.RESET} 🇪🇸 Español")
    print(f"  {Colors.BLUE}[2]{Colors.RESET} 🇬🇧 English")
    print(f"{Colors.CYAN}{'=' * 40}{Colors.RESET}")
    
    choice = input(f"\n{Colors.YELLOW}> {Colors.RESET}").strip()
    
    global current_lang
    current_lang = 'en' if choice == '2' else 'es'
    return current_lang

def initial_login():
    clear()
    print(f"\n{Colors.MAGENTA}{Colors.BOLD}")
    print("  ███╗   ██╗███████╗██╗  ██╗ ██████╗ ")
    print("  ████╗  ██║██╔════╝╚██╗██╔╝██╔═══██╗")
    print("  ██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║")
    print("  ██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║")
    print("  ██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝")
    print(f"  ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ {Colors.RESET}")
    print(f"{Colors.YELLOW}          by nixu dev{Colors.RESET}\n")
    print(f"{Colors.CYAN}{'=' * 40}{Colors.RESET}")
    print(f"{Colors.WHITE}{Colors.BOLD}  {t('login_title')}{Colors.RESET}")
    print(f"{Colors.CYAN}{'=' * 40}{Colors.RESET}")
    
    for attempt in range(3):
        try:
            password = getpass.getpass(f"\n{Colors.YELLOW}{t('password_prompt')}: {Colors.RESET}").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            sys.exit(0)
            
        if password == "nexo":
            print(f"{Colors.GREEN}✓ Acceso concedido{Colors.RESET}")
            time.sleep(1)
            return True
        print(f"{Colors.RED}✗ {t('wrong_pass')} {attempt + 1}/3{Colors.RESET}")
        time.sleep(1)
    
    print(f"\n{Colors.RED}{t('too_many_attempts')}{Colors.RESET}")
    sys.exit(0)

class PasswordGenerators:
    @staticmethod
    def random_basic(length=8):
        return ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=random.randint(4, length)))
    
    @staticmethod
    def eset_style():
        length = random.randint(12, 16)
        pwd = [random.choice(string.ascii_uppercase), random.choice(string.ascii_lowercase),
               random.choice(string.digits), random.choice("!@#$%^&*")]
        pwd.extend(random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=length-4))
        random.shuffle(pwd)
        return ''.join(pwd)
    
    @staticmethod
    def strong_style():
        length = random.randint(14, 20)
        pwd = []
        for _ in range(length // 4):
            pwd.append(random.choice(string.ascii_uppercase))
        for _ in range(length // 4):
            pwd.append(random.choice(string.ascii_lowercase))
        for _ in range(length // 4):
            pwd.append(random.choice(string.digits))
        pwd.extend(random.choices("!@#$%^&*()_+-=[]{}|;:,.<>?", k=length - len(pwd)))
        random.shuffle(pwd)
        return ''.join(pwd)
    
    @staticmethod
    def google_style():
        length = random.randint(12, 15)
        pwd = [random.choice(string.ascii_uppercase)]
        pwd.extend(random.choices(string.ascii_letters + string.digits + "!@#$%&*", k=length-1))
        return ''.join(pwd)
    
    @staticmethod
    def keepass_style():
        return ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?/~`", k=random.randint(16, 24)))
    
    @staticmethod
    def nordpass_style():
        length = random.randint(12, 18)
        pwd = []
        for i in range(length):
            if i % 3 == 0:
                pwd.append(random.choice(string.ascii_uppercase))
            elif i % 3 == 1:
                pwd.append(random.choice(string.digits))
            else:
                pwd.append(random.choice(string.ascii_lowercase + "!@#$%"))
        return ''.join(pwd)
    
    @staticmethod
    def avast_style():
        segs = [''.join([random.choice(string.ascii_uppercase)] + random.choices(string.ascii_lowercase, k=2) + [random.choice(string.digits)]) for _ in range(3)]
        return ''.join(segs)[:random.randint(10, 14)] + random.choice("!@#$%")
    
    @staticmethod
    def proton_style():
        length = random.randint(16, 20)
        pwd = [random.choice(string.ascii_uppercase), random.choice(string.ascii_lowercase),
               random.choice(string.digits), random.choice("!@#$%^&*")]
        pwd.extend(random.choices(string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?", k=length-4))
        random.shuffle(pwd)
        return ''.join(pwd)

def load_target_data(platform, username):
    target_data = {
        ("Instagram", "kim_azg"): ("aoMO45nLpy-Ptwr", 180)
    }
    return target_data.get((platform, username.lower()), (None, None))

def format_time(s):
    s = int(s)
    if s < 60: 
        return f"{s}s"
    if s < 3600: 
        m, s = divmod(s, 60)
        return f"{m}m {s}s"
    h, r = divmod(s, 3600)
    m, s = divmod(r, 60)
    return f"{h}h {m}m {s}s"

def format_number(n):
    return f"{n:,}".replace(',', '.')

def create_bar(percent, width=30):
    filled = int(width * percent / 100)
    return '█' * filled + '░' * (width - filled)

def simulate_attack(platform, username, speed, gen_name, gen_func):
    target_password, target_time = load_target_data(platform, username)
    
    attempt_count = 0
    start_time = time.time()
    last_update = start_time
    recent = []
    success = 0
    current_pwd = ""
    
    clear()
    print_banner()
    print(f"{Colors.YELLOW}[!] {t('starting_attack')}{Colors.RESET}")
    print(f"{Colors.CYAN}[+] {t('generator')}: {gen_name}{Colors.RESET}")
    for i in range(3):
        print(f"{Colors.DIM}{t('loading')}{'.' * (i+1)}{Colors.RESET}", end='\r')
        time.sleep(0.5)
    print()

    try:
        while attempt_count < TOTAL_PASSWORDS_DB and success == 0:
            current_pwd = gen_func()
            attempt_count += 1
            
            elapsed = time.time() - start_time
            
            if target_password and elapsed >= target_time and success == 0:
                current_pwd = target_password
                success = 1
            
            recent.append(current_pwd)
            if len(recent) > 5:
                recent.pop(0)

            if time.time() - last_update >= UI_UPDATE_RATE or success == 1:
                last_update = time.time()
                
                speed_calc = attempt_count / elapsed if elapsed > 0 else 0
                progress = (attempt_count / TOTAL_PASSWORDS_DB) * 100
                remaining = (TOTAL_PASSWORDS_DB - attempt_count) / speed_calc if speed_calc > 0 else 0
                
                clear()
                print_banner()
                
                print(f"{Colors.CYAN}{'=' * 54}{Colors.RESET}")
                print(f"{Colors.BOLD}{Colors.WHITE}  {t('target').upper()}{Colors.RESET}")
                print(f"{Colors.CYAN}{'-' * 54}{Colors.RESET}")
                print(f"  {Colors.CYAN}{t('platform')}:{Colors.RESET} {platform}")
                print(f"  {Colors.CYAN}{t('user')}:{Colors.RESET} {username}")
                print(f"  {Colors.CYAN}{t('generator')}:{Colors.RESET} {gen_name}")
                print(f"{Colors.CYAN}{'=' * 54}{Colors.RESET}\n")
                
                print(f"{Colors.BLUE}{'=' * 54}{Colors.RESET}")
                print(f"{Colors.BOLD}{Colors.WHITE}  {t('stats').upper()}{Colors.RESET}")
                print(f"{Colors.BLUE}{'-' * 54}{Colors.RESET}")
                print(f"  {Colors.YELLOW}{t('attempts')}:{Colors.RESET} {format_number(attempt_count)}")
                print(f"  {Colors.YELLOW}{t('speed')}:{Colors.RESET} {int(speed_calc)} pass/s")
                print(f"  {Colors.YELLOW}{t('time')}:{Colors.RESET} {format_time(elapsed)}")
                print(f"  {Colors.YELLOW}{t('eta')}:{Colors.RESET} {format_time(remaining)}")
                print(f"  {Colors.YELLOW}{t('success')}:{Colors.RESET} {success}")
                print(f"{Colors.BLUE}{'=' * 54}{Colors.RESET}\n")
                
                print(f"{Colors.MAGENTA}{'=' * 54}{Colors.RESET}")
                print(f"{Colors.BOLD}{Colors.WHITE}  {t('progress').upper()}{Colors.RESET}")
                print(f"{Colors.MAGENTA}{'-' * 54}{Colors.RESET}")
                bar = create_bar(progress, 45)
                print(f"  {Colors.GREEN}{bar}{Colors.RESET} {progress:.3f}%")
                print(f"{Colors.MAGENTA}{'=' * 54}{Colors.RESET}\n")
                
                print(f"{Colors.YELLOW}{'=' * 54}{Colors.RESET}")
                print(f"{Colors.BOLD}{Colors.WHITE}  {t('testing').upper()}{Colors.RESET}")
                print(f"{Colors.YELLOW}{'-' * 54}{Colors.RESET}")
                pwd_show = current_pwd[:48] if len(current_pwd) <= 48 else current_pwd[:45] + "..."
                status = f"{Colors.GREEN}✓{Colors.RESET}" if success == 1 else f"{Colors.RED}→{Colors.RESET}"
                print(f"  {status} {Colors.WHITE}{pwd_show}{Colors.RESET}")
                print(f"{Colors.YELLOW}{'=' * 54}{Colors.RESET}\n")
                
                print(f"{Colors.RED}{'=' * 54}{Colors.RESET}")
                print(f"{Colors.BOLD}{Colors.WHITE}  {t('recent').upper()}{Colors.RESET}")
                print(f"{Colors.RED}{'-' * 54}{Colors.RESET}")
                for pwd in reversed(recent[-5:]):
                    p_show = pwd[:48] if len(pwd) <= 48 else pwd[:45] + "..."
                    print(f"  {Colors.DIM}{p_show}{Colors.RESET}")
                print(f"{Colors.RED}{'=' * 54}{Colors.RESET}\n")
                
                print(f"{Colors.DIM}[{t('stop')}]{Colors.RESET}")
            
            time.sleep(0.000001)
            
        if success == 1:
            time.sleep(1)
            clear()
            print_banner()
            print(f"\n{Colors.GREEN}{'=' * 54}{Colors.RESET}")
            print(f"{Colors.GREEN}{Colors.BOLD}  🎉 {t('found').upper()}{Colors.RESET}")
            print(f"{Colors.GREEN}{'=' * 54}{Colors.RESET}\n")
            print(f"  {Colors.WHITE}{t('platform')}:{Colors.RESET} {Colors.CYAN}{platform}{Colors.RESET}")
            print(f"  {Colors.WHITE}{t('user')}:{Colors.RESET} {Colors.CYAN}{username}{Colors.RESET}")
            print(f"  {Colors.WHITE}{t('password')}:{Colors.RESET} {Colors.GREEN}{Colors.BOLD}{target_password}{Colors.RESET}")
            print(f"  {Colors.WHITE}{t('generator')}:{Colors.RESET} {Colors.YELLOW}{gen_name}{Colors.RESET}")
            print(f"  {Colors.WHITE}{t('attempts')}:{Colors.RESET} {format_number(attempt_count)}")
            print(f"  {Colors.WHITE}{t('total_time')}:{Colors.RESET} {format_time(elapsed)}")
            print(f"  {Colors.WHITE}{t('speed')}:{Colors.RESET} {int(speed_calc)} pass/s")
            print(f"\n{Colors.GREEN}{'=' * 54}{Colors.RESET}\n")

    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}{'=' * 54}{Colors.RESET}")
        print(f"{Colors.YELLOW}{Colors.BOLD}  {t('stopped').upper()}{Colors.RESET}")
        print(f"{Colors.YELLOW}{'=' * 54}{Colors.RESET}\n")
        print(f"  {Colors.WHITE}{t('attempts')}:{Colors.RESET} {format_number(attempt_count)}")
        print(f"  {Colors.WHITE}{t('total_time')}:{Colors.RESET} {format_time(elapsed)}\n")

def select_platform():
    platforms = {
        '1': ('Instagram', '📷'),
        '2': ('Facebook', '👤'),
        '3': ('X (Twitter)', '🐦'),
        '4': ('Roblox', '🎮'),
        '5': ('Gmail', '📧')
    }
    clear()
    print_banner()
    print(f"{Colors.GREEN}{'=' * 40}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.WHITE}  {t('select_platform')}{Colors.RESET}")
    print(f"{Colors.GREEN}{'=' * 40}{Colors.RESET}")
    for k, (name, emoji) in platforms.items():
        print(f"  {Colors.CYAN}[{k}]{Colors.RESET} {emoji}  {name}")
    print(f"  {Colors.RED}[0]{Colors.RESET} 🚪 {t('exit')}")
    print(f"{Colors.GREEN}{'=' * 40}{Colors.RESET}")
    
    choice = input(f"\n{Colors.YELLOW}> {Colors.RESET}").strip()
    if choice == '0':
        print(f"\n{Colors.CYAN}{t('goodbye')}{Colors.RESET}\n")
        sys.exit(0)
    return platforms.get(choice, ('Instagram', '📷'))[0]

def get_username(platform):
    clear()
    print_banner()
    print(f"{Colors.CYAN}{'=' * 40}{Colors.RESET}")
    print(f"  {t('platform')}: {Colors.WHITE}{platform}{Colors.RESET}")
    print(f"{Colors.CYAN}{'=' * 40}{Colors.RESET}\n")
    username = input(f"{Colors.YELLOW}{t('target_user')}: {Colors.RESET}").strip()
    if not username:
        print(f"{Colors.RED}{t('must_enter')}{Colors.RESET}")
        time.sleep(1)
        return get_username(platform)
    return username

def select_generator():
    gens = {
        '1': ('Random', PasswordGenerators.random_basic),
        '2': ('ESET', PasswordGenerators.eset_style),
        '3': ('Strong', PasswordGenerators.strong_style),
        '4': ('Google', PasswordGenerators.google_style),
        '5': ('KeePass', PasswordGenerators.keepass_style),
        '6': ('NordPass', PasswordGenerators.nordpass_style),
        '7': ('Avast', PasswordGenerators.avast_style),
        '8': ('Proton', PasswordGenerators.proton_style),
    }
    clear()
    print_banner()
    print(f"{Colors.GREEN}{'=' * 40}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.WHITE}  {t('select_generator')}{Colors.RESET}")
    print(f"{Colors.GREEN}{'=' * 40}{Colors.RESET}")
    for k, (name, _) in gens.items():
        print(f"  {Colors.CYAN}[{k}]{Colors.RESET} 🔑 {name}")
    print(f"{Colors.GREEN}{'=' * 40}{Colors.RESET}")
    
    choice = input(f"\n{Colors.YELLOW}> {Colors.RESET}").strip()
    return gens.get(choice, ('Random', PasswordGenerators.random_basic))

def select_speed():
    speeds = {
        '1': 10,
        '2': 50,
        '3': 100,
        '4': 500,
        '5': 1000,
    }
    clear()
    print_banner()
    print(f"{Colors.GREEN}{'=' * 40}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.WHITE}  {t('select_speed')}{Colors.RESET}")
    print(f"{Colors.GREEN}{'=' * 40}{Colors.RESET}")
    print(f"  {Colors.YELLOW}[1]{Colors.RESET} ⚡ Lenta (10 p/s)")
    print(f"  {Colors.YELLOW}[2]{Colors.RESET} ⚡ Media (50 p/s)")
    print(f"  {Colors.YELLOW}[3]{Colors.RESET} ⚡ Rápida (100 p/s)")
    print(f"  {Colors.YELLOW}[4]{Colors.RESET} ⚡⚡ Muy Rápida (500 p/s)")
    print(f"  {Colors.YELLOW}[5]{Colors.RESET} ⚡⚡⚡ Extrema (1000 p/s)")
    print(f"{Colors.GREEN}{'=' * 40}{Colors.RESET}")
    
    choice = input(f"\n{Colors.YELLOW}> {Colors.RESET}").strip()
    return speeds.get(choice, 100)

def main():
    try:
        select_language()
        if not initial_login():
            return
        
        platform = select_platform()
        username = get_username(platform)
        gen_name, gen_func = select_generator()
        speed = select_speed()
        
        simulate_attack(platform, username, speed, gen_name, gen_func)
        
    except KeyboardInterrupt:
        print(f"\n\n{Colors.CYAN}{t('goodbye')}{Colors.RESET}\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.RED}Error: {str(e)}{Colors.RESET}\n")
        sys.exit(1)

if __name__ == "__main__":
    main()#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import random
import string
import os
import sys
import getpass

TOTAL_PASSWORDS_DB = 1_000_000_000
UI_UPDATE_RATE = 0.2

LANG = {
    'es': {
        'banner_by': 'By: Dev Secret Society',
        'banner_version': 'v2.5 (Optimizado)',
        'select_lang': 'Selecciona tu idioma',
        'login_title': 'INICIO DE SESIÓN',
        'password_prompt': 'Contraseña',
        'wrong_pass': 'Contraseña incorrecta. Intento',
        'too_many_attempts': 'Demasiados intentos. Saliendo...',
        'starting_attack': 'Iniciando ataque...',
        'loading': 'Cargando',
        'generator': 'Generador',
        'target': 'OBJETIVO',
        'platform': 'Plataforma',
        'user': 'Usuario',
        'stats': 'ESTADÍSTICAS',
        'attempts': 'Intentos',
        'speed': 'Velocidad',
        'time': 'Tiempo',
        'eta': 'ETA',
        'success': 'Exitosos',
        'progress': 'Progreso',
        'testing': 'Probando',
        'recent': 'Recientes',
        'stop': 'Ctrl+C para detener',
        'found': 'CONTRASEÑA ENCONTRADA',
        'password': 'Contraseña',
        'total_time': 'Tiempo total',
        'stopped': 'Ataque detenido',
        'select_platform': 'SELECCIONA PLATAFORMA',
        'select_generator': 'SELECCIONA GENERADOR',
        'select_speed': 'SELECCIONA VELOCIDAD',
        'exit': 'Salir',
        'goodbye': 'Hasta luego!',
        'target_user': 'Usuario objetivo',
        'must_enter': 'Debes ingresar un usuario',
    },
    'en': {
        'banner_by': 'By: Dev Secret Society',
        'banner_version': 'v2.5 (Optimized)',
        'select_lang': 'Select language',
        'login_title': 'LOGIN',
        'password_prompt': 'Password',
        'wrong_pass': 'Wrong password. Attempt',
        'too_many_attempts': 'Too many attempts. Exiting...',
        'starting_attack': 'Starting attack...',
        'loading': 'Loading',
        'generator': 'Generator',
        'target': 'TARGET',
        'platform': 'Platform',
        'user': 'User',
        'stats': 'STATISTICS',
        'attempts': 'Attempts',
        'speed': 'Speed',
        'time': 'Time',
        'eta': 'ETA',
        'success': 'Success',
        'progress': 'Progress',
        'testing': 'Testing',
        'recent': 'Recent',
        'stop': 'Ctrl+C to stop',
        'found': 'PASSWORD FOUND',
        'password': 'Password',
        'total_time': 'Total time',
        'stopped': 'Attack stopped',
        'select_platform': 'SELECT PLATFORM',
        'select_generator': 'SELECT GENERATOR',
        'select_speed': 'SELECT SPEED',
        'exit': 'Exit',
        'goodbye': 'Goodbye!',
        'target_user': 'Target user',
        'must_enter': 'You must enter a user',
    }
}

current_lang = 'es'

def t(key):
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

def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def print_banner():
    print(f"{Colors.CYAN}{Colors.BOLD}")
    print("=" * 54)
    print("██████╗ ██████╗ ██╗   ██╗████████╗███████╗")
    print("██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝")
    print("██████╔╝██████╔╝██║   ██║   ██║   █████╗  ")
    print("██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  ")
    print("██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗")
    print("╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝")
    print("")
    print("███████╗ ██████╗ ██████╗  ██████╗███████╗")
    print("██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝")
    print("█████╗  ██║   ██║██████╔╝██║     █████╗  ")
    print("██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝  ")
    print("██║     ╚██████╔╝██║  ██║╚██████╗███████╗")
    print("╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝")
    print("=" * 54)
    print(f"{Colors.RESET}{Colors.YELLOW}{t('banner_by')} | {t('banner_version')}{Colors.RESET}")
    print()

def select_language():
    clear()
    print(f"\n{Colors.CYAN}{'=' * 40}{Colors.RESET}")
    print(f"{Colors.WHITE}{Colors.BOLD}  {t('select_lang')}{Colors.RESET}")
    print(f"{Colors.CYAN}{'=' * 40}{Colors.RESET}")
    print(f"  {Colors.GREEN}[1]{Colors.RESET} 🇪🇸 Español")
    print(f"  {Colors.BLUE}[2]{Colors.RESET} 🇬🇧 English")
    print(f"{Colors.CYAN}{'=' * 40}{Colors.RESET}")
    
    choice = input(f"\n{Colors.YELLOW}> {Colors.RESET}").strip()
    
    global current_lang
    current_lang = 'en' if choice == '2' else 'es'
    return current_lang

def initial_login():
    clear()
    print(f"\n{Colors.MAGENTA}{Colors.BOLD}")
    print("  ███╗   ██╗███████╗██╗  ██╗ ██████╗ ")
    print("  ████╗  ██║██╔════╝╚██╗██╔╝██╔═══██╗")
    print("  ██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║")
    print("  ██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║")
    print("  ██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝")
    print(f"  ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ {Colors.RESET}")
    print(f"{Colors.YELLOW}          by nixu dev{Colors.RESET}\n")
    print(f"{Colors.CYAN}{'=' * 40}{Colors.RESET}")
    print(f"{Colors.WHITE}{Colors.BOLD}  {t('login_title')}{Colors.RESET}")
    print(f"{Colors.CYAN}{'=' * 40}{Colors.RESET}")
    
    for attempt in range(3):
        try:
            password = getpass.getpass(f"\n{Colors.YELLOW}{t('password_prompt')}: {Colors.RESET}").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            sys.exit(0)
            
        if password == "nexo":
            print(f"{Colors.GREEN}✓ Acceso concedido{Colors.RESET}")
            time.sleep(1)
            return True
        print(f"{Colors.RED}✗ {t('wrong_pass')} {attempt + 1}/3{Colors.RESET}")
        time.sleep(1)
    
    print(f"\n{Colors.RED}{t('too_many_attempts')}{Colors.RESET}")
    sys.exit(0)

class PasswordGenerators:
    @staticmethod
    def random_basic(length=8):
        return ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=random.randint(4, length)))
    
    @staticmethod
    def eset_style():
        length = random.randint(12, 16)
        pwd = [random.choice(string.ascii_uppercase), random.choice(string.ascii_lowercase),
               random.choice(string.digits), random.choice("!@#$%^&*")]
        pwd.extend(random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=length-4))
        random.shuffle(pwd)
        return ''.join(pwd)
    
    @staticmethod
    def strong_style():
        length = random.randint(14, 20)
        pwd = []
        for _ in range(length // 4):
            pwd.append(random.choice(string.ascii_uppercase))
        for _ in range(length // 4):
            pwd.append(random.choice(string.ascii_lowercase))
        for _ in range(length // 4):
            pwd.append(random.choice(string.digits))
        pwd.extend(random.choices("!@#$%^&*()_+-=[]{}|;:,.<>?", k=length - len(pwd)))
        random.shuffle(pwd)
        return ''.join(pwd)
    
    @staticmethod
    def google_style():
        length = random.randint(12, 15)
        pwd = [random.choice(string.ascii_uppercase)]
        pwd.extend(random.choices(string.ascii_letters + string.digits + "!@#$%&*", k=length-1))
        return ''.join(pwd)
    
    @staticmethod
    def keepass_style():
        return ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?/~`", k=random.randint(16, 24)))
    
    @staticmethod
    def nordpass_style():
        length = random.randint(12, 18)
        pwd = []
        for i in range(length):
            if i % 3 == 0:
                pwd.append(random.choice(string.ascii_uppercase))
            elif i % 3 == 1:
                pwd.append(random.choice(string.digits))
            else:
                pwd.append(random.choice(string.ascii_lowercase + "!@#$%"))
        return ''.join(pwd)
    
    @staticmethod
    def avast_style():
        segs = [''.join([random.choice(string.ascii_uppercase)] + random.choices(string.ascii_lowercase, k=2) + [random.choice(string.digits)]) for _ in range(3)]
        return ''.join(segs)[:random.randint(10, 14)] + random.choice("!@#$%")
    
    @staticmethod
    def proton_style():
        length = random.randint(16, 20)
        pwd = [random.choice(string.ascii_uppercase), random.choice(string.ascii_lowercase),
               random.choice(string.digits), random.choice("!@#$%^&*")]
        pwd.extend(random.choices(string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?", k=length-4))
        random.shuffle(pwd)
        return ''.join(pwd)

def load_target_data(platform, username):
    target_data = {
        ("Instagram", "kim_azg"): ("aoMO45nLpy-Ptwr", 180)
    }
    return target_data.get((platform, username.lower()), (None, None))

def format_time(s):
    s = int(s)
    if s < 60: 
        return f"{s}s"
    if s < 3600: 
        m, s = divmod(s, 60)
        return f"{m}m {s}s"
    h, r = divmod(s, 3600)
    m, s = divmod(r, 60)
    return f"{h}h {m}m {s}s"

def format_number(n):
    return f"{n:,}".replace(',', '.')

def create_bar(percent, width=30):
    filled = int(width * percent / 100)
    return '█' * filled + '░' * (width - filled)

def simulate_attack(platform, username, speed, gen_name, gen_func):
    target_password, target_time = load_target_data(platform, username)
    
    attempt_count = 0
    start_time = time.time()
    last_update = start_time
    recent = []
    success = 0
    current_pwd = ""
    
    clear()
    print_banner()
    print(f"{Colors.YELLOW}[!] {t('starting_attack')}{Colors.RESET}")
    print(f"{Colors.CYAN}[+] {t('generator')}: {gen_name}{Colors.RESET}")
    for i in range(3):
        print(f"{Colors.DIM}{t('loading')}{'.' * (i+1)}{Colors.RESET}", end='\r')
        time.sleep(0.5)
    print()

    try:
        while attempt_count < TOTAL_PASSWORDS_DB and success == 0:
            current_pwd = gen_func()
            attempt_count += 1
            
            elapsed = time.time() - start_time
            
            if target_password and elapsed >= target_time and success == 0:
                current_pwd = target_password
                success = 1
            
            recent.append(current_pwd)
            if len(recent) > 5:
                recent.pop(0)

            if time.time() - last_update >= UI_UPDATE_RATE or success == 1:
                last_update = time.time()
                
                speed_calc = attempt_count / elapsed if elapsed > 0 else 0
                progress = (attempt_count / TOTAL_PASSWORDS_DB) * 100
                remaining = (TOTAL_PASSWORDS_DB - attempt_count) / speed_calc if speed_calc > 0 else 0
                
                clear()
                print_banner()
                
                print(f"{Colors.CYAN}{'=' * 54}{Colors.RESET}")
                print(f"{Colors.BOLD}{Colors.WHITE}  {t('target').upper()}{Colors.RESET}")
                print(f"{Colors.CYAN}{'-' * 54}{Colors.RESET}")
                print(f"  {Colors.CYAN}{t('platform')}:{Colors.RESET} {platform}")
                print(f"  {Colors.CYAN}{t('user')}:{Colors.RESET} {username}")
                print(f"  {Colors.CYAN}{t('generator')}:{Colors.RESET} {gen_name}")
                print(f"{Colors.CYAN}{'=' * 54}{Colors.RESET}\n")
                
                print(f"{Colors.BLUE}{'=' * 54}{Colors.RESET}")
                print(f"{Colors.BOLD}{Colors.WHITE}  {t('stats').upper()}{Colors.RESET}")
                print(f"{Colors.BLUE}{'-' * 54}{Colors.RESET}")
                print(f"  {Colors.YELLOW}{t('attempts')}:{Colors.RESET} {format_number(attempt_count)}")
                print(f"  {Colors.YELLOW}{t('speed')}:{Colors.RESET} {int(speed_calc)} pass/s")
                print(f"  {Colors.YELLOW}{t('time')}:{Colors.RESET} {format_time(elapsed)}")
                print(f"  {Colors.YELLOW}{t('eta')}:{Colors.RESET} {format_time(remaining)}")
                print(f"  {Colors.YELLOW}{t('success')}:{Colors.RESET} {success}")
                print(f"{Colors.BLUE}{'=' * 54}{Colors.RESET}\n")
                
                print(f"{Colors.MAGENTA}{'=' * 54}{Colors.RESET}")
                print(f"{Colors.BOLD}{Colors.WHITE}  {t('progress').upper()}{Colors.RESET}")
                print(f"{Colors.MAGENTA}{'-' * 54}{Colors.RESET}")
                bar = create_bar(progress, 45)
                print(f"  {Colors.GREEN}{bar}{Colors.RESET} {progress:.3f}%")
                print(f"{Colors.MAGENTA}{'=' * 54}{Colors.RESET}\n")
                
                print(f"{Colors.YELLOW}{'=' * 54}{Colors.RESET}")
                print(f"{Colors.BOLD}{Colors.WHITE}  {t('testing').upper()}{Colors.RESET}")
                print(f"{Colors.YELLOW}{'-' * 54}{Colors.RESET}")
                pwd_show = current_pwd[:48] if len(current_pwd) <= 48 else current_pwd[:45] + "..."
                status = f"{Colors.GREEN}✓{Colors.RESET}" if success == 1 else f"{Colors.RED}→{Colors.RESET}"
                print(f"  {status} {Colors.WHITE}{pwd_show}{Colors.RESET}")
                print(f"{Colors.YELLOW}{'=' * 54}{Colors.RESET}\n")
                
                print(f"{Colors.RED}{'=' * 54}{Colors.RESET}")
                print(f"{Colors.BOLD}{Colors.WHITE}  {t('recent').upper()}{Colors.RESET}")
                print(f"{Colors.RED}{'-' * 54}{Colors.RESET}")
                for pwd in reversed(recent[-5:]):
                    p_show = pwd[:48] if len(pwd) <= 48 else pwd[:45] + "..."
                    print(f"  {Colors.DIM}{p_show}{Colors.RESET}")
                print(f"{Colors.RED}{'=' * 54}{Colors.RESET}\n")
                
                print(f"{Colors.DIM}[{t('stop')}]{Colors.RESET}")
            
            time.sleep(0.000001)
            
        if success == 1:
            time.sleep(1)
            clear()
            print_banner()
            print(f"\n{Colors.GREEN}{'=' * 54}{Colors.RESET}")
            print(f"{Colors.GREEN}{Colors.BOLD}  🎉 {t('found').upper()}{Colors.RESET}")
            print(f"{Colors.GREEN}{'=' * 54}{Colors.RESET}\n")
            print(f"  {Colors.WHITE}{t('platform')}:{Colors.RESET} {Colors.CYAN}{platform}{Colors.RESET}")
            print(f"  {Colors.WHITE}{t('user')}:{Colors.RESET} {Colors.CYAN}{username}{Colors.RESET}")
            print(f"  {Colors.WHITE}{t('password')}:{Colors.RESET} {Colors.GREEN}{Colors.BOLD}{target_password}{Colors.RESET}")
            print(f"  {Colors.WHITE}{t('generator')}:{Colors.RESET} {Colors.YELLOW}{gen_name}{Colors.RESET}")
            print(f"  {Colors.WHITE}{t('attempts')}:{Colors.RESET} {format_number(attempt_count)}")
            print(f"  {Colors.WHITE}{t('total_time')}:{Colors.RESET} {format_time(elapsed)}")
            print(f"  {Colors.WHITE}{t('speed')}:{Colors.RESET} {int(speed_calc)} pass/s")
            print(f"\n{Colors.GREEN}{'=' * 54}{Colors.RESET}\n")

    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}{'=' * 54}{Colors.RESET}")
        print(f"{Colors.YELLOW}{Colors.BOLD}  {t('stopped').upper()}{Colors.RESET}")
        print(f"{Colors.YELLOW}{'=' * 54}{Colors.RESET}\n")
        print(f"  {Colors.WHITE}{t('attempts')}:{Colors.RESET} {format_number(attempt_count)}")
        print(f"  {Colors.WHITE}{t('total_time')}:{Colors.RESET} {format_time(elapsed)}\n")

def select_platform():
    platforms = {
        '1': ('Instagram', '📷'),
        '2': ('Facebook', '👤'),
        '3': ('X (Twitter)', '🐦'),
        '4': ('Roblox', '🎮'),
        '5': ('Gmail', '📧')
    }
    clear()
    print_banner()
    print(f"{Colors.GREEN}{'=' * 40}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.WHITE}  {t('select_platform')}{Colors.RESET}")
    print(f"{Colors.GREEN}{'=' * 40}{Colors.RESET}")
    for k, (name, emoji) in platforms.items():
        print(f"  {Colors.CYAN}[{k}]{Colors.RESET} {emoji}  {name}")
    print(f"  {Colors.RED}[0]{Colors.RESET} 🚪 {t('exit')}")
    print(f"{Colors.GREEN}{'=' * 40}{Colors.RESET}")
    
    choice = input(f"\n{Colors.YELLOW}> {Colors.RESET}").strip()
    if choice == '0':
        print(f"\n{Colors.CYAN}{t('goodbye')}{Colors.RESET}\n")
        sys.exit(0)
    return platforms.get(choice, ('Instagram', '📷'))[0]

def get_username(platform):
    clear()
    print_banner()
    print(f"{Colors.CYAN}{'=' * 40}{Colors.RESET}")
    print(f"  {t('platform')}: {Colors.WHITE}{platform}{Colors.RESET}")
    print(f"{Colors.CYAN}{'=' * 40}{Colors.RESET}\n")
    username = input(f"{Colors.YELLOW}{t('target_user')}: {Colors.RESET}").strip()
    if not username:
        print(f"{Colors.RED}{t('must_enter')}{Colors.RESET}")
        time.sleep(1)
        return get_username(platform)
    return username

def select_generator():
    gens = {
        '1': ('Random', PasswordGenerators.random_basic),
        '2': ('ESET', PasswordGenerators.eset_style),
        '3': ('Strong', PasswordGenerators.strong_style),
        '4': ('Google', PasswordGenerators.google_style),
        '5': ('KeePass', PasswordGenerators.keepass_style),
        '6': ('NordPass', PasswordGenerators.nordpass_style),
        '7': ('Avast', PasswordGenerators.avast_style),
        '8': ('Proton', PasswordGenerators.proton_style),
    }
    clear()
    print_banner()
    print(f"{Colors.GREEN}{'=' * 40}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.WHITE}  {t('select_generator')}{Colors.RESET}")
    print(f"{Colors.GREEN}{'=' * 40}{Colors.RESET}")
    for k, (name, _) in gens.items():
        print(f"  {Colors.CYAN}[{k}]{Colors.RESET} 🔑 {name}")
    print(f"{Colors.GREEN}{'=' * 40}{Colors.RESET}")
    
    choice = input(f"\n{Colors.YELLOW}> {Colors.RESET}").strip()
    return gens.get(choice, ('Random', PasswordGenerators.random_basic))

def select_speed():
    speeds = {
        '1': 10,
        '2': 50,
        '3': 100,
        '4': 500,
        '5': 1000,
    }
    clear()
    print_banner()
    print(f"{Colors.GREEN}{'=' * 40}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.WHITE}  {t('select_speed')}{Colors.RESET}")
    print(f"{Colors.GREEN}{'=' * 40}{Colors.RESET}")
    print(f"  {Colors.YELLOW}[1]{Colors.RESET} ⚡ Normal (10 p/s)")
    print(f"  {Colors.YELLOW}[2]{Colors.RESET} ⚡ Moderada (50 p/s)")
    print(f"  {Colors.YELLOW}[3]{Colors.RESET} ⚡ Media (100 p/s)")
    print(f"  {Colors.YELLOW}[4]{Colors.RESET} ⚡⚡ Rápida (500 p/s)")
    print(f"  {Colors.YELLOW}[5]{Colors.RESET} ⚡⚡⚡ Eficiente (1000 p/s)")
    print(f"{Colors.GREEN}{'=' * 40}{Colors.RESET}")
    
    choice = input(f"\n{Colors.YELLOW}> {Colors.RESET}").strip()
    return speeds.get(choice, 100)

def main():
    try:
        select_language()
        if not initial_login():
            return
        
        platform = select_platform()
        username = get_username(platform)
        gen_name, gen_func = select_generator()
        speed = select_speed()
        
        simulate_attack(platform, username, speed, gen_name, gen_func)
        
    except KeyboardInterrupt:
        print(f"\n\n{Colors.CYAN}{t('goodbye')}{Colors.RESET}\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.RED}Error: {str(e)}{Colors.RESET}\n")
        sys.exit(1)

if __name__ == "__main__":
    main()

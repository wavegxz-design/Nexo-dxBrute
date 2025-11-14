#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import random
import string
import os
import sys
import getpass
from datetime import datetime

TOTAL_PASSWORDS_DB = 1_000_000_000
UI_UPDATE_RATE = 0.15

LANG = {
    'es': {
        'banner_by': 'By: Dev Secret Society',
        'banner_version': 'v2.4 (Optimizado)',
        'select_lang': 'Selecciona tu idioma / Select your language',
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
        'current_speed': 'Velocidad',
        'active_time': 'Tiempo activo',
        'remaining_time': 'Tiempo restante',
        'success_attempts': 'Exitosos',
        'failed_attempts': 'Fallidos',
        'progress': 'PROGRESO DEL ATAQUE',
        'testing_pass': 'PROBANDO CONTRASEÑA',
        'recent_attempts': 'ÚLTIMOS INTENTOS',
        'id_col': '#ID',
        'password_col': 'CONTRASEÑA',
        'status_col': 'ESTADO',
        'access_granted': '✓ ACCESO',
        'access_denied': '✗ DENEGADO',
        'stop_attack': 'Presiona Ctrl+C para detener',
        'pass_found': '¡CONTRASEÑA ENCONTRADA!',
        'password': 'Contraseña',
        'generator_used': 'Generador',
        'attempts_made': 'Intentos',
        'total_time': 'Tiempo',
        'avg_speed': 'Velocidad',
        'attack_stopped': 'Ataque detenido por el usuario',
        'select_generator': 'SELECCIONA EL GENERADOR',
        'auto_mode': 'AUTO (Todos)',
        'generator_info': 'Cada generador simula patrones específicos',
        'select_platform': 'SELECCIONA LA PLATAFORMA',
        'exit': 'Salir',
        'goodbye': '¡Hasta luego!',
        'invalid_option': 'Opción inválida',
        'target_user': 'Usuario objetivo',
        'target_email': 'Email objetivo',
        'must_enter': 'Debes ingresar un',
        'select_speed': 'SELECCIONA LA VELOCIDAD',
        'slow': 'Lenta',
        'medium': 'Media',
        'fast': 'Rápida',
        'very_fast': 'Muy Rápida',
        'extreme': 'Extrema',
        'db_total': f'de {TOTAL_PASSWORDS_DB:,}'.replace(',', '.'),
    },
    'en': {
        'banner_by': 'By: Dev Secret Society',
        'banner_version': 'v2.4 (Optimized)',
        'select_lang': 'Select language',
        'login_title': 'Login to continue',
        'password_prompt': 'Password',
        'wrong_pass': 'Wrong password. Attempt',
        'too_many_attempts': 'Too many attempts. Exiting...',
        'starting_attack': 'Starting attack...',
        'generator': 'Generator',
        'target': 'TARGET',
        'platform': 'Platform',
        'user': 'User',
        'stats': 'STATISTICS',
        'total_attempts': 'Total attempts',
        'database': 'Database',
        'current_speed': 'Speed',
        'active_time': 'Active time',
        'remaining_time': 'Remaining',
        'success_attempts': 'Success',
        'failed_attempts': 'Failed',
        'progress': 'PROGRESS',
        'testing_pass': 'TESTING PASSWORD',
        'recent_attempts': 'RECENT ATTEMPTS',
        'id_col': '#ID',
        'password_col': 'PASSWORD',
        'status_col': 'STATUS',
        'access_granted': '✓ ACCESS',
        'access_denied': '✗ DENIED',
        'stop_attack': 'Press Ctrl+C to stop',
        'pass_found': 'PASSWORD FOUND!',
        'password': 'Password',
        'generator_used': 'Generator',
        'attempts_made': 'Attempts',
        'total_time': 'Time',
        'avg_speed': 'Speed',
        'attack_stopped': 'Attack stopped',
        'select_generator': 'SELECT GENERATOR',
        'select_platform': 'SELECT PLATFORM',
        'exit': 'Exit',
        'goodbye': 'Goodbye!',
        'invalid_option': 'Invalid option',
        'target_user': 'Target user',
        'target_email': 'Target email',
        'must_enter': 'You must enter',
        'select_speed': 'SELECT SPEED',
        'db_total': f'of {TOTAL_PASSWORDS_DB:,}'.replace(',', '.'),
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

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        print("\033[H\033[2J\033[3J", end='')
        sys.stdout.flush()

def print_banner():
    banner = f"""
{Colors.CYAN}{Colors.BOLD}
╔══════════════════════════════════════════════════════╗
║  ██████╗ ██████╗ ██╗   ██╗████████╗███████╗        ║
║  ██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝        ║
║  ██████╔╝██████╔╝██║   ██║   ██║   █████╗          ║
║  ██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝          ║
║  ██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗        ║
║  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝        ║
║                                                      ║
║  ███████╗ ██████╗ ██████╗  ██████╗███████╗         ║
║  ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝         ║
║  █████╗  ██║   ██║██████╔╝██║     █████╗           ║
║  ██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝           ║
║  ██║     ╚██████╔╝██║  ██║╚██████╗███████╗         ║
║  ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝         ║
╚══════════════════════════════════════════════════════╝{Colors.RESET}
{Colors.YELLOW}        {t('banner_by')} | {t('banner_version')}{Colors.RESET}
"""
    print(banner)

def select_language():
    clear_screen()
    print(f"\n{Colors.CYAN}╔═══════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.CYAN}║{Colors.WHITE}  {t('select_lang'):^27}  {Colors.CYAN}║{Colors.RESET}")
    print(f"{Colors.CYAN}╠═══════════════════════════════╣{Colors.RESET}")
    print(f"{Colors.CYAN}║{Colors.RESET}  {Colors.GREEN}[1]{Colors.RESET} 🇪🇸 Español           {Colors.CYAN}║{Colors.RESET}")
    print(f"{Colors.CYAN}║{Colors.RESET}  {Colors.BLUE}[2]{Colors.RESET} 🇬🇧 English           {Colors.CYAN}║{Colors.RESET}")
    print(f"{Colors.CYAN}╚═══════════════════════════════╝{Colors.RESET}")
    
    choice = input(f"\n{Colors.YELLOW}└──> {Colors.RESET}").strip()
    
    global current_lang
    current_lang = 'en' if choice == '2' else 'es'
    return current_lang

def initial_login():
    clear_screen()
    print(f"\n{Colors.MAGENTA}{Colors.BOLD}")
    print("  ███╗   ██╗███████╗██╗  ██╗ ██████╗ ")
    print("  ████╗  ██║██╔════╝╚██╗██╔╝██╔═══██╗")
    print("  ██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║")
    print("  ██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║")
    print("  ██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝")
    print(f"  ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ {Colors.RESET}")
    print(f"{Colors.YELLOW}          by nixu dev{Colors.RESET}\n")
    print(f"{Colors.CYAN}╔══════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.CYAN}║{Colors.WHITE}  {t('login_title'):^30}  {Colors.CYAN}║{Colors.RESET}")
    print(f"{Colors.CYAN}╚══════════════════════════════════╝{Colors.RESET}")
    
    for attempt in range(3):
        try:
            password = getpass.getpass(f"\n{Colors.YELLOW}{t('password_prompt')}: {Colors.RESET}").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n")
            sys.exit(0)
            
        if password == "nexo":
            print(f"{Colors.GREEN}✓ {t('access_granted')}{Colors.RESET}")
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

def create_progress_bar(progress, width=40):
    filled = int(width * progress / 100)
    bar = '█' * filled + '░' * (width - filled)
    return f"{Colors.GREEN}{bar}{Colors.RESET}"

def simulate_attack(platform, username, speed, gen_name, gen_func):
    target_password, target_time = load_target_data(platform, username)
    
    attempt_count = 0
    start_time = time.time()
    last_update_time = start_time
    recent = []
    success = 0
    current_password = ""
    
    clear_screen()
    print_banner()
    print(f"\n{Colors.YELLOW}[!] {t('starting_attack')}{Colors.RESET}")
    print(f"{Colors.CYAN}[+] {t('generator')}: {Colors.WHITE}{gen_name}{Colors.RESET}")
    time.sleep(2)

    try:
        while attempt_count < TOTAL_PASSWORDS_DB and success == 0:
            pwd = gen_func()
            attempt_count += 1
            current_password = pwd
            
            elapsed = time.time() - start_time
            
            if target_password and elapsed >= target_time and success == 0:
                current_password = target_password
                success = 1
            
            if pwd != target_password or success == 1:
                recent.append(pwd)
                if len(recent) > 8:
                    recent.pop(0)

            current_time = time.time()
            if current_time - last_update_time >= UI_UPDATE_RATE or success == 1:
                last_update_time = current_time

                current_speed = attempt_count / elapsed if elapsed > 0 else 0
                progress_percent = (attempt_count / TOTAL_PASSWORDS_DB) * 100
                
                remaining_attempts = TOTAL_PASSWORDS_DB - attempt_count
                if current_speed > 0:
                    remaining_time = remaining_attempts / current_speed
                    remaining_time_str = format_time(remaining_time)
                else:
                    remaining_time_str = "--:--"
                
                clear_screen()
                print_banner()
                
                print(f"\n{Colors.CYAN}╔══════════════════════════════════════════════════╗{Colors.RESET}")
                print(f"{Colors.CYAN}║{Colors.BOLD} {t('target'):^48} {Colors.CYAN}║{Colors.RESET}")
                print(f"{Colors.CYAN}╠══════════════════════════════════════════════════╣{Colors.RESET}")
                print(f"{Colors.CYAN}║ {t('platform')}: {Colors.WHITE}{platform:<20} {Colors.CYAN}| {t('user')}: {Colors.WHITE}{username:<15} {Colors.CYAN}║{Colors.RESET}")
                print(f"{Colors.CYAN}╚══════════════════════════════════════════════════╝{Colors.RESET}")
                
                print(f"\n{Colors.BLUE}╔═════════════════════╦═════════════════════════╗{Colors.RESET}")
                print(f"{Colors.BLUE}║{Colors.BOLD} {t('stats'):^19} {Colors.BLUE}║{Colors.BOLD} {t('generator'):^23} {Colors.BLUE}║{Colors.RESET}")
                print(f"{Colors.BLUE}╠═════════════════════╬═════════════════════════╣{Colors.RESET}")
                print(f"{Colors.BLUE}║ {Colors.WHITE}{format_number(attempt_count):>19} {Colors.BLUE}║ {Colors.YELLOW}{gen_name:<23} {Colors.BLUE}║{Colors.RESET}")
                print(f"{Colors.BLUE}║ {Colors.CYAN}{int(current_speed):>14} p/s {Colors.BLUE}║ {Colors.WHITE}{format_time(elapsed):<23} {Colors.BLUE}║{Colors.RESET}")
                print(f"{Colors.BLUE}║ {Colors.MAGENTA}{remaining_time_str:>19} {Colors.BLUE}║ {Colors.GREEN}✓ {success:<21} {Colors.BLUE}║{Colors.RESET}")
                print(f"{Colors.BLUE}╚═════════════════════╩═════════════════════════╝{Colors.RESET}")

                progress_bar = create_progress_bar(progress_percent, 44)
                print(f"\n{Colors.MAGENTA}╔══════════════════════════════════════════════════╗{Colors.RESET}")
                print(f"{Colors.MAGENTA}║{Colors.BOLD} {t('progress'):^48} {Colors.MAGENTA}║{Colors.RESET}")
                print(f"{Colors.MAGENTA}╠══════════════════════════════════════════════════╣{Colors.RESET}")
                print(f"{Colors.MAGENTA}║ {progress_bar} {progress_percent:>5.2f}% {Colors.MAGENTA}║{Colors.RESET}")
                print(f"{Colors.MAGENTA}╚══════════════════════════════════════════════════╝{Colors.RESET}")

                print(f"\n{Colors.YELLOW}╔══════════════════════════════════════════════════╗{Colors.RESET}")
                print(f"{Colors.YELLOW}║{Colors.BOLD} {t('testing_pass'):^48} {Colors.YELLOW}║{Colors.RESET}")
                print(f"{Colors.YELLOW}╠══════════════════════════════════════════════════╣{Colors.RESET}")
                pwd_display = current_password[:44] if len(current_password) <= 44 else current_password[:41] + "..."
                status_icon = f"{Colors.GREEN}✓{Colors.RESET}" if success == 1 else f"{Colors.RED}→{Colors.RESET}"
                print(f"{Colors.YELLOW}║ {status_icon} {Colors.WHITE}{pwd_display:<45} {Colors.YELLOW}║{Colors.RESET}")
                print(f"{Colors.YELLOW}╚══════════════════════════════════════════════════╝{Colors.RESET}")

                print(f"\n{Colors.RED}╔══════════════════════════════════════════════════╗{Colors.RESET}")
                print(f"{Colors.RED}║{Colors.BOLD} {t('recent_attempts'):^48} {Colors.RED}║{Colors.RESET}")
                print(f"{Colors.RED}╠══════════════════════════════════════════════════╣{Colors.RESET}")
                
                for i, p in enumerate(reversed(recent[-5:]), 1):
                    p_display = p[:40] if len(p) <= 40 else p[:37] + "..."
                    print(f"{Colors.RED}║ {Colors.DIM}{p_display:<46} {Colors.RED}║{Colors.RESET}")
                
                print(f"{Colors.RED}╚══════════════════════════════════════════════════╝{Colors.RESET}")
                
                print(f"\n{Colors.DIM}[{t('stop_attack')}]{Colors.RESET}")
            
            time.sleep(0.00001)
            
        if success == 1:
            time.sleep(1)
            clear_screen()
            print_banner()
            print(f"\n{Colors.GREEN}╔══════════════════════════════════════════╗{Colors.RESET}")
            print(f"{Colors.GREEN}║  🎉 {t('pass_found'):^34}  ║{Colors.RESET}")
            print(f"{Colors.GREEN}╚══════════════════════════════════════════╝{Colors.RESET}\n")
            print(f"  {Colors.WHITE}{t('platform')}:{Colors.RESET} {Colors.CYAN}{platform}{Colors.RESET}")
            print(f"  {Colors.WHITE}{t('user')}:{Colors.RESET} {Colors.CYAN}{username}{Colors.RESET}")
            print(f"  {Colors.WHITE}{t('password')}:{Colors.RESET} {Colors.GREEN}{Colors.BOLD}{target_password}{Colors.RESET}")
            print(f"  {Colors.WHITE}{t('generator_used')}:{Colors.RESET} {Colors.YELLOW}{gen_name}{Colors.RESET}")
            print(f"  {Colors.WHITE}{t('attempts_made')}:{Colors.RESET} {format_number(attempt_count)}")
            print(f"  {Colors.WHITE}{t('total_time')}:{Colors.RESET} {format_time(elapsed)}")
            print(f"  {Colors.WHITE}{t('avg_speed')}:{Colors.RESET} {int(current_speed)} pass/s\n")

    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}╔══════════════════════════════════════╗{Colors.RESET}")
        print(f"{Colors.YELLOW}║  {t('attack_stopped'):^32}  ║{Colors.RESET}")
        print(f"{Colors.YELLOW}╚══════════════════════════════════════╝{Colors.RESET}\n")
        print(f"  {Colors.WHITE}{t('attempts_made')}:{Colors.RESET} {format_number(attempt_count)}")
        print(f"  {Colors.WHITE}{t('total_time')}:{Colors.RESET} {format_time(elapsed)}\n")

def select_platform():
    platforms = {
        '1': ('Instagram', '📷'),
        '2': ('Facebook', '👤'),
        '3': ('X (Twitter)', '🐦'),
        '4': ('Roblox', '🎮'),
        '5': ('Gmail', '📧')
    }
    clear_screen()
    print_banner()
    print(f"\n{Colors.GREEN}╔═══════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.GREEN}║{Colors.BOLD} {t('select_platform'):^27} {Colors.GREEN}║{Colors.RESET}")
    print(f"{Colors.GREEN}╠═══════════════════════════════╣{Colors.RESET}")
    for k, (name, emoji) in platforms.items():
        print(f"{Colors.GREEN}║{Colors.RESET}  {Colors.CYAN}[{k}]{Colors.RESET} {emoji}  {name:<17} {Colors.GREEN}║{Colors.RESET}")
    print(f"{Colors.GREEN}║{Colors.RESET}  {Colors.RED}[0]{Colors.RESET} 🚪 {t('exit'):<18} {Colors.GREEN}║{Colors.RESET}")
    print(f"{Colors.GREEN}╚═══════════════════════════════╝{Colors.RESET}")
    
    choice = input(f"\n{Colors.YELLOW}└──> {Colors.RESET}").strip()
    if choice == '0':
        print(f"\n{Colors.CYAN}{t('goodbye')}{Colors.RESET}\n")
        sys.exit(0)
    return platforms.get(choice, ('Instagram', '📷'))[0]

def get_username(platform):
    clear_screen()
    print_banner()
    print(f"\n{Colors.CYAN}╔═══════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.CYAN}║ {t('platform')}: {Colors.WHITE}{platform:<18} {Colors.CYAN}║{Colors.RESET}")
    print(f"{Colors.CYAN}╚═══════════════════════════════╝{Colors.RESET}\n")
    username = input(f"{Colors.YELLOW}{t('target_user')}: {Colors.RESET}").strip()
    if not username:
        print(f"{Colors.RED}{t('must_enter')} usuario{Colors.RESET}")
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
    clear_screen()
    print_banner()
    print(f"\n{Colors.GREEN}╔═══════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.GREEN}║{Colors.BOLD} {t('select_generator'):^27} {Colors.GREEN}║{Colors.RESET}")
    print(f"{Colors.GREEN}╠═══════════════════════════════╣{Colors.RESET}")
    for k, (name, _) in gens.items():
        print(f"{Colors.GREEN}║{Colors.RESET}  {Colors.CYAN}[{k}]{Colors.RESET} 🔑 {name:<18} {Colors.GREEN}║{Colors.RESET}")
    print(f"{Colors.GREEN}╚═══════════════════════════════╝{Colors.RESET}")
    
    choice = input(f"\n{Colors.YELLOW}└──> {Colors.RESET}").strip()
    return gens.get(choice, ('Random', PasswordGenerators.random_basic))

def select_speed():
    speeds = {
        '1': (10, t('slow')),
        '2': (50, t('medium')),
        '3': (100, t('fast')),
        '4': (500, t('very_fast')),
        '5': (1000, t('extreme')),
    }
    clear_screen()
    print_banner()
    print(f"\n{Colors.GREEN}╔═══════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.GREEN}║{Colors.BOLD} {t('select_speed'):^27} {Colors.GREEN}║{Colors.RESET}")
    print(f"{Colors.GREEN}╠═══════════════════════════════╣{Colors.RESET}")
    print(f"{Colors.GREEN}║{Colors.RESET}  {Colors.YELLOW}[1]{Colors.RESET} ⚡ Lenta (10 p/s)     {Colors.GREEN}║{Colors.RESET}")
    print(f"{Colors.GREEN}║{Colors.RESET}  {Colors.YELLOW}[2]{Colors.RESET} ⚡ Media (50 p/s)     {Colors.GREEN}║{Colors.RESET}")
    print(f"{Colors.GREEN}║{Colors.RESET}  {Colors.YELLOW}[3]{Colors.RESET} ⚡ Rápida (100 p/s)   {Colors.GREEN}║{Colors.RESET}")
    print(f"{Colors.GREEN}║{Colors.RESET}  {Colors.YELLOW}[4]{Colors.RESET} ⚡⚡ Muy Rápida (500) {Colors.GREEN}║{Colors.RESET}")
    print(f"{Colors.GREEN}║{Colors.RESET}  {Colors.YELLOW}[5]{Colors.RESET} ⚡⚡⚡ Extrema (1000) {Colors.GREEN}║{Colors.RESET}")
    print(f"{Colors.GREEN}╚═══════════════════════════════╝{Colors.RESET}")
    
    choice = input(f"\n{Colors.YELLOW}└──> {Colors.RESET}").strip()
    return speeds.get(choice, (100, 'Normal'))[0]

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

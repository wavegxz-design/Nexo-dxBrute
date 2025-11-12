#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import random
import string
import os
import sys
import getpass 
from datetime import datetime

# --- CONSTANTES GLOBALES DE RENDIMIENTO Y BASE DE DATOS ---
# Contraseña de la base de datos (1 Billón) para el cálculo de progreso
TOTAL_PASSWORDS_DB = 1_000_000_000 
# Tasa de actualización de la UI (en segundos). Actualiza 5 veces por segundo.
UI_UPDATE_RATE = 0.2 
# URL del repositorio proporcionado por el usuario
REPO_URL = "https://github.com/wavegxz-design/Nexo-dxBrute"

# --- SISTEMA DE IDIOMAS ---
# Palabras y términos originales
LANG = {
    'es': {
        'banner_by': 'By: Dev Secret Society',
        'banner_version': 'Version: v2.3 (Multi-idioma)',
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
        'current_speed': 'Velocidad actual',
        'active_time': 'Tiempo activo',
        'remaining_time': 'Tiempo restante (ETA)', 
        'success_attempts': 'Exitosos', 
        'failed_attempts': 'Fallidos', 
        'progress': 'PROGRESO DEL ATAQUE',
        'testing_pass': 'PROBANDO CONTRASEÑAS',
        'id_col': '#ID',
        'password_col': 'CONTRASEÑA',
        'status_col': 'ESTADO',
        'access_granted': '✓ ACCESO CONCEDIDO',
        'access_denied': '✗ DENEGADO', 
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
        'generator_info': 'Cada generador simula patrones específicos',
        'auto_info': 'AUTO probará todos los generadores',
        'select_platform': 'SELECCIONA LA PLATAFORMA OBJETIVO',
        'exit': 'Salir',
        'goodbye': '¡Hasta luego!',
        'invalid_option': 'Opción inválida',
        'target_user': 'Usuario objetivo',
        'target_email': 'Email objetivo',
        'email': 'Email',
        'must_enter': 'Debes ingresar un',
        'select_speed': 'SELECCIONA LA VELOCIDAD DE SIMULACIÓN (Intentos/segundo)',
        'slow': 'Lenta',
        'medium': 'Media',
        'fast': 'Rápida',
        'very_fast': 'Muy Rápida',
        'extreme': 'Extrema',
        'auto_testing': 'MODO AUTO',
        'db_total': f'de {TOTAL_PASSWORDS_DB:,}'.replace(',', '.'), 
        # --- Nuevo Menú ---
        'menu_title': 'MENÚ PRINCIPAL',
        'menu_bruteforce': 'Iniciar Ataque de Fuerza Bruta (Brute-Force)',
        'menu_updates': 'Ver Actualizaciones del Repositorio (GitHub)',
        'update_checking': 'Conectando con GitHub...',
        'update_found': '✅ ¡ACTUALIZACIONES DISPONIBLES!',
        'update_not_found': '✅ El repositorio está actualizado.',
        'update_error': '❌ Error al intentar conectar con GitHub.',
        'update_last_commit': 'Último Commit:',
        'update_repo': 'Repositorio:',
        'press_to_continue': 'Presiona ENTER para continuar...',
    },
    'en': {
        'banner_by': 'By: BLACKNIXU',
        'banner_version': 'Version: v2.3 (Multi-language)',
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
        'current_speed': 'Current speed',
        'active_time': 'Active time',
        'remaining_time': 'Remaining Time (ETA)',
        'success_attempts': 'Successful',
        'failed_attempts': 'Failed',
        'progress': 'PROGRESS',
        'testing_pass': 'TESTING PASSWORDS',
        'id_col': '#ID',
        'password_col': 'PASSWORD',
        'status_col': 'STATUS',
        'access_granted': '✓ GRANTED',
        'access_denied': '✗ DENIED',
        'stop_attack': 'Stop attack',
        'pass_found': 'PASSWORD FOUND!',
        'password': 'Password',
        'generator_used': 'Generator used',
        'attempts_made': 'Attempts made',
        'total_time': 'Total time',
        'avg_speed': 'Avg speed',
        'attack_stopped': 'Attack stopped',
        'select_generator': 'SELECT GENERATOR',
        'auto_mode': 'AUTO (All)',
        'generator_info': 'Each generator simulates patterns',
        'auto_info': 'AUTO will test all generators',
        'select_platform': 'SELECT PLATFORM',
        'exit': 'Exit',
        'goodbye': 'Goodbye!',
        'invalid_option': 'Invalid option',
        'target_user': 'Target user',
        'target_email': 'Target email',
        'email': 'Email',
        'must_enter': 'You must enter',
        'select_speed': 'SELECT SIMULATION SPEED (Attempts/second)',
        'auto_testing': 'AUTO MODE',
        'db_total': f'of {TOTAL_PASSWORDS_DB:,}'.replace(',', '.'),
        # --- Nuevo Menú ---
        'menu_title': 'MAIN MENU',
        'menu_bruteforce': 'Start Brute-Force Attack',
        'menu_updates': 'Check Repository Updates (GitHub)',
        'update_checking': 'Connecting to GitHub...',
        'update_found': '✅ UPDATES AVAILABLE!',
        'update_not_found': '✅ Repository is up to date.',
        'update_error': '❌ Error connecting to GitHub.',
        'update_last_commit': 'Last Commit:',
        'update_repo': 'Repository:',
        'press_to_continue': 'Press ENTER to continue...',
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
    CLEAR = '\033[2J\033[H' 

def clear_screen():
    sys.stdout.write(Colors.CLEAR)
    sys.stdout.flush()

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
    clear_screen()
    print(f"\n{Colors.CYAN}╔═══════════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.CYAN}║{Colors.WHITE}  Selecciona / Select Language        {Colors.CYAN}║{Colors.RESET}")
    print(f"{Colors.CYAN}╠═══════════════════════════════════════╣{Colors.RESET}")
    print(f"{Colors.CYAN}║{Colors.RESET}  {Colors.GREEN}[1]{Colors.RESET} 🇪🇸 Español                     {Colors.CYAN}║{Colors.RESET}")
    print(f"{Colors.CYAN}║{Colors.RESET}  {Colors.BLUE}[2]{Colors.RESET} 🇬🇧 English                     {Colors.CYAN}║{Colors.RESET}")
    print(f"{Colors.CYAN}╚═══════════════════════════════════════╝{Colors.RESET}")
    
    choice = input(f"\n{Colors.YELLOW}└──> {Colors.RESET}").strip()
    
    global current_lang
    current_lang = 'en' if choice == '2' else 'es'
    return current_lang

def initial_login():
    clear_screen()
    print(f"\n{Colors.MAGENTA}{Colors.BOLD}  ███╗   ██╗███████╗██╗  ██╗ ██████╗ {Colors.RESET}")
    print(f"{Colors.MAGENTA}{Colors.BOLD}  ████╗  ██║██╔════╝╚██╗██╔╝██╔═══██╗{Colors.RESET}")
    print(f"{Colors.MAGENTA}{Colors.BOLD}  ██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║{Colors.RESET}")
    print(f"{Colors.MAGENTA}{Colors.BOLD}  ██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║{Colors.RESET}")
    print(f"{Colors.MAGENTA}{Colors.BOLD}  ██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝{Colors.RESET}")
    print(f"{Colors.MAGENTA}{Colors.BOLD}  ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ {Colors.RESET}\n")
    print(f"{Colors.YELLOW}              by nixu dev{Colors.RESET}\n")
    print(f"{Colors.CYAN}╔══════════════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.CYAN}║{Colors.WHITE}  {t('login_title'):^38}  {Colors.CYAN}║{Colors.RESET}")
    print(f"{Colors.CYAN}╚══════════════════════════════════════════╝{Colors.RESET}")
    
    for attempt in range(3):
        try:
            password = getpass.getpass(f"\n{Colors.YELLOW}{t('password_prompt')}: {Colors.RESET}").strip()
        except EOFError:
            print("\nError de entrada. Saliendo...")
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

def simulate_attack(platform, username, speed, gen_name, gen_func):
    target_password, target_time = load_target_data(platform, username)
    
    attempt_count = 0
    start_time = time.time()
    last_update_time = start_time
    recent = []
    success = 0
    
    clear_screen()
    print_banner()
    print(f"\n{Colors.YELLOW}[!] {t('starting_attack')}{Colors.RESET}")
    time.sleep(1)

    try:
        while attempt_count < TOTAL_PASSWORDS_DB and success == 0:
            
            pwd = gen_func()
            attempt_count += 1
            
            elapsed_sim_time = attempt_count * (1.0 / speed)
            
            if target_password and elapsed_sim_time >= target_time and success == 0:
                pwd = target_password
                success = 1
            
            recent.append(pwd)
            if len(recent) > 10:
                recent.pop(0)

            current_time = time.time()
            elapsed = current_time - start_time
            
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
                
                # Sección de OBJETIVO
                print(f"{Colors.YELLOW}╔═════════════════════════════════════════════════════════════════╗{Colors.RESET}")
                print(f"{Colors.YELLOW}║{Colors.BOLD} {t('target'):^63} {Colors.YELLOW}║{Colors.RESET}")
                print(f"{Colors.YELLOW}╠═════════════════════════════════════════════════════════════════╣{Colors.RESET}")
                print(f"{Colors.YELLOW}║ {Colors.CYAN}{t('platform')}: {Colors.WHITE}{platform:<25} {Colors.CYAN}{t('user')}: {Colors.WHITE}{username:<25} {Colors.YELLOW}║{Colors.RESET}")
                print(f"{Colors.YELLOW}╚═════════════════════════════════════════════════════════════════╝{Colors.RESET}")
                
                # Sección de ESTADÍSTICAS EN TIEMPO REAL
                print(f"\n{Colors.BLUE}╔═══════════════════════════╦═══════════════════════════╗{Colors.RESET}")
                print(f"{Colors.BLUE}║{Colors.BOLD} {t('stats'):^25} {Colors.BLUE}║{Colors.BOLD} {t('generator'):^25} {Colors.BLUE}║{Colors.RESET}")
                print(f"{Colors.BLUE}╠═══════════════════════════╬═══════════════════════════╣{Colors.RESET}")
                print(f"{Colors.BLUE}║ {Colors.CYAN}{t('total_attempts')}: {Colors.WHITE}{format_number(attempt_count):<12} {Colors.BLUE}║ {Colors.CYAN}{t('generator')}: {Colors.WHITE}{gen_name:<18} {Colors.BLUE}║{Colors.RESET}")
                print(f"{Colors.BLUE}║ {Colors.CYAN}{t('current_speed')}: {Colors.WHITE}{int(current_speed):<12} p/s {Colors.BLUE}║ {Colors.CYAN}{t('active_time')}: {Colors.WHITE}{format_time(elapsed):<18} {Colors.BLUE}║{Colors.RESET}")
                print(f"{Colors.BLUE}║ {Colors.CYAN}{t('success_attempts')}: {Colors.GREEN}{success:<12} {Colors.BLUE}║ {Colors.CYAN}{t('remaining_time')}: {Colors.WHITE}{remaining_time_str:<18} {Colors.BLUE}║{Colors.RESET}")
                print(f"{Colors.BLUE}╚═══════════════════════════╩═══════════════════════════╝{Colors.RESET}")

                # Sección de PROGRESO y Barra
                progress_bar_length = 58
                filled_length = max(0, min(progress_bar_length, int(progress_bar_length * progress_percent // 100)))
                bar = '█' * filled_length + '-' * (progress_bar_length - filled_length)
                
                print(f"\n{Colors.MAGENTA}╔═════════════════════════════════════════════════════════════════╗{Colors.RESET}")
                print(f"{Colors.MAGENTA}║{Colors.BOLD} {t('progress'):^63} {Colors.MAGENTA}║{Colors.RESET}")
                print(f"{Colors.MAGENTA}╠═════════════════════════════════════════════════════════════════╣{Colors.RESET}")
                print(f"{Colors.MAGENTA}║ [{bar}] {Colors.BOLD}{progress_percent:.2f}% {Colors.MAGENTA}║{Colors.RESET}")
                print(f"{Colors.MAGENTA}║ {Colors.WHITE}{format_number(attempt_count)} {t('db_total')} {Colors.MAGENTA}║{Colors.RESET}")
                print(f"{Colors.MAGENTA}╚═════════════════════════════════════════════════════════════════╝{Colors.RESET}")

                # Sección de Contraseñas Recientes
                print(f"\n{Colors.RED}  {t('testing_pass')}  {Colors.RESET}")
                print(f"  {t('id_col'):<5} | {t('password_col'):<25} | {t('status_col'):<10}")
                print("  " + "-"*5 + "-+-" + "-"*25 + "-+-" + "-"*10)

                for i, p in enumerate(reversed(recent[-5:]), 1):
                    id_num = attempt_count - len(recent) + i
                    status_text = t('access_granted') if p == target_password else t('access_denied')
                    color = Colors.GREEN if p == target_password else Colors.RED
                    print(f"  {id_num:<5} | {p:<25} | {color}{status_text:<10}{Colors.RESET}")
            
            time.sleep(0.0001) 
            
        if success == 1:
             clear_screen()
             print_banner()
             print(f"\n{Colors.GREEN}╔════════════════════════════════════╗{Colors.RESET}")
             print(f"{Colors.GREEN}║  🎉 {t('pass_found'):^30}  ║{Colors.RESET}")
             print(f"{Colors.GREEN}╚════════════════════════════════════╝{Colors.RESET}\n")
             print(f"{Colors.WHITE}{t('password')}: {Colors.GREEN}{target_password}{Colors.RESET}")
             print(f"{Colors.WHITE}{t('generator')}: {Colors.WHITE}{gen_name}{Colors.RESET}")
             print(f"{Colors.WHITE}{t('attempts_made')}: {format_number(attempt_count)}{Colors.RESET}")
             print(f"{Colors.WHITE}{t('total_time')}: {format_time(elapsed)}{Colors.RESET}\n")

    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}{t('attack_stopped')}{Colors.RESET}\n")

def select_platform():
    platforms = {'1': 'Instagram', '2': 'Facebook', '3': 'X (Twitter)', '4': 'Roblox', '5': 'Gmail'}
    clear_screen()
    print_banner()
    print(f"\n{t('select_platform')}:\n")
    for k, v in platforms.items():
        print(f"  [{k}] {v}")
    print(f"  [0] {t('exit')}")
    choice = input(f"\n{Colors.YELLOW}└──> {Colors.RESET}").strip()
    if choice == '0':
        sys.exit(0)
    return platforms.get(choice, 'Instagram')

def get_username(platform):
    clear_screen()
    print_banner()
    print(f"\n{t('platform')}: {platform}\n")
    return input(f"{Colors.YELLOW}{t('target_user')}: {Colors.RESET}").strip()

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
    print(f"\n{t('select_generator')}:\n")
    for k, (name, _) in gens.items():
        print(f"  [{k}] {name}")
    choice = input(f"\n{Colors.YELLOW}└──> {Colors.RESET}").strip()
    return gens.get(choice, ('Random', PasswordGenerators.random_basic))

def select_speed():
    speeds = {
        '1': 10, '2': 50, '3': 100, '4': 500, '5': 1000,
    }
    clear_screen()
    print_banner()
    print(f"\n{t('select_speed')}:\n")
    print(f"  [1] {t('slow')} (10 pass/s)")
    print(f"  [2] {t('medium')} (50 pass/s)")
    print(f"  [3] {t('fast')} (100 pass/s)")
    print(f"  [4] {t('very_fast')} (500 pass/s)")
    print(f"  [5] {t('extreme')} (1000 pass/s)")
    choice = input(f"\n{Colors.YELLOW}└──> {Colors.RESET}").strip()
    return speeds.get(choice, 100)

def main_menu():
    while True:
        clear_screen()
        print_banner()
        print(f"\n{Colors.MAGENTA}╔═══════════════════════════════════════╗{Colors.RESET}")
        print(f"{Colors.MAGENTA}║{Colors.BOLD} {t('menu_title'):^37} {Colors.MAGENTA}║{Colors.RESET}")
        print(f"{Colors.MAGENTA}╠═══════════════════════════════════════╣{Colors.RESET}")
        print(f"{Colors.MAGENTA}║ {Colors.CYAN}[1] {t('menu_bruteforce'):<34} {Colors.MAGENTA}║{Colors.RESET}")
        print(f"{Colors.MAGENTA}║ {Colors.BLUE}[2] {t('menu_updates'):<34} {Colors.MAGENTA}║{Colors.RESET}")
        print(f"{Colors.MAGENTA}║{Colors.RESET}  {Colors.RED}[0] {t('exit'):<34} {Colors.MAGENTA}║{Colors.RESET}")
        print(f"{Colors.MAGENTA}╚═══════════════════════════════════════╝{Colors.RESET}")
        
        choice = input(f"\n{Colors.YELLOW}└──> {Colors.RESET}").strip()
        
        if choice == '1':
            return 'bruteforce'
        elif choice == '2':
            check_updates_github()
        elif choice == '0':
            print(f"\n{Colors.GREEN}{t('goodbye')}{Colors.RESET}")
            sys.exit(0)
        else:
            print(f"{Colors.RED}{t('invalid_option')}{Colors.RESET}")
            time.sleep(1)

def check_updates_github():
    """
    Simula la búsqueda de actualizaciones en GitHub usando el URL oficial.
    """
    clear_screen()
    print_banner()
    print(f"\n{Colors.YELLOW}[!] {t('update_checking')}{Colors.RESET}")
    time.sleep(1)

    # --- SIMULACIÓN DE RESULTADO ---
    # En un entorno real, aquí harías una petición real a la API de GitHub.
    # Usamos la hora actual para simular un commit reciente y hacemos que el resultado
    # parezca "Actualizado" o "Con Cambios" de forma plausible.
    
    current_time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Simulación de éxito (repositorio actualizado o commit reciente)
    print(f"\n{Colors.GREEN}{t('update_not_found')}{Colors.RESET}")
    
    print(f"\n{Colors.CYAN}╔═════════════════════════════════════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.CYAN}║ {t('update_repo'):<15} {Colors.WHITE}{REPO_URL:<48} {Colors.CYAN}║{Colors.RESET}")
    print(f"{Colors.CYAN}║ {t('update_last_commit'):<15} {Colors.WHITE}Fechas actualizadas: {current_time_str:<29} {Colors.CYAN}║{Colors.RESET}")
    print(f"{Colors.CYAN}║ {Colors.WHITE}Para ver los cambios, visita el link de arriba.                      {Colors.CYAN}║{Colors.RESET}")
    print(f"{Colors.CYAN}╚═════════════════════════════════════════════════════════════════╝{Colors.RESET}")
        
    input(f"\n{Colors.YELLOW}└──> {t('press_to_continue')}{Colors.RESET}")

def run_bruteforce_setup():
    """
    Ejecuta la secuencia completa de selección de ataque.
    """
    platform = select_platform()
    username = get_username(platform)
    gen_name, gen_func = select_generator()
    speed = select_speed()
    simulate_attack(platform, username, speed, gen_name, gen_func)

def main():
    select_language()
    if not initial_login():
        return
    
    action = main_menu() 

    if action == 'bruteforce':
        run_bruteforce_setup()
    
if __name__ == "__main__":
    main()

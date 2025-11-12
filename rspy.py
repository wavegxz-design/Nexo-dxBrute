#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import random
import string
import os
import sys
import getpass # Importado para ocultar la contraseña de acceso
from datetime import datetime

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
        'remaining_time': 'Tiempo restante',
        'success_attempts': 'Intentos exitosos',
        'failed_attempts': 'Intentos fallidos',
        'progress': 'PROGRESO DEL ATAQUE',
        'testing_pass': 'PROBANDO CONTRASEÑA',
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
        'select_speed': 'SELECCIONA LA VELOCIDAD',
        'slow': 'Lenta',
        'medium': 'Media',
        'fast': 'Rápida',
        'very_fast': 'Muy Rápida',
        'extreme': 'Extrema',
        'auto_testing': 'MODO AUTO',
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
        'remaining_time': 'Remaining time',
        'success_attempts': 'Successful',
        'failed_attempts': 'Failed',
        'progress': 'PROGRESS',
        'testing_pass': 'TESTING PASSWORD',
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
        'select_speed': 'SELECT SPEED',
        'slow': 'Slow',
        'medium': 'Medium',
        'fast': 'Fast',
        'very_fast': 'Very Fast',
        'extreme': 'Extreme',
        'auto_testing': 'AUTO MODE',
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
    """
    Mejora de Seguridad: Usa getpass para ocultar la entrada de la clave 'nexo'.
    """
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
            # Uso de getpass para la seguridad de la entrada
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
    # Generadores de patrones sin cambios
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
    """
    Mejora de Seguridad: Simula la carga de datos sensibles de un archivo externo.
    En un proyecto real, esto cargaría un archivo (ej. JSON) para evitar 
    que las claves de prueba estén visibles en el código principal.
    """
    # Estos valores ya no están en simulate_attack
    target_data = {
        ("Instagram", "kim_azg"): ("aoMO45nLpy-Ptwr", 180)
    }
    return target_data.get((platform, username.lower()), (None, None))

def format_time(s):
    if s < 60: return f"{int(s)}s"
    if s < 3600: return f"{int(s//60)}m {int(s%60)}s"
    return f"{int(s//3600)}h {int((s%3600)//60)}m"

def format_number(n):
    return f"{n:,}".replace(',', '.')

def simulate_attack(platform, username, speed, gen_name, gen_func):
    """
    Interfaz Original Restaurada: La actualización de la UI se basa en `attempt_count % speed == 0`.
    Usa la función `load_target_data` para obtener la clave de prueba.
    """
    target_password, target_time = load_target_data(platform, username)
    
    attempt_count = 0
    start_time = time.time()
    recent = []
    success = 0
    
    clear_screen()
    print_banner()
    print(f"\n{Colors.YELLOW}[!] {t('starting_attack')}{Colors.RESET}")
    time.sleep(1)
    
    try:
        while True:
            pwd = gen_func()
            attempt_count += 1
            elapsed = time.time() - start_time
            
            # Lógica de éxito sin cambios
            if target_password and elapsed >= target_time and success == 0:
                pwd = target_password
                success = 1
            
            recent.append(pwd)
            if len(recent) > 10:
                recent.pop(0)
            
            # Lógica de Interfaz Original: Actualiza la pantalla cada 'speed' intentos
            if attempt_count % speed == 0:
                clear_screen()
                print_banner()
                print(f"\n{Colors.CYAN}Platform: {Colors.WHITE}{platform} {Colors.CYAN}| User: {Colors.WHITE}{username}{Colors.RESET}")
                print(f"{Colors.GREEN}Attempts: {format_number(attempt_count)} | Speed: {int(attempt_count/elapsed if elapsed > 0 else 0)} p/s{Colors.RESET}")
                print(f"{Colors.MAGENTA}Testing: {Colors.WHITE}{pwd}{Colors.RESET}\n")
                # Muestra los últimos 5 patrones probados
                for i, p in enumerate(reversed(recent[-5:]), 1):
                    status = f"{Colors.GREEN}✓" if p == target_password else f"{Colors.RED}✗"
                    print(f"{status} {p}{Colors.RESET}")
            
            if success == 1:
                # Interfaz de Contraseña Encontrada Original
                clear_screen()
                print_banner()
                print(f"\n{Colors.GREEN}╔════════════════════════════════════╗{Colors.RESET}")
                print(f"{Colors.GREEN}║  🎉 {t('pass_found'):^30}  ║{Colors.RESET}")
                print(f"{Colors.GREEN}╚════════════════════════════════════╝{Colors.RESET}\n")
                print(f"{Colors.WHITE}Password: {Colors.GREEN}{target_password}{Colors.RESET}")
                print(f"{Colors.WHITE}Attempts: {format_number(attempt_count)}{Colors.RESET}")
                print(f"{Colors.WHITE}Time: {format_time(elapsed)}{Colors.RESET}\n")
                break
            
            time.sleep(1.0 / speed)
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
    speeds = {'1': 10, '2': 50, '3': 100, '4': 500, '5': 1000}
    clear_screen()
    print_banner()
    print(f"\n{t('select_speed')}:\n")
    for k, v in speeds.items():
        print(f"  [{k}] {v} pass/s")
    choice = input(f"\n{Colors.YELLOW}└──> {Colors.RESET}").strip()
    return speeds.get(choice, 100)

def main():
    select_language()
    if not initial_login():
        return
    platform = select_platform()
    username = get_username(platform)
    gen_name, gen_func = select_generator()
    speed = select_speed()
    simulate_attack(platform, username, speed, gen_name, gen_func)

if __name__ == "__main__":
    main()

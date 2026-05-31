#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TIGRAN CYBER COMMAND X - Professional Cyberpunk Simulation Tool
Fully simulated cybersecurity training environment
Version: 6.0.0
"""

import time
import random
import sys
import os
import threading
from datetime import datetime
from colorama import init, Fore, Back, Style

# Initialize colorama
init(autoreset=True)

# ==================== GLOBAL CONFIG ====================
VERSION = "6.0.0"
BUILD_DATE = "2024.12.01"
SCAN_DELAY = 0.008
LOADING_DELAY = 0.05
TYPING_DELAY = 0.01

# ==================== KNOWLEDGE BASE QUESTIONS ====================
HISTORY_QUESTIONS = [
    ("В каком году Армения приняла христианство?", 301),
    ("В каком году была провозглашена независимость Армении?", 1991),
    ("В каком году был основан Ереван?", 782),
    ("В каком году пала Западная Римская империя?", 476),
    ("В каком году началась Вторая мировая война?", 1939),
    ("В каком году человек высадился на Луну?", 1969),
    ("В каком году был построен Колизей?", 80),
    ("В каком году распался СССР?", 1991),
    ("В каком году началась Первая мировая война?", 1914),
    ("В каком году закончилась Холодная война?", 1991),
]

PROGRAMMING_QUESTIONS = [
    ("В каком году появился язык программирования C?", 1972),
    ("В каком году появился язык программирования Python?", 1991),
    ("В каком году появился язык программирования Java?", 1995),
    ("В каком году появился язык программирования C++?", 1985),
    ("В каком году появился язык JavaScript?", 1995),
    ("В каком году появился язык Go?", 2009),
    ("В каком году появился язык Rust?", 2010),
    ("В каком году появился язык Swift?", 2014),
    ("В каком году появился язык Kotlin?", 2011),
    ("В каком году появился язык TypeScript?", 2012),
]

TECH_QUESTIONS = [
    ("В каком году был создан первый iPhone?", 2007),
    ("В каком году был создан первый Android телефон?", 2008),
    ("В каком году появился Linux?", 1991),
    ("В каком году появился интернет (ARPANET)?", 1969),
    ("В каком году был создан первый компьютер ENIAC?", 1946),
    ("В каком году появился Windows 95?", 1995),
    ("В каком году появился первый веб-браузер?", 1990),
    ("В каком году был создан первый транзистор?", 1947),
    ("В каком году появился WiFi стандарт 802.11?", 1997),
    ("В каком году появился Bluetooth?", 1994),
]

SCIENCE_QUESTIONS = [
    ("В каком году была открыта теория относительности Эйнштейна?", 1905),
    ("В каком году была расшифрована структура ДНК?", 1953),
    ("В каком году был запущен первый спутник Земли?", 1957),
    ("В каком году был совершен первый полёт человека в космос?", 1961),
    ("В каком году было открыто деление ядра урана?", 1938),
    ("В каком году был открыт пенициллин?", 1928),
    ("В каком году был изобретён телескоп Галилея?", 1609),
    ("В каком году был изобретён микроскоп?", 1590),
    ("В каком году была открыта вакцинация?", 1796),
    ("В каком году был создан первый искусственный интеллект?", 1956),
]

MATH_QUESTIONS = [
    ("В каком году была доказана теорема Ферма?", 1995),
    ("В каком году был создан математический анализ?", 1687),
    ("В каком году была опубликована работа 'Начала' Евклида?", 300),
    ("В каком году была изобретена арабская цифровая система?", 825),
    ("В каком году был открыт ноль как число?", 628),
    ("В каком году появилась теория множеств Кантора?", 1874),
    ("В каком году была доказана неразрешимость проблемы остановки?", 1936),
    ("В каком году была создана теория игр?", 1944),
    ("В каком году появилась теория хаоса?", 1961),
    ("В каком году была создана криптография с открытым ключом?", 1976),
]

SPACE_QUESTIONS = [
    ("В каком году был запущен телескоп Хаббл?", 1990),
    ("В каком году была открыта первая экзопланета?", 1992),
    ("В каком году был запущен марсоход Curiosity?", 2011),
    ("В каком году была открыта тёмная материя?", 1933),
    ("В каком году был запущен космический корабль Восток-1?", 1961),
    ("В каком году была запущена станция Мир?", 1986),
    ("В каком году был запущен МКС?", 1998),
    ("В каком году была открыта чёрная дыра Лебедь X-1?", 1964),
    ("В каком году была открыта космическая микроволновая фоновая радиация?", 1965),
    ("В каком году был создан Плутон?", 1930),
]

ARMENIA_QUESTIONS = [
    ("В каком году был основан первый армянский алфавит Месропом Маштоцем?", 405),
    ("В каком году было Битва при Аварайре?", 451),
    ("В каком году было создано Киликийское армянское царство?", 1080),
    ("В каком году был основан Матенадаран?", 1921),
    ("В каком году была создана первая армянская республика?", 1918),
    ("В каком году было Спитакское землетрясение?", 1988),
    ("В каком году Армения вступила в ООН?", 1992),
    ("В каком году была принята Конституция Армении?", 1995),
    ("В каком году был открыт коньячный завод в Ереване?", 1887),
    ("В каком году был основан театр оперы и балета в Ереване?", 1933),
]

# Combine all questions
ALL_QUESTIONS = (HISTORY_QUESTIONS + PROGRAMMING_QUESTIONS + TECH_QUESTIONS + 
                 SCIENCE_QUESTIONS + MATH_QUESTIONS + SPACE_QUESTIONS + ARMENIA_QUESTIONS)

# ==================== CODEMASTER HACKING SYSTEM ====================
class CodeMasterHacking:
    """Advanced hacking minigame system"""
    
    def __init__(self):
        self.target_code = None
        self.attempts = 0
        self.max_attempts = 4
        self.previous_guesses = []
        self.questions_asked = []
        self.answers_received = []
        
    def generate_new_puzzle(self):
        """Generate a new random puzzle based on historical questions"""
        # Select 4 random questions from the knowledge base
        self.questions_asked = random.sample(ALL_QUESTIONS, 4)
        self.answers_received = []
        
        # The target code is derived from the answers
        digits = []
        for question, answer in self.questions_asked:
            # Take last digit of the answer year
            digits.append(answer % 10)
        
        self.target_code = digits
        self.attempts = 0
        self.previous_guesses = []
        
        return self.questions_asked
    
    def check_guess(self, guess_digits):
        """Check a 4-digit guess against the target code"""
        if len(guess_digits) != 4:
            return False
        
        self.attempts += 1
        
        # Evaluate the guess
        result = []
        target_copy = self.target_code.copy()
        guess_copy = guess_digits.copy()
        
        # First pass: check exact matches (green)
        for i in range(4):
            if guess_copy[i] == target_copy[i]:
                result.append(('✓', guess_copy[i], 'correct position'))
                target_copy[i] = None
                guess_copy[i] = None
        
        # Second pass: check correct digits in wrong position (yellow)
        for i in range(4):
            if guess_copy[i] is not None:
                for j in range(4):
                    if target_copy[j] is not None and guess_copy[i] == target_copy[j]:
                        result.append(('◉', guess_copy[i], 'wrong position'))
                        target_copy[j] = None
                        break
        
        # Remaining digits are incorrect (red)
        for i in range(4):
            if guess_copy[i] is not None:
                result.append(('✗', guess_copy[i], 'not present'))
        
        # Store guess
        self.previous_guesses.append((guess_digits, result))
        
        # Check if solved
        is_correct = all(g == t for g, t in zip(guess_digits, self.target_code))
        
        return result, is_correct
    
    def get_hint(self):
        """Provide a logical hint based on previous attempts"""
        if len(self.previous_guesses) == 0:
            return "Система ожидает первую попытку ввода..."
        
        hint = "\n"
        hint += f"{Fore.CYAN}┌─────────────────────────────────────────────────────────────┐{Fore.RESET}\n"
        hint += f"{Fore.CYAN}│{Fore.YELLOW} АНАЛИЗ ПРЕДЫДУЩИХ ПОПЫТОК{Fore.CYAN}{' ' * 47}│{Fore.RESET}\n"
        hint += f"{Fore.CYAN}├─────────────────────────────────────────────────────────────┤{Fore.RESET}\n"
        
        for idx, (guess, result) in enumerate(self.previous_guesses):
            guess_str = ''.join(str(d) for d in guess)
            hint += f"{Fore.CYAN}│{Fore.WHITE} Попытка {idx + 1}: {guess_str}{Fore.CYAN}{' ' * (40 - len(guess_str))}│{Fore.RESET}\n"
            
            # Count correct digits
            correct_pos = sum(1 for r in result if r[0] == '✓')
            correct_wrong_pos = sum(1 for r in result if r[0] == '◉')
            incorrect = sum(1 for r in result if r[0] == '✗')
            
            hint += f"{Fore.CYAN}│{Fore.GREEN}  ✓ Правильная позиция: {correct_pos}{Fore.CYAN}{' ' * 33}│{Fore.RESET}\n"
            hint += f"{Fore.CYAN}│{Fore.YELLOW}  ◉ Есть, но не здесь: {correct_wrong_pos}{Fore.CYAN}{' ' * 30}│{Fore.RESET}\n"
            hint += f"{Fore.CYAN}│{Fore.RED}  ✗ Отсутствуют: {incorrect}{Fore.CYAN}{' ' * 36}│{Fore.RESET}\n"
        
        hint += f"{Fore.CYAN}└─────────────────────────────────────────────────────────────┘{Fore.RESET}"
        return hint
    
    def get_remaining_attempts(self):
        """Get remaining attempts"""
        return self.max_attempts - self.attempts
    
    def is_failed(self):
        """Check if player failed"""
        return self.attempts >= self.max_attempts

# ==================== UTILITY FUNCTIONS ====================

def clear_screen():
    """Clear terminal screen"""
    os.system('clear' if os.name != 'nt' else 'cls')

def type_effect(text, delay=TYPING_DELAY, color=Fore.GREEN):
    """Print text with typewriter effect"""
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def slow_print(text, delay=0.005, color=Fore.WHITE):
    """Print text line by line with delay"""
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def blink_cursor():
    """Simulate blinking cursor"""
    chars = ['|', '/', '-', '\\']
    for i in range(4):
        sys.stdout.write(f'\r{Fore.GREEN}{chars[i]}')
        sys.stdout.flush()
        time.sleep(0.2)

def progress_bar(current, total, prefix='', suffix='', length=50):
    """Display progress bar"""
    percent = 100 * (current / float(total))
    filled_length = int(length * current // total)
    bar = f"{Fore.CYAN}█{Fore.RESET}" * filled_length + f"{Fore.BLACK}░{Fore.RESET}" * (length - filled_length)
    sys.stdout.write(f'\r{Fore.YELLOW}{prefix}{Fore.RESET} |{bar}| {Fore.GREEN}{percent:.0f}%{Fore.RESET} {suffix}')
    sys.stdout.flush()

def loading_animation(text, duration=1.5):
    """Display loading animation"""
    frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    start_time = time.time()
    frame_idx = 0
    while time.time() - start_time < duration:
        sys.stdout.write(f"\r{Fore.CYAN}{frames[frame_idx % len(frames)]} {text}{Fore.RESET}")
        sys.stdout.flush()
        frame_idx += 1
        time.sleep(0.08)
    sys.stdout.write(f"\r{Fore.GREEN}✓ {text}{' ' * 30}{Fore.RESET}\n")

def generate_random_id():
    """Generate random ID"""
    return f"0x{random.randint(10000000, 99999999):08X}"

def generate_random_coords():
    """Generate random coordinates"""
    lat = random.uniform(-90, 90)
    lon = random.uniform(-180, 180)
    return lat, lon

def generate_random_ip():
    """Generate random IP address"""
    return f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}"

def print_hacking_header():
    """Print hacking minigame header"""
    header = f"""
{Fore.RED}{'═'*70}
{Fore.RED}  ╔══════════════════════════════════════════════════════════════════╗
{Fore.RED}  ║{Fore.YELLOW}              CODEMASTER ACCESS TERMINAL v5.2.1{Fore.RED}                      ║
{Fore.RED}  ║{Fore.CYAN}                   Watch Dogs / GTA Style Hacking{Fore.RED}                       ║
{Fore.RED}  ╚══════════════════════════════════════════════════════════════════╝
{Fore.RED}{'═'*70}{Fore.RESET}
"""
    print(header)

# ==================== HACKING MINIGAME ====================

def hacking_minigame():
    """Main hacking minigame with knowledge questions"""
    print_hacking_header()
    
    codemaster = CodeMasterHacking()
    questions = codemaster.generate_new_puzzle()
    
    type_effect("┌─────────────────────────────────────────────────────────────────────┐", 0.001, Fore.CYAN)
    type_effect("│  СИСТЕМА КОДОВОГО ДОСТУПА АКТИВИРОВАНА                              │", 0.001, Fore.CYAN)
    type_effect("│  Агент, для взлома необходимо ответить на 4 вопроса                 │", 0.001, Fore.CYAN)
    type_effect("│  Каждый ответ формирует цифру кода доступа                          │", 0.001, Fore.CYAN)
    type_effect("└─────────────────────────────────────────────────────────────────────┘", 0.001, Fore.CYAN)
    
    print()
    time.sleep(1)
    
    # Phase 1: Knowledge questions
    collected_digits = []
    
    for idx, (question, answer) in enumerate(questions):
        print(f"\n{Fore.MAGENTA}{'─'*70}")
        type_effect(f"ВОПРОС {idx + 1}/4", 0.02, Fore.RED)
        print(f"{Fore.MAGENTA}{'─'*70}")
        
        type_effect(question, 0.02, Fore.YELLOW)
        print()
        
        # Show hint about the answer
        last_digit_hint = f"Подсказка: последняя цифра ответа будет использована в коде"
        slow_print(f"[INFO] {last_digit_hint}", 0.005, Fore.CYAN)
        
        attempts = 2
        while attempts > 0:
            try:
                user_answer = input(f"{Fore.GREEN}Ваш ответ ({attempts} попытка): {Fore.RESET}")
                user_year = int(user_answer)
                
                if user_year == answer:
                    digit = answer % 10
                    collected_digits.append(digit)
                    print(f"{Fore.GREEN}✓ ВЕРНО! Цифра кода: {digit}{Fore.RESET}")
                    break
                else:
                    attempts -= 1
                    if attempts > 0:
                        # Provide hint based on closeness
                        diff = abs(user_year - answer)
                        if diff <= 10:
                            print(f"{Fore.YELLOW}⚠ Очень близко! Разница {diff} лет{Fore.RESET}")
                        elif diff <= 50:
                            print(f"{Fore.YELLOW}⚠ Близко, но не точно. Разница {diff} лет{Fore.RESET}")
                        else:
                            print(f"{Fore.RED}✗ НЕВЕРНО! Правильный ответ: {answer}{Fore.RESET}")
                            print(f"{Fore.CYAN}💡 Историческая справка: {answer} год{Fore.RESET}")
                    else:
                        print(f"{Fore.RED}✗ ИСПОЛЬЗОВАНА ПОСЛЕДНЯЯ ПОПЫТКА!{Fore.RESET}")
                        digit = answer % 10
                        collected_digits.append(digit)
                        print(f"{Fore.YELLOW}⚠ КОД СФОРМИРОВАН АВТОМАТИЧЕСКИ: {digit}{Fore.RESET}")
                        
            except ValueError:
                print(f"{Fore.RED}✗ Введите число!{Fore.RESET}")
                attempts -= 1
            except KeyboardInterrupt:
                return False
        
        time.sleep(0.5)
    
    # Phase 2: Code breaking
    print(f"\n{Fore.MAGENTA}{'='*70}")
    type_effect("┌─────────────────────────────────────────────────────────────────────┐", 0.001, Fore.CYAN)
    type_effect("│  КОД СФОРМИРОВАН                                                  │", 0.001, Fore.CYAN)
    type_effect("│  Теперь необходимо взломать финальный код доступа                  │", 0.001, Fore.CYAN)
    type_effect("│  Используйте логику и предыдущие подсказки                         │", 0.001, Fore.CYAN)
    type_effect("└─────────────────────────────────────────────────────────────────────┘", 0.001, Fore.CYAN)
    print(f"{Fore.MAGENTA}{'='*70}{Fore.RESET}")
    
    time.sleep(1)
    
    # Show the digits collected
    print(f"\n{Fore.CYAN}[DEBUG] Собранные цифры: {collected_digits}{Fore.RESET}")
    print(f"{Fore.YELLOW}[INFO] Цифры могут быть переставлены в коде!{Fore.RESET}")
    print(f"{Fore.RED}[WARNING] Вам нужно угадать ПРАВИЛЬНУЮ ПОСЛЕДОВАТЕЛЬНОСТЬ!{Fore.RESET}")
    
    time.sleep(1)
    
    # Phase 3: Guess the code
    print(f"\n{Fore.MAGENTA}{'─'*70}")
    type_effect("НАЧАЛО ВЗЛОМА", 0.02, Fore.RED)
    print(f"{Fore.MAGENTA}{'─'*70}")
    
    print(f"\n{Fore.CYAN}Доступно попыток: {codemaster.max_attempts}{Fore.RESET}")
    print(f"{Fore.YELLOW}Формат ввода: четыре цифры (например: 1234){Fore.RESET}")
    
    # Provide initial target hint from collected digits
    print(f"\n{Fore.CYAN}[СИСТЕМНАЯ ПОДСКАЗКА]{Fore.RESET}")
    print(f"   В коде используются только эти цифры: {set(collected_digits)}")
    print(f"   Каждая цифра используется ровно один раз")
    
    while not codemaster.is_failed():
        print(f"\n{Fore.GREEN}Попыток осталось: {codemaster.get_remaining_attempts()}{Fore.RESET}")
        
        try:
            guess_input = input(f"{Fore.YELLOW}ВВЕДИТЕ КОД > {Fore.RESET}")
            
            if len(guess_input) != 4 or not guess_input.isdigit():
                print(f"{Fore.RED}✗ Неверный формат! Введите 4 цифры.{Fore.RESET}")
                continue
            
            guess = [int(d) for d in guess_input]
            result, is_correct = codemaster.check_guess(guess)
            
            # Visual feedback
            print(f"\n{Fore.CYAN}┌─────────────────────────────────────────────────────────────┐{Fore.RESET}")
            print(f"{Fore.CYAN}│{Fore.WHITE} РЕЗУЛЬТАТ АНАЛИЗА:                                  {Fore.CYAN}│{Fore.RESET}")
            print(f"{Fore.CYAN}├─────────────────────────────────────────────────────────────┤{Fore.RESET}")
            
            # Show guess with colors
            guess_line = "│  "
            for r in result:
                if r[0] == '✓':
                    guess_line += f"{Fore.GREEN}{r[1]} "
                elif r[0] == '◉':
                    guess_line += f"{Fore.YELLOW}{r[1]} "
                else:
                    guess_line += f"{Fore.RED}{r[1]} "
            guess_line += f"{Fore.CYAN}{' ' * (40 - len(guess_input))}│{Fore.RESET}"
            print(guess_line)
            
            # Show status
            correct_pos = sum(1 for r in result if r[0] == '✓')
            correct_wrong = sum(1 for r in result if r[0] == '◉')
            
            print(f"{Fore.CYAN}│{Fore.GREEN}  ✓ Правильная позиция: {correct_pos}{Fore.CYAN}{' ' * 33}│{Fore.RESET}")
            print(f"{Fore.CYAN}│{Fore.YELLOW}  ◉ Есть, но не здесь: {correct_wrong}{Fore.CYAN}{' ' * 30}│{Fore.RESET}")
            print(f"{Fore.CYAN}└─────────────────────────────────────────────────────────────┘{Fore.RESET}")
            
            if is_correct:
                print(f"\n{Fore.GREEN}{'█'*70}")
                print(f"{Fore.GREEN}█{Fore.YELLOW}{' ' * 68}{Fore.GREEN}█")
                print(f"{Fore.GREEN}█{Fore.YELLOW}  🎉 ДОСТУП РАЗРЕШЁН! КОД ВЕРНЫЙ! 🎉{Fore.GREEN}{' ' * 22}█")
                print(f"{Fore.GREEN}█{Fore.YELLOW}{' ' * 68}{Fore.GREEN}█")
                print(f"{Fore.GREEN}{'█'*70}{Fore.RESET}")
                time.sleep(1.5)
                return True
            else:
                # Show hints
                if codemaster.get_remaining_attempts() > 0:
                    print(f"\n{Fore.CYAN}Хотите получить логическую подсказку? (y/n){Fore.RESET}")
                    hint_choice = input(f"{Fore.GREEN}> {Fore.RESET}")
                    if hint_choice.lower() == 'y':
                        print(codemaster.get_hint())
        
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}[!] Взлом прерван!{Fore.RESET}")
            return False
    
    # Failed
    print(f"\n{Fore.RED}{'█'*70}")
    print(f"{Fore.RED}█{Fore.YELLOW}{' ' * 68}{Fore.RED}█")
    print(f"{Fore.RED}█{Fore.YELLOW}  ❌ ДОСТУП ЗАБЛОКИРОВАН! ПОПЫТКИ ИСЧЕРПАНЫ! ❌{Fore.RED}{' ' * 15}█")
    print(f"{Fore.RED}█{Fore.YELLOW}{' ' * 68}{Fore.RED}█")
    print(f"{Fore.RED}{'█'*70}{Fore.RESET}")
    print(f"\n{Fore.YELLOW}Правильный код был: {''.join(str(d) for d in codemaster.target_code)}{Fore.RESET}")
    time.sleep(2)
    return False

# ==================== ASCII BANNERS ====================

def print_main_banner():
    """Print main ASCII banner"""
    banner = f"""
{Fore.RED}{'█'*70}
{Fore.RED}████████╗██╗ ██████╗ ██████╗ █████╗ ███╗   ██╗{Fore.RESET}
{Fore.RED}╚══██╔══╝██║██╔════╝ ██╔══██╗██╔══██╗████╗  ██║{Fore.RESET}
{Fore.RED}   ██║   ██║██║  ███╗██████╔╝███████║██╔██╗ ██║{Fore.RESET}
{Fore.RED}   ██║   ██║██║   ██║██╔══██╗██╔══██║██║╚██╗██║{Fore.RESET}
{Fore.RED}   ██║   ██║╚██████╔╝██║  ██║██║  ██║██║ ╚████║{Fore.RESET}
{Fore.RED}   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝{Fore.RESET}
{Fore.RED}{'█'*70}
{Fore.YELLOW}████████╗██╗ ██████╗ ██████╗  █████╗ ███╗   ██╗{Fore.RESET}
{Fore.YELLOW}╚══██╔══╝██║██╔════╝ ██╔══██╗██╔══██╗████╗  ██║{Fore.RESET}
{Fore.YELLOW}   ██║   ██║██║  ███╗██████╔╝███████║██╔██╗ ██║{Fore.RESET}
{Fore.YELLOW}   ██║   ██║██║   ██║██╔══██╗██╔══██║██║╚██╗██║{Fore.RESET}
{Fore.YELLOW}   ██║   ██║╚██████╔╝██║  ██║██║  ██║██║ ╚████║{Fore.RESET}
{Fore.YELLOW}   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝{Fore.RESET}
{Fore.RED}{'█'*70}
{Fore.CYAN}{' ' * 15}TIGRAN CYBER COMMAND X{Fore.RESET}
{Fore.CYAN}{' ' * 15}Version {VERSION} | Build: {BUILD_DATE}{Fore.RESET}
{Fore.RED}{'█'*70}{Fore.RESET}
"""
    print(banner)

def print_simulation_header():
    """Print simulation header"""
    print(f"\n{Fore.MAGENTA}{'═'*70}")
    print(f"{Fore.MAGENTA}║{Fore.CYAN} SIMULATION CONTROL CENTER{Fore.MAGENTA}{' ' * 46}║")
    print(f"{Fore.MAGENTA}{'═'*70}{Fore.RESET}")

# ==================== LOADING SEQUENCES ====================

def loading_sequence():
    """Initial loading sequence"""
    print(f"\n{Fore.CYAN}[>] INITIALIZING TIGRAN CYBER COMMAND X...{Fore.RESET}")
    time.sleep(0.5)
    
    modules = [
        "AI Core Loading",
        "Neural Network Loading",
        "Quantum Engine Loading",
        "Satellite Sync",
        "Signal Mapping",
        "Threat Database Sync",
        "Cyber Defense Matrix",
        "Neural Link Calibration",
        "Quantum Entanglement Protocol",
        "Blockchain Verification Layer"
    ]
    
    for module in modules:
        loading_animation(module, random.uniform(0.8, 1.5))
        time.sleep(random.uniform(0.1, 0.3))
    
    print(f"\n{Fore.GREEN}{'='*70}")
    print(f"{Fore.GREEN}✓ ALL SYSTEMS ONLINE")
    print(f"{Fore.GREEN}✓ CYBER DEFENSE MATRIX ACTIVE")
    print(f"{Fore.GREEN}✓ QUANTUM SECURE CHANNEL ESTABLISHED")
    print(f"{Fore.GREEN}{'='*70}{Fore.RESET}")
    time.sleep(1)

# ==================== SCANNING FUNCTIONS ====================

def fake_wifi_scan():
    """Simulate WiFi scanning"""
    print(f"\n{Fore.BLUE}[>] SCANNING: WiFi Networks{Fore.RESET}")
    loading_animation("Scanning 2.4GHz and 5GHz bands", 2.0)
    
    networks = [
        f"SSID: HomeWiFi_5G - BSSID: {generate_random_id()} - CH: 36 - RSSI: -54dBm - ENC: WPA3",
        f"SSID: Guest_Network - BSSID: {generate_random_id()} - CH: 6 - RSSI: -67dBm - ENC: WPA2",
        f"SSID: IoT_Hub - BSSID: {generate_random_id()} - CH: 1 - RSSI: -42dBm - ENC: WPA2",
        f"SSID: Hidden_SSID - BSSID: {generate_random_id()} - CH: 11 - RSSI: -78dBm - ENC: Unknown",
        f"SSID: Drone_Link - BSSID: {generate_random_id()} - CH: 149 - RSSI: -63dBm - ENC: WPA3-Enterprise"
    ]
    
    for net in networks:
        slow_print(f"    {net}", 0.003, Fore.GREEN)
        time.sleep(random.uniform(0.1, 0.2))
    
    print(f"{Fore.GREEN}✓ Found {len(networks)} WiFi networks{Fore.RESET}")

def fake_bluetooth_scan():
    """Simulate Bluetooth scanning"""
    print(f"\n{Fore.BLUE}[>] SCANNING: Bluetooth Devices{Fore.RESET}")
    loading_animation("Probing Bluetooth Low Energy devices", 1.8)
    
    bt_devices = [
        f"Device: AirPods Pro - MAC: {generate_random_id()} - RSSI: -62dBm - Class: Audio",
        f"Device: Samsung Galaxy S23 - MAC: {generate_random_id()} - RSSI: -55dBm - Class: Phone",
        f"Device: ESP32_Device - MAC: {generate_random_id()} - RSSI: -48dBm - Class: IoT",
        f"Device: Keyboard K380 - MAC: {generate_random_id()} - RSSI: -71dBm - Class: HID",
        f"Device: Smart Watch - MAC: {generate_random_id()} - RSSI: -59dBm - Class: Wearable"
    ]
    
    for device in bt_devices:
        slow_print(f"    {device}", 0.003, Fore.CYAN)
        time.sleep(random.uniform(0.1, 0.2))
    
    print(f"{Fore.GREEN}✓ Found {len(bt_devices)} Bluetooth devices{Fore.RESET}")

def fake_cellular_scan():
    """Simulate cellular network scanning"""
    print(f"\n{Fore.BLUE}[>] SCANNING: Cellular Networks{Fore.RESET}")
    loading_animation("Analyzing cellular frequencies", 2.2)
    
    networks = [
        f"MCC: 250 - MNC: 01 - Operator: MTS - Band: B3 (1800MHz) - Signal: -72dBm",
        f"MCC: 250 - MNC: 02 - Operator: Beeline - Band: B7 (2600MHz) - Signal: -85dBm",
        f"MCC: 250 - MNC: 99 - Operator: Tele2 - Band: B20 (800MHz) - Signal: -68dBm",
        f"MCC: 250 - MNC: 20 - Operator: Megafon - Band: B1 (2100MHz) - Signal: -91dBm",
        f"MCC: 250 - MNC: 50 - Operator: Yota - Band: B38 (2600MHz) - Signal: -77dBm"
    ]
    
    for net in networks:
        slow_print(f"    {net}", 0.003, Fore.YELLOW)
        time.sleep(random.uniform(0.1, 0.25))
    
    print(f"{Fore.GREEN}✓ Cell tower triangulation complete{Fore.RESET}")

def fake_gps_mapping():
    """Simulate GPS mapping"""
    print(f"\n{Fore.BLUE}[>] SCANNING: GPS Coordinates{Fore.RESET}")
    loading_animation("Acquiring satellite lock", 2.5)
    
    lat, lon = generate_random_coords()
    satellites = random.randint(8, 24)
    
    slow_print(f"    Latitude: {lat:.6f}°", 0.003, Fore.CYAN)
    slow_print(f"    Longitude: {lon:.6f}°", 0.003, Fore.CYAN)
    slow_print(f"    Altitude: {random.randint(50, 500)}m", 0.003, Fore.CYAN)
    slow_print(f"    Satellites: {satellites}", 0.003, Fore.CYAN)
    slow_print(f"    Accuracy: ±{random.uniform(2.0, 5.0):.1f}m", 0.003, Fore.CYAN)
    
    print(f"{Fore.GREEN}✓ GPS position acquired{Fore.RESET}")

def fake_rf_spectrum_analysis():
    """Simulate RF spectrum analysis"""
    print(f"\n{Fore.BLUE}[>] SCANNING: RF Spectrum{Fore.RESET}")
    loading_animation("Analyzing radio frequency spectrum", 2.3)
    
    frequencies = [
        f"433 MHz - Signal: {random.randint(-90, -40)}dBm - Activity: ISM Band - Interference: LOW",
        f"868 MHz - Signal: {random.randint(-95, -50)}dBm - Activity: LoRaWAN - Interference: MEDIUM",
        f"915 MHz - Signal: {random.randint(-100, -45)}dBm - Activity: ZigBee - Interference: HIGH",
        f"2.4 GHz - Signal: {random.randint(-80, -35)}dBm - Activity: WiFi/BT - Interference: CRITICAL",
        f"5.8 GHz - Signal: {random.randint(-85, -40)}dBm - Activity: WiFi/Drone - Interference: HIGH"
    ]
    
    for freq in frequencies:
        slow_print(f"    {freq}", 0.003, Fore.MAGENTA)
        time.sleep(random.uniform(0.1, 0.2))
    
    print(f"{Fore.GREEN}✓ RF spectrum analysis complete{Fore.RESET}")

def fake_drone_detection():
    """Simulate drone detection"""
    print(f"\n{Fore.BLUE}[>] SCANNING: Drone Detection{Fore.RESET}")
    loading_animation("Monitoring for UAV activity", 2.0)
    
    drones = [
        f"UAV: DJI Mavic 3 - ID: {generate_random_id()} - Alt: 120m - Speed: 45km/h - Dir: NE",
        f"UAV: Unknown - ID: {generate_random_id()} - Alt: 80m - Speed: 60km/h - Dir: SW"
    ]
    
    for drone in drones:
        slow_print(f"    {drone}", 0.003, Fore.RED)
        time.sleep(random.uniform(0.2, 0.3))
    
    print(f"{Fore.YELLOW}⚠ {len(drones)} drones detected in area{Fore.RESET}")

def fake_esp32_detection():
    """Simulate ESP32 device detection"""
    print(f"\n{Fore.BLUE}[>] SCANNING: IoT Devices (ESP32){Fore.RESET}")
    loading_animation("Searching for ESP32 modules", 2.1)
    
    esp_devices = [
        f"ESP32 - MAC: {generate_random_id()} - Signal: -48dBm - Distance: 273m - Status: ACTIVE",
        f"ESP8266 - MAC: {generate_random_id()} - Signal: -55dBm - Distance: 150m - Status: SLEEP",
        f"ESP32-C3 - MAC: {generate_random_id()} - Signal: -62dBm - Distance: 320m - Status: ACTIVE"
    ]
    
    for device in esp_devices:
        slow_print(f"    {device}", 0.003, Fore.RED)
        time.sleep(random.uniform(0.1, 0.2))
    
    print(f"{Fore.YELLOW}⚠ {len(esp_devices)} ESP32 devices detected{Fore.RESET}")

def fake_smart_device_mapping():
    """Simulate smart device mapping"""
    print(f"\n{Fore.BLUE}[>] SCANNING: Smart Devices{Fore.RESET}")
    loading_animation("Mapping smart home devices", 2.0)
    
    devices = [
        f"Smart TV - IP: {generate_random_ip()} - MAC: {generate_random_id()} - Type: Samsung",
        f"Smart Speaker - IP: {generate_random_ip()} - MAC: {generate_random_id()} - Type: Google Home",
        f"Smart Bulb - IP: {generate_random_ip()} - MAC: {generate_random_id()} - Type: Philips Hue",
        f"Smart Plug - IP: {generate_random_ip()} - MAC: {generate_random_id()} - Type: TP-Link Kasa",
        f"Security Camera - IP: {generate_random_ip()} - MAC: {generate_random_id()} - Type: Xiaomi"
    ]
    
    for device in devices:
        slow_print(f"    {device}", 0.003, Fore.CYAN)
        time.sleep(random.uniform(0.1, 0.2))
    
    print(f"{Fore.GREEN}✓ {len(devices)} smart devices mapped{Fore.RESET}")

def fake_camera_detection():
    """Simulate camera detection"""
    print(f"\n{Fore.BLUE}[>] SCANNING: Camera Devices{Fore.RESET}")
    loading_animation("Detecting optical sensors", 1.9)
    
    cameras = [
        f"Camera: IP Camera - IP: {generate_random_ip()} - MAC: {generate_random_id()} - FOV: 120°",
        f"Camera: Webcam - USB - VID: {generate_random_id()} - PID: {generate_random_id()} - Status: ACTIVE"
    ]
    
    for camera in cameras:
        slow_print(f"    {camera}", 0.003, Fore.YELLOW)
        time.sleep(random.uniform(0.15, 0.25))
    
    print(f"{Fore.GREEN}✓ {len(cameras)} camera devices detected{Fore.RESET}")

def fake_sensor_detection():
    """Simulate sensor detection"""
    print(f"\n{Fore.BLUE}[>] SCANNING: Environmental Sensors{Fore.RESET}")
    loading_animation("Detecting IoT sensors", 2.0)
    
    sensors = [
        f"Sensor: Temperature - Value: {random.uniform(-10, 40):.1f}°C - Accuracy: ±0.5°C",
        f"Sensor: Humidity - Value: {random.uniform(20, 90):.0f}% - Accuracy: ±3%",
        f"Sensor: Motion - Status: {random.choice(['IDLE', 'ACTIVE', 'SLEEP'])} - Sensitivity: HIGH",
        f"Sensor: Door - Status: {random.choice(['CLOSED', 'OPEN'])} - Battery: {random.randint(20, 100)}%"
    ]
    
    for sensor in sensors:
        slow_print(f"    {sensor}", 0.003, Fore.MAGENTA)
        time.sleep(random.uniform(0.1, 0.2))
    
    print(f"{Fore.GREEN}✓ Sensor analysis complete{Fore.RESET}")

# ==================== DETECTION RESULTS ====================

def fake_detection_results():
    """Display fake detection results"""
    print(f"\n{Fore.RED}{'='*70}")
    type_effect("[!] WARNING: SUSPICIOUS SIGNALS DETECTED", 0.02, Fore.RED)
    print(f"{Fore.RED}{'='*70}{Fore.RESET}")
    
    threats = [
        ("ESP32 Wireless Module", "CRITICAL", Fore.RED),
        ("Unknown IoT Device", "HIGH", Fore.RED),
        ("Anonymous Signal", "MEDIUM", Fore.YELLOW),
        ("Smart Relay Active", "MEDIUM", Fore.YELLOW),
        ("RF Beacon Detected", "LOW", Fore.GREEN)
    ]
    
    for threat, level, color in threats:
        slow_print(f"    • {threat:<30} Threat Level: {level}", 0.008, color)
        time.sleep(random.uniform(0.1, 0.3))
    
    print(f"{Fore.RED}{'='*70}{Fore.RESET}")
    time.sleep(1)

# ==================== SIMULATION GAME MODES ====================

def select_location():
    """Location selection menu"""
    print_simulation_header()
    print(f"""
{Fore.CYAN}[1]{Fore.WHITE} Локальный объект (Local Building)
{Fore.CYAN}[2]{Fore.WHITE} Квартира (Apartment)
{Fore.CYAN}[3]{Fore.WHITE} Частный дом (Private House)
{Fore.CYAN}[4]{Fore.WHITE} Улица (Street)
{Fore.CYAN}[5]{Fore.WHITE} Район (District)
{Fore.CYAN}[6]{Fore.WHITE} Город (City)
{Fore.CYAN}[7]{Fore.WHITE} Спутниковая зона (Satellite Zone)
{Fore.CYAN}[0]{Fore.WHITE} Выход (Exit)
{Fore.RESET}
""")
    
    while True:
        try:
            choice = input(f"{Fore.GREEN}Выберите локацию (1-7): {Fore.RESET}")
            if choice == '0':
                return None
            if choice in ['1', '2', '3', '4', '5', '6', '7']:
                return int(choice)
            print(f"{Fore.RED}Неверный выбор!{Fore.RESET}")
        except KeyboardInterrupt:
            return None

def select_difficulty():
    """Difficulty selection menu"""
    print(f"""
{Fore.MAGENTA}{'─'*70}
{Fore.CYAN}ВЫБЕРИТЕ УРОВЕНЬ СИМУЛЯЦИИ
{Fore.MAGENTA}{'─'*70}
{Fore.GREEN}[1]{Fore.WHITE} Низкий (Low)
{Fore.GREEN}[2]{Fore.WHITE} Средний (Medium)
{Fore.GREEN}[3]{Fore.WHITE} Высокий (High)
{Fore.GREEN}[4]{Fore.WHITE} Экстремальный (Extreme)
{Fore.GREEN}[5]{Fore.WHITE} Невозможный (Impossible)
{Fore.RESET}
""")
    
    while True:
        try:
            choice = input(f"{Fore.GREEN}Выберите уровень (1-5): {Fore.RESET}")
            if choice in ['1', '2', '3', '4', '5']:
                return int(choice)
            print(f"{Fore.RED}Неверный выбор!{Fore.RESET}")
        except KeyboardInterrupt:
            return None

# ==================== SIMULATION PROCESSES ====================

def run_simulation_processes(difficulty):
    """Run simulated cyber processes"""
    processes = [
        "AI Calculation",
        "Signal Override Simulation",
        "Defense Bypass Simulation",
        "Firewall Challenge",
        "Access Puzzle",
        "Quantum Key Puzzle",
        "Neural Lock Puzzle",
        "Cipher Puzzle",
        "Matrix Puzzle",
        "Hash Cracking Simulation",
        "Brute Force Mitigation",
        "Intrusion Detection Analysis"
    ]
    
    for process in processes:
        print(f"\n{Fore.CYAN}[>] {process}...{Fore.RESET}")
        loading_animation("Processing", random.uniform(0.8, 1.5))
        
        # Show random tech messages
        messages = [
            f"[DEBUG] Processing ID: {generate_random_id()}",
            f"[INFO] Thread: {random.randint(1, 128)}",
            f"[NET] Packet sequence: {random.randint(1000, 9999)}",
            f"[CRYPTO] Key derivation completed",
            f"[SEC] Firewall rule applied"
        ]
        slow_print(f"    {random.choice(messages)}", 0.003, Fore.CYAN)
        time.sleep(random.uniform(0.1, 0.3))
    
    return True

# ==================== FINAL REPORT ====================

def print_final_report():
    """Display final simulation report"""
    print(f"\n{Fore.GREEN}{'█'*70}")
    print(f"{Fore.GREEN}{'█'*10}{Fore.YELLOW} TIGRAN CYBER COMMAND X - SIMULATION COMPLETE {Fore.GREEN}{'█'*10}")
    print(f"{Fore.GREEN}{'█'*70}{Fore.RESET}")
    
    reports = [
        ("System Integrity:", "100%", Fore.GREEN),
        ("Security Level:", "SECURE", Fore.GREEN),
        ("Threat Level:", "NONE", Fore.GREEN),
        ("Simulation Score:", f"{random.randint(85, 100)}/100", Fore.GREEN),
        ("Response Time:", f"{random.randint(2, 15)}ms", Fore.CYAN),
        ("Encryption Status:", "AES-256-GCM", Fore.CYAN),
        ("Quantum Safe:", "ENABLED", Fore.GREEN)
    ]
    
    for label, value, color in reports:
        slow_print(f"    {label:<20} {value}", 0.005, color)
        time.sleep(0.08)
    
    print(f"{Fore.GREEN}{'█'*70}{Fore.RESET}")

def print_thank_you():
    """Print thank you message"""
    print(f"\n{Fore.MAGENTA}{'─'*70}")
    print(f"{Fore.CYAN}Спасибо за использование TIGRAN CYBER COMMAND X!")
    print(f"{Fore.CYAN}Тренировочная симуляция завершена.")
    print(f"{Fore.MAGENTA}{'─'*70}{Fore.RESET}")
    print(f"\n{Fore.YELLOW}Дата: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Fore.RESET}")
    print(f"{Fore.YELLOW}ID сессии: {generate_random_id()}{Fore.RESET}")

# ==================== MAIN MENU ====================

def main():
    """Main function"""
    try:
        clear_screen()
        print_main_banner()
        time.sleep(1.5)
        
        # HACKING MINIGAME FIRST - MUST PASS TO CONTINUE
        print(f"\n{Fore.RED}{'='*70}")
        type_effect("[!] ТРЕБУЕТСЯ АВТОРИЗАЦИЯ ДОСТУПА [!]", 0.02, Fore.RED)
        print(f"{Fore.RED}{'='*70}{Fore.RESET}")
        time.sleep(1)
        
        hacking_success = hacking_minigame()
        
        if not hacking_success:
            print(f"\n{Fore.RED}[!] АВТОРИЗАЦИЯ НЕ ПРОЙДЕНА! ДОСТУП ЗАПРЕЩЁН!{Fore.RESET}")
            print(f"{Fore.YELLOW}Программа будет закрыта...{Fore.RESET}")
            time.sleep(3)
            return
        
        print(f"\n{Fore.GREEN}✓ АВТОРИЗАЦИЯ ПРОЙДЕНА! ДОБРО ПОЖАЛОВАТЬ, ОПЕРАТОР!{Fore.RESET}")
        time.sleep(1.5)
        
        loading_sequence()
        time.sleep(0.5)
        
        # Scanning phase
        print(f"\n{Fore.RED}{'='*70}")
        type_effect("[>] INITIATING SURVEILLANCE SCAN", 0.02, Fore.RED)
        print(f"{Fore.RED}{'='*70}{Fore.RESET}")
        
        fake_wifi_scan()
        fake_bluetooth_scan()
        fake_cellular_scan()
        fake_gps_mapping()
        fake_rf_spectrum_analysis()
        fake_drone_detection()
        fake_esp32_detection()
        fake_smart_device_mapping()
        fake_camera_detection()
        fake_sensor_detection()
        
        fake_detection_results()
        time.sleep(1)
        
        # Simulation game
        while True:
            location = select_location()
            if location is None:
                print(f"{Fore.YELLOW}Выход из программы...{Fore.RESET}")
                break
            
            difficulty = select_difficulty()
            if difficulty is None:
                break
            
            clear_screen()
            print_main_banner()
            print_simulation_header()
            
            locations = {
                1: "Локальный объект",
                2: "Квартира",
                3: "Частный дом",
                4: "Улица",
                5: "Район",
                6: "Город",
                7: "Спутниковая зона"
            }
            
            difficulties = {1: "Низкий", 2: "Средний", 3: "Высокий", 4: "Экстремальный", 5: "Невозможный"}
            
            print(f"\n{Fore.GREEN}Локация: {locations[location]}")
            print(f"Уровень сложности: {difficulties[difficulty]}{Fore.RESET}")
            print(f"{Fore.MAGENTA}{'─'*70}{Fore.RESET}")
            time.sleep(1)
            
            # Progress bar for simulation
            print(f"\n{Fore.CYAN}[>] ЗАГРУЗКА СИМУЛЯЦИИ...{Fore.RESET}")
            for i in range(101):
                progress_bar(i, 100, prefix='Загрузка:', suffix='Готово')
                time.sleep(0.02)
            print()
            
            # Run simulation
            success = run_simulation_processes(difficulty)
            
            print_final_report()
            print_thank_you()
            
            print(f"\n{Fore.CYAN}Нажмите Enter для продолжения или Ctrl+C для выхода...{Fore.RESET}")
            try:
                input()
            except KeyboardInterrupt:
                break
            
            clear_screen()
            print_main_banner()
    
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}\n[!] Программа прервана пользователем.{Fore.RESET}")
    finally:
        print(f"\n{Fore.YELLOW}Завершение работы TIGRAN CYBER COMMAND X...{Fore.RESET}")
        time.sleep(1)

if __name__ == "__main__":
    main()

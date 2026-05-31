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
    ("In what year did Armenia adopt Christianity?", 301),
    ("In what year was Armenia's independence declared?", 1991),
    ("In what year was Yerevan founded?", 782),
    ("In what year did the Western Roman Empire fall?", 476),
    ("In what year did World War II begin?", 1939),
    ("In what year did humans land on the Moon?", 1969),
    ("In what year was the Colosseum built?", 80),
    ("In what year did the USSR collapse?", 1991),
    ("In what year did World War I begin?", 1914),
    ("In what year did the Cold War end?", 1991),
]

PROGRAMMING_QUESTIONS = [
    ("In what year was the C programming language created?", 1972),
    ("In what year was Python created?", 1991),
    ("In what year was Java created?", 1995),
    ("In what year was C++ created?", 1985),
    ("In what year was JavaScript created?", 1995),
    ("In what year was Go created?", 2009),
    ("In what year was Rust created?", 2010),
    ("In what year was Swift created?", 2014),
    ("In what year was Kotlin created?", 2011),
    ("In what year was TypeScript created?", 2012),
]

TECH_QUESTIONS = [
    ("In what year was the first iPhone released?", 2007),
    ("In what year was the first Android phone released?", 2008),
    ("In what year was Linux created?", 1991),
    ("In what year was the internet (ARPANET) created?", 1969),
    ("In what year was the first computer ENIAC built?", 1946),
    ("In what year was Windows 95 released?", 1995),
    ("In what year was the first web browser created?", 1990),
    ("In what year was the first transistor invented?", 1947),
    ("In what year was WiFi 802.11 standard introduced?", 1997),
    ("In what year was Bluetooth introduced?", 1994),
]

SCIENCE_QUESTIONS = [
    ("In what year was Einstein's theory of relativity published?", 1905),
    ("In what year was the structure of DNA discovered?", 1953),
    ("In what year was the first Earth satellite launched?", 1957),
    ("In what year was the first human space flight?", 1961),
    ("In what year was uranium nuclear fission discovered?", 1938),
    ("In what year was penicillin discovered?", 1928),
    ("In what year was Galileo's telescope invented?", 1609),
    ("In what year was the microscope invented?", 1590),
    ("In what year was vaccination discovered?", 1796),
    ("In what year was the first artificial intelligence created?", 1956),
]

MATH_QUESTIONS = [
    ("In what year was Fermat's Last Theorem proven?", 1995),
    ("In what year was mathematical analysis created?", 1687),
    ("In what year was Euclid's 'Elements' published?", 300),
    ("In what year was the Arabic numeral system invented?", 825),
    ("In what year was zero discovered as a number?", 628),
    ("In what year was Cantor's set theory introduced?", 1874),
    ("In what year was the halting problem proven undecidable?", 1936),
    ("In what year was game theory created?", 1944),
    ("In what year was chaos theory introduced?", 1961),
    ("In what year was public key cryptography invented?", 1976),
]

SPACE_QUESTIONS = [
    ("In what year was the Hubble telescope launched?", 1990),
    ("In what year was the first exoplanet discovered?", 1992),
    ("In what year was the Curiosity rover launched?", 2011),
    ("In what year was dark matter discovered?", 1933),
    ("In what year was Vostok-1 launched?", 1961),
    ("In what year was the Mir space station launched?", 1986),
    ("In what year was the ISS launched?", 1998),
    ("In what year was the black hole Cygnus X-1 discovered?", 1964),
    ("In what year was cosmic microwave background radiation discovered?", 1965),
    ("In what year was Pluto discovered?", 1930),
]

ARMENIA_QUESTIONS = [
    ("In what year was the Armenian alphabet created by Mesrop Mashtots?", 405),
    ("In what year was the Battle of Avarayr?", 451),
    ("In what year was the Armenian Kingdom of Cilicia founded?", 1080),
    ("In what year was Matenadaran founded?", 1921),
    ("In what year was the First Republic of Armenia established?", 1918),
    ("In what year was the Spitak earthquake?", 1988),
    ("In what year did Armenia join the UN?", 1992),
    ("In what year was the Constitution of Armenia adopted?", 1995),
    ("In what year was the Yerevan Brandy Company founded?", 1887),
    ("In what year was the Yerevan Opera Theatre founded?", 1933),
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
        self.questions_asked = random.sample(ALL_QUESTIONS, 4)
        self.answers_received = []
        
        digits = []
        for question, answer in self.questions_asked:
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
        
        result = []
        target_copy = self.target_code.copy()
        guess_copy = guess_digits.copy()
        
        # First pass: check exact matches
        for i in range(4):
            if guess_copy[i] == target_copy[i]:
                result.append(('✓', guess_copy[i], 'correct position'))
                target_copy[i] = None
                guess_copy[i] = None
        
        # Second pass: check correct digits in wrong position
        for i in range(4):
            if guess_copy[i] is not None:
                for j in range(4):
                    if target_copy[j] is not None and guess_copy[i] == target_copy[j]:
                        result.append(('◉', guess_copy[i], 'wrong position'))
                        target_copy[j] = None
                        break
        
        # Remaining digits are incorrect
        for i in range(4):
            if guess_copy[i] is not None:
                result.append(('✗', guess_copy[i], 'not present'))
        
        self.previous_guesses.append((guess_digits, result))
        
        is_correct = all(g == t for g, t in zip(guess_digits, self.target_code))
        
        return result, is_correct
    
    def get_hint(self):
        """Provide a logical hint based on previous attempts"""
        if len(self.previous_guesses) == 0:
            return "System waiting for first input..."
        
        hint = "\n"
        hint += f"{Fore.CYAN}┌─────────────────────────────────────────────────────────────┐{Fore.RESET}\n"
        hint += f"{Fore.CYAN}│{Fore.YELLOW} PREVIOUS ATTEMPTS ANALYSIS{Fore.CYAN}{' ' * 45}│{Fore.RESET}\n"
        hint += f"{Fore.CYAN}├─────────────────────────────────────────────────────────────┤{Fore.RESET}\n"
        
        for idx, (guess, result) in enumerate(self.previous_guesses):
            guess_str = ''.join(str(d) for d in guess)
            hint += f"{Fore.CYAN}│{Fore.WHITE} Attempt {idx + 1}: {guess_str}{Fore.CYAN}{' ' * (40 - len(guess_str))}│{Fore.RESET}\n"
            
            correct_pos = sum(1 for r in result if r[0] == '✓')
            correct_wrong_pos = sum(1 for r in result if r[0] == '◉')
            incorrect = sum(1 for r in result if r[0] == '✗')
            
            hint += f"{Fore.CYAN}│{Fore.GREEN}  ✓ Correct position: {correct_pos}{Fore.CYAN}{' ' * 37}│{Fore.RESET}\n"
            hint += f"{Fore.CYAN}│{Fore.YELLOW}  ◉ Wrong position: {correct_wrong_pos}{Fore.CYAN}{' ' * 35}│{Fore.RESET}\n"
            hint += f"{Fore.CYAN}│{Fore.RED}  ✗ Not present: {incorrect}{Fore.CYAN}{' ' * 38}│{Fore.RESET}\n"
        
        hint += f"{Fore.CYAN}└─────────────────────────────────────────────────────────────┘{Fore.RESET}"
        return hint
    
    def get_remaining_attempts(self):
        return self.max_attempts - self.attempts
    
    def is_failed(self):
        return self.attempts >= self.max_attempts

# ==================== UTILITY FUNCTIONS ====================

def clear_screen():
    os.system('clear' if os.name != 'nt' else 'cls')

def type_effect(text, delay=TYPING_DELAY, color=Fore.GREEN):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def slow_print(text, delay=0.005, color=Fore.WHITE):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def progress_bar(current, total, prefix='', suffix='', length=50):
    percent = 100 * (current / float(total))
    filled_length = int(length * current // total)
    bar = f"{Fore.CYAN}█{Fore.RESET}" * filled_length + f"{Fore.BLACK}░{Fore.RESET}" * (length - filled_length)
    sys.stdout.write(f'\r{Fore.YELLOW}{prefix}{Fore.RESET} |{bar}| {Fore.GREEN}{percent:.0f}%{Fore.RESET} {suffix}')
    sys.stdout.flush()

def loading_animation(text, duration=1.5):
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
    return f"0x{random.randint(10000000, 99999999):08X}"

def generate_random_coords():
    lat = random.uniform(-90, 90)
    lon = random.uniform(-180, 180)
    return lat, lon

def generate_random_ip():
    return f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}"

def print_hacking_header():
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
    type_effect("│              CODE ACCESS SYSTEM ACTIVATED                           │", 0.001, Fore.CYAN)
    type_effect("│  Agent, you must answer 4 questions to hack the system             │", 0.001, Fore.CYAN)
    type_effect("│  Each answer generates a digit of the access code                  │", 0.001, Fore.CYAN)
    type_effect("└─────────────────────────────────────────────────────────────────────┘", 0.001, Fore.CYAN)
    
    print()
    time.sleep(1)
    
    collected_digits = []
    
    for idx, (question, answer) in enumerate(questions):
        print(f"\n{Fore.MAGENTA}{'─'*70}")
        type_effect(f"QUESTION {idx + 1}/4", 0.02, Fore.RED)
        print(f"{Fore.MAGENTA}{'─'*70}")
        
        type_effect(question, 0.02, Fore.YELLOW)
        print()
        
        last_digit_hint = "Hint: The last digit of the answer will be used in the code"
        slow_print(f"[INFO] {last_digit_hint}", 0.005, Fore.CYAN)
        
        attempts = 2
        while attempts > 0:
            try:
                user_answer = input(f"{Fore.GREEN}Your answer ({attempts} attempts left): {Fore.RESET}")
                user_year = int(user_answer)
                
                if user_year == answer:
                    digit = answer % 10
                    collected_digits.append(digit)
                    print(f"{Fore.GREEN}✓ CORRECT! Code digit: {digit}{Fore.RESET}")
                    break
                else:
                    attempts -= 1
                    if attempts > 0:
                        diff = abs(user_year - answer)
                        if diff <= 10:
                            print(f"{Fore.YELLOW}⚠ Very close! Difference: {diff} years{Fore.RESET}")
                        elif diff <= 50:
                            print(f"{Fore.YELLOW}⚠ Close but not exact. Difference: {diff} years{Fore.RESET}")
                        else:
                            print(f"{Fore.RED}✗ INCORRECT! Correct answer: {answer}{Fore.RESET}")
                            print(f"{Fore.CYAN}💡 Historical fact: The answer is {answer}{Fore.RESET}")
                    else:
                        print(f"{Fore.RED}✗ LAST ATTEMPT USED!{Fore.RESET}")
                        digit = answer % 10
                        collected_digits.append(digit)
                        print(f"{Fore.YELLOW}⚠ Code generated automatically: {digit}{Fore.RESET}")
                        
            except ValueError:
                print(f"{Fore.RED}✗ Please enter a number!{Fore.RESET}")
                attempts -= 1
            except KeyboardInterrupt:
                return False
        
        time.sleep(0.5)
    
    print(f"\n{Fore.MAGENTA}{'='*70}")
    type_effect("┌─────────────────────────────────────────────────────────────────────┐", 0.001, Fore.CYAN)
    type_effect("│                    CODE GENERATED                                   │", 0.001, Fore.CYAN)
    type_effect("│          Now you must crack the final access code                  │", 0.001, Fore.CYAN)
    type_effect("│          Use logic and previous hints                              │", 0.001, Fore.CYAN)
    type_effect("└─────────────────────────────────────────────────────────────────────┘", 0.001, Fore.CYAN)
    print(f"{Fore.MAGENTA}{'='*70}{Fore.RESET}")
    
    time.sleep(1)
    
    print(f"\n{Fore.CYAN}[DEBUG] Collected digits: {collected_digits}{Fore.RESET}")
    print(f"{Fore.YELLOW}[INFO] Digits may be rearranged in the code!{Fore.RESET}")
    print(f"{Fore.RED}[WARNING] You need to guess the CORRECT SEQUENCE!{Fore.RESET}")
    
    time.sleep(1)
    
    print(f"\n{Fore.MAGENTA}{'─'*70}")
    type_effect("HACK INITIATED", 0.02, Fore.RED)
    print(f"{Fore.MAGENTA}{'─'*70}")
    
    print(f"\n{Fore.CYAN}Attempts available: {codemaster.max_attempts}{Fore.RESET}")
    print(f"{Fore.YELLOW}Input format: four digits (e.g., 1234){Fore.RESET}")
    
    print(f"\n{Fore.CYAN}[SYSTEM HINT]{Fore.RESET}")
    print(f"   Only these digits are used in the code: {set(collected_digits)}")
    print(f"   Each digit is used exactly once")
    
    while not codemaster.is_failed():
        print(f"\n{Fore.GREEN}Attempts remaining: {codemaster.get_remaining_attempts()}{Fore.RESET}")
        
        try:
            guess_input = input(f"{Fore.YELLOW}ENTER CODE > {Fore.RESET}")
            
            if len(guess_input) != 4 or not guess_input.isdigit():
                print(f"{Fore.RED}✗ Invalid format! Enter 4 digits.{Fore.RESET}")
                continue
            
            guess = [int(d) for d in guess_input]
            result, is_correct = codemaster.check_guess(guess)
            
            print(f"\n{Fore.CYAN}┌─────────────────────────────────────────────────────────────┐{Fore.RESET}")
            print(f"{Fore.CYAN}│{Fore.WHITE} ANALYSIS RESULT:                                       {Fore.CYAN}│{Fore.RESET}")
            print(f"{Fore.CYAN}├─────────────────────────────────────────────────────────────┤{Fore.RESET}")
            
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
            
            correct_pos = sum(1 for r in result if r[0] == '✓')
            correct_wrong = sum(1 for r in result if r[0] == '◉')
            
            print(f"{Fore.CYAN}│{Fore.GREEN}  ✓ Correct position: {correct_pos}{Fore.CYAN}{' ' * 37}│{Fore.RESET}")
            print(f"{Fore.CYAN}│{Fore.YELLOW}  ◉ Wrong position: {correct_wrong}{Fore.CYAN}{' ' * 37}│{Fore.RESET}")
            print(f"{Fore.CYAN}└─────────────────────────────────────────────────────────────┘{Fore.RESET}")
            
            if is_correct:
                print(f"\n{Fore.GREEN}{'█'*70}")
                print(f"{Fore.GREEN}█{Fore.YELLOW}{' ' * 68}{Fore.GREEN}█")
                print(f"{Fore.GREEN}█{Fore.YELLOW}  🎉 ACCESS GRANTED! CODE IS CORRECT! 🎉{Fore.GREEN}{' ' * 22}█")
                print(f"{Fore.GREEN}█{Fore.YELLOW}{' ' * 68}{Fore.GREEN}█")
                print(f"{Fore.GREEN}{'█'*70}{Fore.RESET}")
                time.sleep(1.5)
                return True
            else:
                if codemaster.get_remaining_attempts() > 0:
                    print(f"\n{Fore.CYAN}Would you like a logical hint? (y/n){Fore.RESET}")
                    hint_choice = input(f"{Fore.GREEN}> {Fore.RESET}")
                    if hint_choice.lower() == 'y':
                        print(codemaster.get_hint())
        
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}[!] Hack interrupted!{Fore.RESET}")
            return False
    
    print(f"\n{Fore.RED}{'█'*70}")
    print(f"{Fore.RED}█{Fore.YELLOW}{' ' * 68}{Fore.RED}█")
    print(f"{Fore.RED}█{Fore.YELLOW}      ❌ ACCESS DENIED! ATTEMPTS EXHAUSTED! ❌{Fore.RED}{' ' * 23}█")
    print(f"{Fore.RED}█{Fore.YELLOW}{' ' * 68}{Fore.RED}█")
    print(f"{Fore.RED}{'█'*70}{Fore.RESET}")
    print(f"\n{Fore.YELLOW}The correct code was: {''.join(str(d) for d in codemaster.target_code)}{Fore.RESET}")
    time.sleep(2)
    return False

# ==================== ASCII BANNERS ====================

def print_main_banner():
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
    print(f"\n{Fore.MAGENTA}{'═'*70}")
    print(f"{Fore.MAGENTA}║{Fore.CYAN} SIMULATION CONTROL CENTER{Fore.MAGENTA}{' ' * 46}║")
    print(f"{Fore.MAGENTA}{'═'*70}{Fore.RESET}")

# ==================== LOADING SEQUENCES ====================

def loading_sequence():
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
    print_simulation_header()
    print(f"""
{Fore.CYAN}[1]{Fore.WHITE} Local Building
{Fore.CYAN}[2]{Fore.WHITE} Apartment
{Fore.CYAN}[3]{Fore.WHITE} Private House
{Fore.CYAN}[4]{Fore.WHITE} Street
{Fore.CYAN}[5]{Fore.WHITE} District
{Fore.CYAN}[6]{Fore.WHITE} City
{Fore.CYAN}[7]{Fore.WHITE} Satellite Zone
{Fore.CYAN}[0]{Fore.WHITE} Exit
{Fore.RESET}
""")
    
    while True:
        try:
            choice = input(f"{Fore.GREEN}Select location (1-7): {Fore.RESET}")
            if choice == '0':
                return None
            if choice in ['1', '2', '3', '4', '5', '6', '7']:
                return int(choice)
            print(f"{Fore.RED}Invalid choice!{Fore.RESET}")
        except KeyboardInterrupt:
            return None

def select_difficulty():
    print(f"""
{Fore.MAGENTA}{'─'*70}
{Fore.CYAN}SELECT SIMULATION DIFFICULTY
{Fore.MAGENTA}{'─'*70}
{Fore.GREEN}[1]{Fore.WHITE} Low
{Fore.GREEN}[2]{Fore.WHITE} Medium
{Fore.GREEN}[3]{Fore.WHITE} High
{Fore.GREEN}[4]{Fore.WHITE} Extreme
{Fore.GREEN}[5]{Fore.WHITE} Impossible
{Fore.RESET}
""")
    
    while True:
        try:
            choice = input(f"{Fore.GREEN}Select difficulty (1-5): {Fore.RESET}")
            if choice in ['1', '2', '3', '4', '5']:
                return int(choice)
            print(f"{Fore.RED}Invalid choice!{Fore.RESET}")
        except KeyboardInterrupt:
            return None

# ==================== SIMULATION PROCESSES ====================

def run_simulation_processes(difficulty):
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
    print(f"\n{Fore.MAGENTA}{'─'*70}")
    print(f"{Fore.CYAN}Thank you for using TIGRAN CYBER COMMAND X!")
    print(f"{Fore.CYAN}Training simulation completed.")
    print(f"{Fore.MAGENTA}{'─'*70}{Fore.RESET}")
    print(f"\n{Fore.YELLOW}Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Fore.RESET}")
    print(f"{Fore.YELLOW}Session ID: {generate_random_id()}{Fore.RESET}")

# ==================== MAIN MENU ====================

def main():
    try:
        clear_screen()
        print_main_banner()
        time.sleep(1.5)
        
        print(f"\n{Fore.RED}{'='*70}")
        type_effect("[!] ACCESS AUTHORIZATION REQUIRED [!]", 0.02, Fore.RED)
        print(f"{Fore.RED}{'='*70}{Fore.RESET}")
        time.sleep(1)
        
        hacking_success = hacking_minigame()
        
        if not hacking_success:
            print(f"\n{Fore.RED}[!] AUTHORIZATION FAILED! ACCESS DENIED!{Fore.RESET}")
            print(f"{Fore.YELLOW}Program will exit...{Fore.RESET}")
            time.sleep(3)
            return
        
        print(f"\n{Fore.GREEN}✓ AUTHORIZATION GRANTED! WELCOME, OPERATOR!{Fore.RESET}")
        time.sleep(1.5)
        
        loading_sequence()
        time.sleep(0.5)
        
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
        
        while True:
            location = select_location()
            if location is None:
                print(f"{Fore.YELLOW}Exiting program...{Fore.RESET}")
                break
            
            difficulty = select_difficulty()
            if difficulty is None:
                break
            
            clear_screen()
            print_main_banner()
            print_simulation_header()
            
            locations = {
                1: "Local Building",
                2: "Apartment",
                3: "Private House",
                4: "Street",
                5: "District",
                6: "City",
                7: "Satellite Zone"
            }
            
            difficulties = {1: "Low", 2: "Medium", 3: "High", 4: "Extreme", 5: "Impossible"}
            
            print(f"\n{Fore.GREEN}Location: {locations[location]}")
            print(f"Difficulty Level: {difficulties[difficulty]}{Fore.RESET}")
            print(f"{Fore.MAGENTA}{'─'*70}{Fore.RESET}")
            time.sleep(1)
            
            print(f"\n{Fore.CYAN}[>] LOADING SIMULATION...{Fore.RESET}")
            for i in range(101):
                progress_bar(i, 100, prefix='Loading:', suffix='Complete')
                time.sleep(0.02)
            print()
            
            success = run_simulation_processes(difficulty)
            
            print_final_report()
            print_thank_you()
            
            print(f"\n{Fore.CYAN}Press Enter to continue or Ctrl+C to exit...{Fore.RESET}")
            try:
                input()
            except KeyboardInterrupt:
                break
            
            clear_screen()
            print_main_banner()
    
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}\n[!] Program interrupted by user.{Fore.RESET}")
    finally:
        print(f"\n{Fore.YELLOW}Shutting down TIGRAN CYBER COMMAND X...{Fore.RESET}")
        time.sleep(1)

if __name__ == "__main__":
    main()

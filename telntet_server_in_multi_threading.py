import threading
import subprocess
import sys


def telnet_server(ip, port):
    cmd = f"nc -z -w 2 {ip} {port}"
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, encoding='utf-8',
                            universal_newlines=True)
    return_code = result.returncode
    print(type(return_code))
    if return_code == 0:
        print(f'{ip} {port} accessable')
    else:
        print(f'{ip} {port} not accessable')


ip_input = sys.argv[1]
port_input = sys.argv[2]
ip_net = '.'.join(ip_input.split('.')[:-1])
if __name__ == '__main__':
    for i in range(1, 255):
        ip_addr = f'{ip_net}.{i}'

        sub_thread = threading.Thread(target=telnet_server, args=(ip_addr, port_input))

        sub_thread.start()

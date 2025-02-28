import threading
import subprocess
import sys


def write_res(filename, msg):
    with open(filename, mode='a', encoding='utf-8') as f:
        f.write(msg)


def telnet_server(ip, port):
    cmd = f"nc -z -w 2 {ip} {port}"
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, encoding='utf-8',
                            universal_newlines=True)
    return_code = result.returncode
    print(type(return_code))
    if return_code == 0:
        ok_msg = f'{ip} {port} accessable'
        print(ok_msg)
        write_res('ok.res', ok_msg)
    else:
        err_msg = f'{ip} {port} not accessable'
        print(err_msg)
        write_res('err.res', err_msg)


ip_input = sys.argv[1]
port_input = sys.argv[2]
ip_net = '.'.join(ip_input.split('.')[:-1])
if __name__ == '__main__':
    for i in range(1, 255):
        ip_addr = f'{ip_net}.{i}'

        sub_thread = threading.Thread(target=telnet_server, args=(ip_addr, port_input))

        sub_thread.start()

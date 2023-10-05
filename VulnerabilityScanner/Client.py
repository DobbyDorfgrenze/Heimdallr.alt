import subprocess
import platform
import requests


class Client:

    def __init__(self, ip):
        self.target = ip

    def install_nmap(self):
        try:
            subprocess.run(['nmap', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            print("Nmap is already installed")
        except subprocess.CalledProcessError:

            try:
                if platform.system() == "Windows":
                    # Download the Nmap installer from the official website
                    nmap_url = "https://nmap.org/dist/nmap-7.92-win32.zip"
                    subprocess.run(['curl', '-o', 'nmap.zip', nmap_url], check=True)
                    subprocess.run(['tar', '-xf', 'nmap.zip'], check=True)
                    print("Nmap installed successfully")
                else:
                    print("Unsupported operating system for Nmap installation")
            except subprocess.CalledProcessError as e:
                print(f"Error installing Nmap: {e.stderr.decode().strip()}")

    def run_nmap_scan(self, output_file):
        try:
            result = subprocess.run(['nmap', '-sV', '--script', 'vulners', '-oX', output_file, self.target],
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, text=True)
            print(result)

            result = subprocess.run(['nmap', '-sV', '--script', 'vulners', '-oX', output_file, self.target],
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, text=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running Nmap scan: {e.stderr.decode().strip()}")



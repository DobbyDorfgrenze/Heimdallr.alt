import requests
import time
from bs4 import BeautifulSoup
import socket
import pickle
import rsa
import os.path
from HTMLPageAnalyzer import *

HOST = 'localhost'
PORT = 9999
PUBLIC_KEY = 0

with open(os.path.dirname(__file__) +'/../Public-Key.txt', 'rb') as f:
    try:
        PUBLIC_KEY = pickle.load(f)
    except Exception as e:
            print(f"Error: {str(e)}")

def enumerate_pages(base_url):
    visited = set()
    to_visit = [base_url]
    vulnarabilities = []

    while to_visit:
        url = to_visit.pop()
        if url in visited:
            continue

        try:
            
            response = requests.get(url)
            time.sleep(3)
            visited.add(url)

            if response.status_code == 200:
                vulnarabilities.append(analyze_page(response.text, url))

        
                #print(vulnarabilities)

                soup = BeautifulSoup(response.text, 'html.parser')
                for link in soup.find_all('a', href=True):
                    absolute_url = link['href']
                    #print(absolute_url)
                    split_url = base_url.split("//", 1)[1]
                    #print(split_url)
                    if "www" in split_url.split(".")[0]:
                        split_url = split_url.split(".")[1]
                    else:
                        split_url= split_url.split(".")[0]
                    #if absolute_url not in to_visit and (absolute_url.startswith("/") or split_url in absolute_url):
                        #to_visit.append(absolute_url)

        except Exception as e:
            print(f"Error visiting {url}: {str(e)}")
            visited.add(url)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        data = pickle.dumps(vulnarabilities)
        encMessage = rsa.encrypt(data, PUBLIC_KEY)
        s.sendall(encMessage)
        encMessage = s.recv(2048)
 
if __name__ == "__main__":
    base_url = "https://www.google.com" 
    enumerate_pages(base_url)


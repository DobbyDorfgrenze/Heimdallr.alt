import requests
import time
from bs4 import BeautifulSoup
import socket
import pickle
import rsa

HOST = 'localhost'
PORT = 9999
PUBLIC_KEY = 0

with open('../Public-Key.txt', 'rb') as f:
    print(pickle.load(f))
    try:
        PUBLIC_KEY = pickle.load(f)
    except Exception as e:
            print(f"Error finding key: {str(e)}")

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
                    test = base_url.split("//", 1)[1]
                    #print(test)
                    if "www" in test.split(".")[0]:
                        test = test.split(".")[1]
                    else:
                        test= test.split(".")[0]
                    #if absolute_url not in to_visit and (absolute_url.startswith("/") or test in absolute_url):
                        #to_visit.append(absolute_url)

        except Exception as e:
            print(f"Error visiting {url}: {str(e)}")
            visited.add(url)
    


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        data = pickle.dumps(vulnarabilities)
        s.sendall(data)
        data = s.recv(1024)


    
def analyze_page(html_content, url):
    #print(html_content)
    vulns = ""
    if "error in your SQL syntax" in html_content:
        #print(f"[SQL Injection] Possible vulnerability found at {url}")
        vulns+=("[SQL Injection]")

    if "<script>alert('XSS')</script>" in html_content:
        #print(f"[XSS] Possible vulnerability found at {url}")
        vulns+=("[XSS]")

    if "CSRFToken" not in html_content:
        #print(f"[CSRF] Possible vulnerability found at {url}")
        #https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/06-Session_Management_Testing/05-Testing_for_Cross_Site_Request_Forgery
        vulns+=("[CSRF]")

    if "include(" in html_content:
        #print(f"[File Inclusion] Possible vulnerability found at {url}")
        vulns+=("[File Inclusion]")

    if "system(" in html_content:
        #print(f"[Command Injection] Possible vulnerability found at {url}")
        vulns+=("[Command Injection]")

    if "../" in html_content or "%2e%2e/" in html_content:
        #print(f"[Directory Traversal] Possible vulnerability found at {url}")
        vulns+=("[Directory Traversal]")

    if "fetch(" in html_content:
        #print(f"[SSRF] Possible vulnerability found at {url}")
        vulns+=("[SSRF]")

    if "DOCTYPE" in html_content:
        #print(f"[XXE] Possible vulnerability found at {url}")
        vulns+=("[XXE]")

    if "window.location" in html_content:
        #print(f"[Open Redirect] Possible vulnerability found at {url}")
        #https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/11-Client_Side_Testing/04-Testing_for_Client_Side_URL_Redirect
        vulns+=("[Open Redirect]")

    if "password" in html_content or "api_key" in html_content:
        #print(f"[Sensitive Data Exposure] Possible vulnerability found at {url}")
        vulns+=("[Sensitive Data Exposure]")

    #print(vulns)
    vulns+=f" Possible Vulnerabilities found at {url}"
    return vulns

 
if __name__ == "__main__":
    base_url = "https://www.google.com" 
    enumerate_pages(base_url)


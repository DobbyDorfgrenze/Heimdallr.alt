import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver

def enumerate_pages(base_url):
    visited = set()
    to_visit = [base_url]

    while to_visit:
        url = to_visit.pop()
        if url in visited:
            continue

        try:
            browser = webdriver.Firefox(r'C:\Users\Public\Desktop\Firefox')
            browser.get(url)
            html = browser.page_source
            print(html)
            soup = BeautifulSoup(html, 'lxml')
            a = soup.find('section', 'wrapper')
            response = requests.get(url)
            visited.add(url)

            if response.status_code == 200:
                analyze_page(response.text, url)
                print(response.text)

                soup = BeautifulSoup(response.text, 'html.parser')
                for link in soup.find_all('a', href=True):
                    absolute_url = link['href']
                    print(absolute_url)
                    test = base_url.split("//", 1)[1]
                    print(test)
                    if "www" in test.split(".")[0]:
                        test = test.split(".")[1]
                    else:
                        test= test.split(".")[0]
                    if absolute_url not in to_visit and (absolute_url.startswith("/") or test in absolute_url):
                        to_visit.append(absolute_url)

        except Exception as e:
            print(f"Error visiting {url}: {str(e)}")
            visited.add(url)


    
def analyze_page(html_content, url):
    if "error in your SQL syntax" in html_content:
        print(f"[SQL Injection] Possible vulnerability found at {url}")

    if "<script>alert('XSS')</script>" in html_content:
        print(f"[XSS] Possible vulnerability found at {url}")

    if "CSRFToken" not in html_content:
        print(f"[CSRF] Possible vulnerability found at {url}")

    if "include(" in html_content:
        print(f"[File Inclusion] Possible vulnerability found at {url}")

    if "system(" in html_content:
        print(f"[Command Injection] Possible vulnerability found at {url}")

    if "../" in html_content or "%2e%2e/" in html_content:
        print(f"[Directory Traversal] Possible vulnerability found at {url}")

    if "fetch(" in html_content:
        print(f"[SSRF] Possible vulnerability found at {url}")

    if "DOCTYPE" in html_content:
        print(f"[XXE] Possible vulnerability found at {url}")

    if "window.location" in html_content:
        print(f"[Open Redirect] Possible vulnerability found at {url}")

    if "password" in html_content or "api_key" in html_content:
        print(f"[Sensitive Data Exposure] Possible vulnerability found at {url}")

 
if __name__ == "__main__":
    base_url = "http://localhost:4200/" 
    enumerate_pages(base_url)

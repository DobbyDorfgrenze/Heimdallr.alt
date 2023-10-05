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
        #https://owasp.org/www-project-web-security-split_urling-guide/lasplit_url/4-Web_Application_Security_split_urling/06-Session_Management_split_urling/05-split_urling_for_Cross_Site_Request_Forgery
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
        #https://owasp.org/www-project-web-security-split_urling-guide/v41/4-Web_Application_Security_split_urling/11-Client_Side_split_urling/04-split_urling_for_Client_Side_URL_Redirect
        vulns+=("[Open Redirect]")

    if "password" in html_content or "api_key" in html_content:
        #print(f"[Sensitive Data Exposure] Possible vulnerability found at {url}")
        vulns+=("[Sensitive Data Exposure]")

    #print(vulns)
    vulns+=f" Possible Vulnerabilities found at {url}"
    return vulns
import time
from datetime import datetime as dt

# Haetaan host path
hosts_path = "c:\Windows\System32\Drivers\etc\hosts"

# loaclhost (tulee uudelleenohjaamaan tähän)
redirect = "127.0.0.1"

website_list = [
    "www.instagram.com",
    "www.iltalehti.fi",
    "www.iltasanomat.fi",
    "www.aamulehti.fi",
    "www.hs.fi"
]
while True: 
  
    # time of your work 
    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16): 
        print("Working hours...") 
        with open(hosts_path, 'r+') as file: 
            content = file.read() 
            for website in website_list: 
                if website in content: 
                    pass
                else: 
                    # mapping hostnames to your localhost IP address 
                    file.write(redirect + " " + website + "\n") 
else: 
        with open(hosts_path, 'r+') as file: 
            content=file.readlines() 
            file.seek(0) 
            for line in content: 
                if not any(website in line for website in website_list): 
                    file.write(line) 

            # removing hostnmes from host file 
            file.truncate() 
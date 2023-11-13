import time
from datetime import datetime as dt

host_path = "C:/Windows/Systems32/drivers/etc/hosts"
redirect = "127.0.0.1"
website_list = ["www.aamulehti.fi"]
print("Alakaa")

while True:
    start_time = dt(dt.now().year,dt.now().month,dt.now().day,8)
    present_time = dt.now()
    end_time = dt(dt.now().year,dt.now().month,dt.now().day,16)
    if start_time < present_time < end_time:
        with open(host_path, 'r+') as file:
            content = file.read()
            for websites in website_list:
                if websites in content:
                    pass
                else:
                    file.write(redirect+" "+websites + "\n")
        time.sleep(30)
    
    else:
        with open(host_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
            time.sleep(30)
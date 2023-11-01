from datetime import datetime as dt

# Haetaan host path
hostpath = "c:\Windows\System32\Drivers\etc\hosts"

# loaclhost (tulee uudelleenohjaamaan tähän)
redirect = "127.0.0.1"

websitelist = [
    "www.instagram.com",
    "www.iltalehti.fi",
    "www.iltasanomat.fi",
    "www.aamulehti.fi",
    "www.hs.fi"
]
"""
Datetime Format
--------------
The datetime format is Year, Month, Day, Hour, Minute, 
e.g. (2022, 12, 28, 14, 15)
2022 - year
12 - month
28 - day
14 - hour (24 hrs format) (14 hrs = 2 pm)
15 - minutes
"""

# Blokataan klo: 8-16
blocktime = {
    "start": dt(dt.now().year, dt.now().month, dt.now().day, 8),
    "end": dt(dt.now().year, dt.now().month, dt.now().day, 16)
}
if blocktime["start"] < dt.now() < blocktime["end"]:
    # to know our current mode
    print("Time to focus ...")

    # read the `host` file to check the list
    with open(hostpath, "r+") as file:
        content = file.read()
        for website in websitelist:
            # if your website is not in the `host` file, add the website
            if not website in content:
                with open(hostpath, "a") as writefile:
                    writefile.write(redirect + " " + website + "\n")

            else: print("Enjoy your free time ...")

    # If the current time is not between working time, remove the websites
    with open(hostpath, "r+") as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in websitelist):
                file.write(line)
        # removing websites from the `host` file
        file.truncate()
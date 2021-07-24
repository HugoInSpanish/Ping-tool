import os

def ping(hostname):
    os.system("ping " + hostname)

print(ping("google.com"))
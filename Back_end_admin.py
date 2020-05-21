import time
from datetime import datetime as dt
import threading

hosts_temp = "hosts"
hosts_path = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.0"
switch = True



def add(website_list,starting_time,ending_time):
    def run():
        while switch:
            if dt(dt.now().year,dt.now().month,dt.now().day,starting_time) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,ending_time):
                with open(hosts_path,"r+") as file:
                    content = file.read()
                    print(website_list)
                    for website in website_list:
                        if website in content:
                            pass
                        else:
                            file.write("\n" + redirect +" " +"www." + website +"\n")
                
        
            else:
                with open (hosts_path,"r+") as file:
                    content = file.readlines()
                    file.seek(0)
                    for line in content:
                        if not any (website in line for website in website_list):
                            file.write(line)
                            file.truncate()
                            
            time.sleep(5)
    thread = threading.Thread(target=run)
    thread.start()    

def delete(website_list):
    global switch
    switch = False
    with open (hosts_path,"r+") as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any (website in line for website in website_list):
                file.write(line)
                file.truncate()
    

def update(website_list):
    global switch
    switch = False
    with open(hosts_path,"r+") as file:
            content = file.read()
            
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write("\n" + redirect +" "+"www." + website +"\n")
                    switch =True
    
                

def view():
    view_list = []
    with open (hosts_path,"r+") as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if line.startswith("127.0.0.0"):
                ind = line.find(" ")
                entry = line[ind+1:]
                view_list.append(entry)
    return view_list            

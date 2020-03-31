#import neccessory module
import os 
#these variable acts as switch for changing the color
global_background = 63
welcome_text = 4
welcome_background = 10
created_text = 17
created_background = 14
location_text = 9
location_background = 15
options_text = 4
options_background = 11
choice_text = 17
choice_background = 15
exit_text = 15
exit_background = 0
server_ip_text = 4
server_ip_background = 10
continue_text = 4
continue_background = 13

def Message():
    os.system("tput setab {}".format(global_background))

    os.system("clear")

    os.system("tput setaf {}".format(welcome_text))
    os.system("tput setab {}".format(welcome_background))

    print("\t\t\t\tWelcome to Our TUI")

    os.system("tput setaf {}".format(created_text))
    os.system("tput setab {}".format(created_background))
    print("\t\t\t     Created by PythonPingerZ     ")
def IsPingable(Server_IP):
   
    os.system("ping -c 1 {}".format(Server_IP))
    p=-1
#out put of os.system cannot be stored in a 						variable so we use os.popen it will pop the 						output that can be stored in some variable
#if p==0 the we can ping to each other 						otherwise not...
    p=os.popen("echo $?").read()
    print("this is {}".format(p))
    
    if p==0:
        print("Now you can ale to do SSH to your Network")
    else:
        print("We are not able to ping to your provided IP")
        os.system("tput setab {}".format(global_background))
        exit() 
    


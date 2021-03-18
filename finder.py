from argparse import *
from os import walk
# global var
result = ''
# end

def args_parse():
    parser = ArgumentParser()
    parser.add_argument('-f',help='File which you want to search in')
    parser.add_argument('-s',help='The string that you want to find')
    parser.add_argument('-d',help='Directory name  if you lookin for in directory',required=False)
    args = parser.parse_args()
    return args

def get_line_number(filename,string):
    global result
    try:
        file_text = open(filename,'r').read()
        line_string = file_text.split('\n')
        len_line = len(line_string)
        for i in line_string:
            if string in i:
                result+='[*] found '
                result+=filename+'   =>  '+i+'\n'
    except:
        print('[!] file %s cannot be opened' %(filename))
        
def find_in_dirs(directory,string):
    for root,dirs,files in walk(directory):
        for i in range(len(files)):
            full_path = root+'/'+files[i]
            full_path = full_path.replace('\\','/')
            get_line_number(full_path,string)


def main(filename,string):
    if '.' in str(filename):
        get_line_number(filename,string)
    else:
        print('[*] Look up in %s directory' %(filename))
        find_in_dirs(filename,string)
    print(result)


if __name__=='__main__':
    args = args_parse()
    try:
        if(args.f):
            main(args.f,args.s)
        elif(args.d):
            main(args.d,args.s)
        else:
            pass
    except:
        print('Usage: <filename> <option>\nEx   :  python finder.py -f test.txt -s \'no one care\'')

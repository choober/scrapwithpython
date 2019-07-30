import requests
from lxml import html
from getpass import getpass
from bs4 import BeautifulSoup


def login():
    usr = raw_input("Username : ")
    pwd = getpass("Password : ")
    user_ip = "118.96.58.173"
    browser_info = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
    action = "login"
    mobile = "false"

    loginurl ="https://ibank.klikbca.com/authentication.do"

    data = {"value(actions)":action,"value(user_id)":usr,"value(user_ip)":user_ip,"value(browser_info)":browser_info,"value(mobile)":mobile,"value(pswd)":pwd}
    r = requests.post(loginurl,data = data)
    #print BeautifulSoup(r.content, "html.parser")
    print str(r.content)
    if str(r.content) == "Informasi Rekening":
	    print "berhasil"
    else:
        print "Login Failed!"

def logout():
    logouturl = "https://m.klikbca.com/authentication.do?value(actions)=logout"
    requests.post(logouturl, headers = logouturl)

def main():
    rtn = login()
    #if rtn == "berhasil":
    #    urlsaldo = "https://ibank.klikbca.com/balanceinquiry.do"
    #    rslt = requests.post(urlsaldo, headers = urlsaldo)
    #    tree = html.fromstring(rslt.content)
    #    print rslt.content
    #else:
    print rtn

if __name__ == '__main__':
	main()

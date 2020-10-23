import datetime, requests, base64


LOGIN_PAGE_URL = "http://172.20.20.1:801/srun_portal_pc.php?ac_id=3&"

# add your DLUT ID and password here
usrid = ''
passwd = ''


def login_request(usrid, passwd):
    data1 = {"action"  : "login",
             "ac_id"   : 3, 
             "username": usrid,
             "password": passwd}

    try:
        result = requests.post(LOGIN_PAGE_URL, data=data1)
        print(result.text)
        print("[01] {} login success  ".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    except:
        print("[00] {} requsest error ".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))


login_request(usrid, passwd)

import requests
from checkMsg import checkMsg
from config.account import get_account
from encrypt.main import xpros


class WebLogin:
    def __init__(self) -> None:
        self.username, self.password = get_account()
        self.session = requests.Session()
        self.session.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
                      "application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Cache-Control": "max-age=0",
            "Content-Type": "application/x-www-form-urlencoded",
            "Host": "10.254.7.4",
            "Origin": "http://10.254.7.4",
            "Proxy-Connection": "keep-alive",
            "Referer": "http://10.254.7.4",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66 "
        }

    def ask_index(self):
        res = self.session.get("http://10.254.7.4/0.htm", timeout=1)
        self.session.headers['Referer'] = "http://10.254.7.4/0.htm"
        return res

    def login(self):
        data = {
            "DDDDD": self.username,
            "upass": xpros(self.password),
            "R1": 0,
            "R2": 1,
            "para": '02',
            "0MKKey": 123456,
            "v6ip": ""
        }

        return self.session.post("http://10.254.7.4/0.htm", data=data, timeout=1)


if __name__ == '__main__':
    webLogin = WebLogin()

    webLogin.ask_index()
    res = webLogin.login()

    msg = checkMsg(res.text)

    if msg == 'UB':
        res = webLogin.session.get("http://10.254.7.4:9002/In1", timeout=1)
        print("登录成功")
    elif msg == '05':
        print('帐号暂停使用（可能是欠费了）')
    elif msg == '01':
        print('请确认账号密码是否正确以及是否在规定时间登录')
    else:
        with open('debug/loginError.html', "wb") as f:
            f.write(res.content)
        print("可能出了点问题")

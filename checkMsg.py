def checkMsg(htmlStr):
    headStr = "Msg="
    msgPosition = htmlStr.find(headStr) + len(headStr)
    msg = htmlStr[msgPosition:msgPosition + 2]
    return msg


if __name__ == '__main__':
    with open('debug/signResponse.html', 'r') as f:
        text = f.read()
    print(checkMsg(text))

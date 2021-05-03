import os


def account_exist() -> bool:
    if not os.path.exists('account.yml'):
        return False
    with open('account.yml', 'r') as yml:
        if yml.read() == "":
            return False
        else:
            return True


def set_account() -> None:
    username = input('请输入帐号：')
    password = input('请输入密码：')

    with open('account.yml', 'w') as yml:
        yml.write(username)
        yml.write('\n')
        yml.write(password)


def get_account() -> [str, str]:
    if not account_exist():
        set_account()
    with open('account.yml', 'r') as yml:
        username, password = yml.read().split('\n')
    return username, password



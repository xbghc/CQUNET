import execjs


def xpros(p):
    with open('encrypt/a41.js', 'r', encoding='utf8') as f:
        jstext:str = f.read()
    ctx = execjs.compile(jstext)
    result = ctx.call('sp', p)
    return result
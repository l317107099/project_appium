import execjs

query = '中国'

with open('baidufanyi.js', 'r', encoding='utf-8') as f:
    ctx = execjs.compile(f.read())

sign = ctx.call('e', query)
print(sign)

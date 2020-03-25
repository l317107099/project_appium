def response(flow):
    url = flow.request.url
    if "https://report.meituan.com" in url:

        with open("reques.txt","w+",encoding='utf-8') as f:
            f.write(flow.request.text)

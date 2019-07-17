import requests

url = 'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?type='
headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
            # 'Cookie': 'bid=Y8fLTbDHvP8; douban-fav-remind=1; __yadk_uid=dUm5rrPv49usekYzbHMsiDBgnYHbbrt2; ll="108288"; _vwo_uuid_v2=DF2153AFB24D8DDE4A3AB7B7451DFF5A7|57bbd79ec8cfde5f30aeff6432b586aa; push_noty_num=0; push_doumail_num=0; __utmv=30149280.18837; __gads=ID=b0355c5e242a3f94:T=1560473356:S=ALNI_Mb64HZdDcZV24Ge5y4KaBDUT9ARIQ; gr_user_id=255857fa-b372-4f11-9487-65b15e9f665d; __utmc=30149280; viewed="25862578_4913064_1770782_27194720_26829016"; gr_cs1_eda4799c-1985-481d-b720-93515ecdff01=user_id%3A1; __utma=30149280.1027424141.1558536968.1562989896.1563004408.27; __utmz=30149280.1563004408.27.15.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/passport/login; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=616d912d-f5a1-43c8-b3f7-ff2267ce2088; gr_cs1_616d912d-f5a1-43c8-b3f7-ff2267ce2088=user_id%3A1; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_616d912d-f5a1-43c8-b3f7-ff2267ce2088=true; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1563007290%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D6JA9-A-UT3kmslX1Ba5uTPcE9QdIPZcAUol_LFjYBMnVYhJx7DbqbHZWNhZJXVZl%26wd%3D%26eqid%3Db69c81920000c37d000000035d294179%22%5D; _pk_ses.100001.8cb4=*; _pk_id.100001.8cb4=aa46c53db7ab13bd.1558536967.15.1563007298.1563004463.; __utmt=1; __utmb=30149280.12.10.1563004408; dbcl2="188372921:kYaOA9xFlUk"'
        }
proxies = {
    'http': 'http://118.123.113.4:80'
}
response = requests.get(url=url,headers=headers,proxies=proxies).content.decode('utf-8')
with open('book_list.html','w',encoding='utf-8') as fp:
    fp.write(response)
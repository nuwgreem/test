import requests
import json



def get_date(url):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-encoding": "gzip, deflate, br",
        "Accept-language": "en-US,en;q=0.9,de;q=0.8,fr;q=0.7,lt;q=0.6,ru;q=0.5,sr;q=0.4,zh-CN;q=0.3,zh;q=0.2,it;q=0.1,sk;q=0.1,ca;q=0.1,es;q=0.1",
        "Cache-control": "max-age=0",
        "Connection": "keep-alive",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"
    }

    r = requests.get(url=url, headers=headers)

    with open("index.json", "w") as file:
        json.dump(requests.json(), file, ensure_ascii=False)

def main():
    get_date("https://cs.money/ru/")


if __name__ == '__main__':
    main()
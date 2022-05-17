from fake_useragent import UserAgent
import requests
import json

ua = UserAgent()
print(ua.random)

def collect_data():
    response = requests.get(
        url='https://inventories.cs.money/5.0/load_bots_inventory/730?buyBonus=40&isStore=true&limit=60&maxPrice=10000&minPrice=1&offset=60&quality=fn&quality=mw&type=2&withStack=true',
        headers={'user-agent': f'{ua.random}'}
    )


    with open('result.json', 'w') as file:
        json.dump(response.json(), file, indent=4, ensure_ascii=False)

def main():
    collect_data()


if __name__ == '__main__':
    main()
import requests

def get_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    if response.ok:
        print("Başlık:", response.json()['title'])
    else:
        print("İstek başarısız:", response.status_code)

if __name__ == "__main__":
    get_post()
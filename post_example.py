import requests

def send_form():
    url = "https://httpbin.org/post"
    data = {"kullanici": "omer", "mesaj": "Merhaba!"}
    response = requests.post(url, data=data)
    if response.ok:
        print("Sunucudan gelen yanıt:")
        print(response.json())
    else:
        print("Gönderim hatalı:", response.status_code)

if __name__ == "__main__":
    send_form()
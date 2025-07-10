
# 🔥 Python `requests` Kütüphanesi: API ile Konuşmanın En Kolay Hali

> Python ile internetten veri çekmek, bir API ile konuşmak ya da bir siteye veri göndermek mi istiyorsun? O zaman `requests` senin en yakın dostun olacak. Bu yazıda `requests` kütüphanesini sıfırdan, gerçek hayattan örneklerle öğreniyoruz.

---

## 🚀 1. `requests` Nedir, Neden Kullanılır?

Python’un standart `urllib` modülü biraz karışıktır. `requests` ise “HTTP for humans” sloganıyla çıktı ve o günden beri Python'daki en popüler kütüphanelerden biri haline geldi.

**Avantajları:**
- Kolay sözdizimi
- JSON, dosya, form, cookie, session yönetimi
- Hata ayıklama kolaylığı

---

## 🔧 2. Kurulum

Terminale şunu yazman yeterli:

```
pip install requests
```

---

## 🌐 3. Basit Bir GET İsteği

```python
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)
print(response.text)
```

- `status_code`: 200 → başarılı demek  
- `text`: Gelen cevabın düz hali (HTML ya da JSON olabilir)

---

## 🔍 4. JSON Verisini Okumak

```python
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
data = response.json()

print("Başlık:", data['title'])
print("İçerik:", data['body'])
```

💡 `response.json()` JSON verisini Python sözlüğüne çevirir. Böylece içinden kolayca veri çekebilirsin.

---

## 📨 5. POST İsteği (Sunucuya Veri Göndermek)

```python
url = "https://httpbin.org/post"
veri = {"ad": "Faruk", "mesaj": "Merhaba dünya!"}

response = requests.post(url, data=veri)
print(response.json())
```

Kullanım örneği: Giriş formu, yorum gönderme, kayıt işlemleri vb.

---

## 🧪 6. Gerçek Hayat Senaryoları

### 🌤️ Hava Durumu API'si Kullanmak

```python
API_KEY = "senin_api_keyin"
city = "Istanbul"
url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&lang=tr"

response = requests.get(url)
weather = response.json()

print(f"{city} için sıcaklık: {weather['current']['temp_c']}°C")
```

---

### 📲 Telegram Bot'tan Mesaj Göndermek

```python
bot_token = "BOT_TOKEN"
chat_id = "123456789"
message = "Python'dan selamlar!"

url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
payload = {"chat_id": chat_id, "text": message}

r = requests.post(url, data=payload)
print(r.ok)
```

---

### 🧷 Dosya İndirme

```python
url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
response = requests.get(url)

with open("dosya.pdf", "wb") as f:
    f.write(response.content)

print("Dosya indirildi.")
```

---

### 🔁 Birden Fazla Siteyi Kontrol Etmek (Uptime Bot)

```python
sites = ["https://google.com", "https://github.com", "https://siteyok.com"]

for site in sites:
    try:
        response = requests.get(site, timeout=2)
        if response.ok:
            print(f"{site} AKTİF ✅")
        else:
            print(f"{site} HATA ⚠️")
    except:
        print(f"{site} ERİŞİLEMİYOR ❌")
```

---

## 🍪 7. Session (Oturum) Yönetimi

```python
session = requests.Session()
session.get("https://httpbin.org/cookies/set/mycookie/test123")

response = session.get("https://httpbin.org/cookies")
print(response.json())
```

---

## 🔐 8. Basic Auth (Kullanıcı Girişi)

```python
from requests.auth import HTTPBasicAuth

response = requests.get(
    "https://httpbin.org/basic-auth/admin/1234",
    auth=HTTPBasicAuth("admin", "1234")
)

print(response.status_code)
```

---

## ⚠️ 9. Hata Yakalama

```python
try:
    r = requests.get("https://siteyok.com")
    r.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Hata oluştu:", e)
```

---

## ⏱️ 10. Timeout ve Proxy Kullanımı

### Zaman Aşımı:

```python
requests.get("https://httpbin.org/delay/5", timeout=2)
```

### Proxy Kullanımı:

```python
proxies = {
    "http": "http://10.10.1.10:3128",
}
requests.get("http://example.com", proxies=proxies)
```

---

## 🧠 Ekstra Bilgiler

- `response.headers` → gelen başlık bilgileri  
- `response.content` → ikili veri (PDF, resim vs.)  
- `response.url` → yönlendirildiyse son URL  
- `allow_redirects=False` → yönlendirmeyi engeller

---

## 📚 Kaynaklar

- 🔗 [Resmi Belgeler](https://docs.python-requests.org/)
- 🧪 [HTTPBin (Test için API)](https://httpbin.org/)
- 🛠️ [JSONPlaceholder](https://jsonplaceholder.typicode.com/)
- 🌦️ [WeatherAPI](https://www.weatherapi.com/)

---

## ✍️ Son Söz

Python’daki en güçlü kütüphanelerden biri olan `requests`, internetle konuşmanın en kısa ve temiz yoludur. Bu yazı sayesinde artık API’lerden veri çekebilir, botlara mesaj gönderebilir veya kendi projende kolayca web’den bilgi alabilirsin.

Beğendiysen paylaşmayı, yıldızlamayı ve yorum bırakmayı unutma.  
GitHub’da: **@omerfaruk-shp**  
Selamlar! 🚀

import requests

def download_pdf():
    url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
    response = requests.get(url)
    if response.ok:
        with open("dummy.pdf", "wb") as f:
            f.write(response.content)
        print("PDF başarıyla indirildi.")
    else:
        print("Dosya indirilemedi:", response.status_code)

if __name__ == "__main__":
    download_pdf()
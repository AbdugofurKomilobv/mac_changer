import requests

url = "https://docs.google.com/forms/u/2/d/e/1FAIpQLSfiycLHbU4jfWvikxCWJpOqCKW-CD_iimdijBtUPOF5NXyfBw/formResponse?pli=1"

data = {
    "entry.123456789": "4 дня",
    "entry.987654321": "1 час / 3 дня"
}

res = requests.post(url, data=data)
print(res.status_code)

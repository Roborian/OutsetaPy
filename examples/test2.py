import requests

url = "https://roborian.outseta.com/tokens"

payload = "username=b.savelkouls@roborian.com"
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Authorization": "Outseta 25daa814-3889-4134-a026-88a1e4ea721c:ff39ad05edaea3571e33410d1c5b6ee9",
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

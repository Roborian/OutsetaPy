import requests
import os

OUTSETA_SUBDOMAIN = os.getenv("OUTSETA_SUBDOMAIN")
OUTSETA_API_KEY = os.getenv("OUTSETA_API_KEY")
OUTSETA_API_SECRET = os.getenv("OUTSETA_API_SECRET")

url = f"https://{OUTSETA_SUBDOMAIN}.outseta.com/tokens"

payload = "username=b.savelkouls@roborian.com"
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Authorization": f"Outseta {OUTSETA_API_KEY}:{OUTSETA_API_SECRET}",
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

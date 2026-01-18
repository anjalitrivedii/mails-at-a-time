import requests
import time

API_KEY = "you_API_key"

url = "https://api.brevo.com/v3/smtp/email"

headers = {
    "accept": "application/json",
    "api-key": API_KEY,
    "content-type": "application/json"
}

recipients = [
    "sabbirrajput03@gmail.com",
    "roshnipalas1@gmail.com",
    "zarna037@gmail.com",
    "anjalitrivedii287@gmail.com"
]

for email in recipients:
    data = {
        "sender": {
            "name": "Tech Minds",
            "email": "techminds011@gmail.com"
        },
        "to": [
            {"email": email}
        ],
        "subject": "Quick update from TechMind",
        "htmlContent": """
        <p>Hello,</p>
        <p>sorry to spam your mail box but i was just checking if my code is working or not :)))).</p>
        <p>Regards,<br>TechMind</p>
        """
    }

    response = requests.post(url, json=data, headers=headers)

    print(f"Sent to {email} | Status: {response.status_code} | Response: {response.json()}")


    time.sleep(1)

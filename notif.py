from win10toast import ToastNotifier
import requests
while True:
    response = requests.get("https://zenquotes.io/api/random").json()[0]
    toast = ToastNotifier()
    toast.show_toast(response['a'],response['q'],duration=60)
from flask import Flask
from flask import Flask, render_template, redirect, url_for, request, session, send_file
import requests, json

# -----------------------------
def share(access_token, status_url, ua):
    headers ={
        'authority': 'graph.facebook.com',
        'cache-control': 'max-age=0', 
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        'sec-ch-ua-mobile': '?0', 
        'upgrade-insecure-requests': '1',
        'user-agent': ua,
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1', 
        'sec-fetch-dest': 'document', 
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5' }

    res = requests.post(f"https://graph.facebook.com/me/feed?link={status_url}&published=0&access_token={access_token}", headers=headers).json()

    if 'id' in res:
        return 'oke'
    else:
        return 'error'

# -----------------------------



app = Flask(__name__)



@app.route('/', methods=['POST', 'GET'])
def homepage():
    return 'homepage'


@app.route('/api', methods=['GET', 'POST'])
def share_ao():
    count = 1
    access_token = str(request.args.get('token'))
    status_url = str(request.args.get('url'))
    ua = str(request.args.get('ua'))
    while True:
        try:
            return share(access_token, status_url, ua)
        except:
            pass



@app.errorhandler(404)
def notfound(e):
    return redirect('/')

# ===============================================================

if __name__ == '__main__':
    app.run(debug=True)
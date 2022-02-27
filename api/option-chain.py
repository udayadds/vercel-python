from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

	def do_GET(self):
		s = self.path
		dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
		self.send_response(200)
		self.send_header('Content-type','application/json')
		self.end_headers()

		if 'ticker' in dic:
			ticker = dic['ticker']
		else:
			ticker = "SBIN"

		baseurl = "https://www.nseindia.com/"
		# url = f"https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"
		url = f"https://www.nseindia.com/api/option-chain-equities?symbol="+ticker
		headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62',
            'accept-language': 'en,gu;q=0.9,hi;q=0.8', 'accept-encoding': 'gzip, deflate, br'
        }
		session = requests.Session()
		request = session.get(baseurl, headers=headers, timeout=5)
		cookies = dict(request.cookies)
		response = session.get(url, headers=headers, timeout=5, cookies=cookies)
		# print(response.json())

		self.wfile.write(response.json().encode())
		return
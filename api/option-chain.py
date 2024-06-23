from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

	def do_GET(self):
		s = self.path
		dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
		self.send_response(200)
		self.send_header('Content-type', 'application/json')
		self.end_headers()

		if 'ticker' in dic:
			ticker = dic['ticker']
		else:
			ticker = "SBIN"

		baseurl = "https://www.nseindia.com/"
		# url = f"https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"
		url = "https://nsearchives.nseindia.com/products/content/sec_bhavdata_full_21062024.csv"
		# print(url)
		headers = {
		}
        
		session = requests.Session()
		request = session.get(baseurl, headers=headers, timeout=10)
		cookies = dict(request.cookies)
		response = session.get(url, headers=headers, timeout=10, cookies=cookies)
		# print(response.json())
		# print(f'Status Code: {response.status_code}')
		# result = response.json()

		self.wfile.write(response.content)
		return

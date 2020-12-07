from flask import Flask, escape, request
import pam
from dotenv import load_dotenv
from os import getenv, path
import json

load_dotenv()

username = getenv("user")
json_path = getenv("memedagsins_json")
all_memes = []

p = pam.pam()
app = Flask(__name__)

@app.route('/set_meme')
def set_meme():
	passw = request.args.get("leyniord")
	meme = request.args.get("meme")

	if meme == None:
		return "Meme vantar\n", 400
	
	if passw == None:
		return "Lykilorð vantar\n", 400
	
	if p.authenticate(username, passw):
		all_memes.append(meme)
		write_json(all_memes)
		return "Success", 202

	return "", 401


@app.route('/get_meme')
def get_meme():
	index = request.args.get("index")
	if len(all_memes) == 0:
		return "", 204

	try:
		if index is None:
			index = len(all_memes) - 1
		else:
			index = int(index)

		meme = all_memes[index]
		
		retval = {
			'meme_url': meme,
			'meme_count': len(all_memes),
			'current_meme': index,
		}

		return json.dumps(retval), 200
	
	except:
		return "Bad request", 400



def get_json():
	if not path.exists(json_path):
		print(f"Creating $json_path")
		ls = []
		with open(json_path, "w") as f:
			f.write(json.dumps(ls))

		return ls
	
	with open(json_path, "r") as f:
		return json.loads(f.read())
		

def write_json(links):
	with open(json_path, "w") as f:
		f.write(json.dumps(links))

	return


all_memes = get_json()

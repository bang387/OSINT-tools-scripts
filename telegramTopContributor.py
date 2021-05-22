import json
import sys
count = 0

#file selection with open('.json') as myfile: 
with open(sys.argv[1], 'r') as myfile: #usage: python3.8 (.json file)
	user_dict = json.load(myfile)
	for i in user_dict['messages']:
		k = user_dict['messages'][count]
		if i['type'] == "message":
			typez = json.dumps(i['from'],ensure_ascii=False, indent = 2, separators=(',','"' ': ')).encode('utf8')
			print(typez.decode())
			count = count + 1
		if i['type'] == "service":
			typez = json.dumps(i['actor'],ensure_ascii=False, indent = 2, separators=(',', ': ')).encode('utf8')
			print(typez.decode())
			count = count + 1

#call to get list of top 10 active users where their name appears the most 
#python3.8 topContributor3.py | sort | uniq -c | sort -nr | head
#for use after exporting group chat history

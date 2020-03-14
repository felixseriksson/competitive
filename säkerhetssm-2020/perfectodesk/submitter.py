import requests
# import re

# URL = 'http://35.228.52.143:8899/submit.php'
# payload = {
#     'ticket_name': 'hej',
#     'ticket_email': 'niwod56737@newe-mail.com',
#     'ticket_text': '1'
# }

session = requests.session()
r = requests.post('http://35.228.52.143:8899/submit.php', data={
    'ticket_name': 'hej',
    'ticket_email': 'niwod56737@newe-mail.com',
    'ticket_text': '1'
})
text = r.text
#print(text)
# with open("results.txt", "w") as f:
#     f.write(s.text)
# print("finished")
# find = re.findall("[0-9]{6}", text)
# ticketid = find[1]
ticketid = text[-174:-168]
#print(ticketid)

# URLL = 'http://35.228.52.143:8899/check.php'
# payload2 = {
#     'ticket_id': ticketid
# }

session = requests.session()
s = requests.post('http://35.228.52.143:8899/check.php', data={
    'ticket_id': ticketid
})
# with open("results.txt", "w") as f:
#     f.write(s.text)
# print("finished")
print(s.text)
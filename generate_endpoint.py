import sys, time, json
from datetime import datetime

MINUTES_SINCE_LOGIN_THRESHOLD = 60

users = set()

while True:
	line = sys.stdin.readline()
	if line == '':
		break

	user, _, date_, time_, _= line.split()
	if user not in users:
		datestring = "{} {}".format(date_, time_)
		logged_date = datetime.strptime(datestring, "%Y-%m-%d %H:%M")
		delta = datetime.now() - logged_date
		if delta.total_seconds() / 60 < MINUTES_SINCE_LOGIN_THRESHOLD:
			users.add(user)

lab_stats = {
	"num_users": len(users),
	"users": list(users),
	"last_updated": time.time(),
	"text": "*{} {}* have logged into lab machines within the last hour: {}".format(len(users), "person" if len(users) == 1 else "people", ", ".join(list(users))),
	"username": "LabMonkey",
}	

with open('/cs/home/nt34/public_html/labstats.php', 'w+') as f:
	f.write(json.dumps(lab_stats, indent=4))

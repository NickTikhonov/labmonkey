# LabMonkey

Cron configuration:

```
9 * * * * /usr/bin/sh ~/Documents/labscripts/find_nodes.sh | /usr/bin/python ~/Documents/labscripts/generate_endpoint.py
```

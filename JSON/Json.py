import json

jsonfile = open("example.json", "rt")
loadedjson = json.loads(jsonfile.read());
print(loadedjson)

dumpedjson = json.dumps(loadedjson)
print(dumpedjson)
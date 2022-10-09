import json
data = {
    '418845': ('Olga', 25),
    '785236': ('Anna', 15),
    '518548': ('Boris', 43),
    '684846': ('Nikita', 27),
    '871848': ('Tanya', 12),
    '849548': ('Martin', 3),
}
with open("data.json", "w") as f:
    temp = json.dumps(data, sort_keys=True)
    f.write(temp)
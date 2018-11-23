#!/usr/bin/python

## read file with show ip arp output

audit_db = []

rf = open("show_ip_arp.txt", "r")

for line in rf:
    columns = line.split()
    audit_db.append({"ip":columns[0],"mac":columns[2]})

rf.close()

for index in audit_db:
    print(index["ip"], ":", index["mac"])

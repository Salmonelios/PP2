import json

file = open('example.json')

data_j = file.read()

data = json.loads(data_j)
print("Interface Status")
print("=======================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")
for i in range(len(data["imdata"])):
    print("{:<50} {:<20} {:<10} {:<6}".format(data["imdata"][i]["l1PhysIf"]['attributes']["dn"], data["imdata"][i]["l1PhysIf"]['attributes']["descr"], data["imdata"][i]["l1PhysIf"]['attributes']["speed"], data["imdata"][i]["l1PhysIf"]['attributes']["mtu"]))
    

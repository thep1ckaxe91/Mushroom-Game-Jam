d = {
    "2,3" : {"b_type" : "grass", "variant" : 0}
}

import json
# with open("saves/save1.json","w") as save:
#     json.dump(d,save)

with open("saves/save1.json","r") as save:
    a = json.load(save)
print(a[str(2)+','+str(3)])
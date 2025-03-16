
import json
# with open('salam/sample-date1.json', "r") as file:
#     data = json.load(file)

# out = []
# out.append("Interface Status")
# out.append("=" * 90)
# out.append(f"{'DN':<40} {'Description':<20} {'Speed':<10} {'MTU':<10}")
# out.append("-" * 90)


# for i in data["imdata"]:
#     b = i["l1PhysIf"]["attributes"]
#     out.append(f"{b['dn']:<40} {b['pathSDescr']:<20} {b['speed']:<10} {b['mtu']:<10}")

# for i in out:
#     print(i)
    
with open('salam/sample-date1.json', "r") as file:
    date = json.load(file)
    
ans = []
ans.append("interface status")
ans.append("=" * 90)
ans.append(f"{'dn':<40} {'description':<20} {'speed':<10} {'mtu':<10}")
ans.append('=' * 90)

for i in date["imdata"]:
    b = i["l1PhysIf"]["attributes"]
    ans.append(f"{b['modTs']:<40} {b['delay']:<20} {b['lcOwn']:<10} {b['mtu']:<10}")
    
for i in ans:
    print(i)
import json
from MypseudoSQL import Table


with open("./test_data/user.json") as f:
    data = json.load(f)

# create table
users = Table(["id", "name", "friends"])

# INSERT INTO
for user in data:
    users.insert(user)

with open("./test_data/interests.json") as f:
    data = json.load(f)

interests = Table(["id", "interests"])

for interest in data:
    interests.insert(interest)

usr_interest = users.join(interests, 1)

supplier = Table(["Supplier Name",
                  "Invoice Number",
                  "Part Number",
                  "Cost",
                  "Purchase Date"])

supplier.insert(["Supplier X", "001-1001", "2341", "500", "1/20/2014"])
supplier.insert(["Supplier X", "001-1001", "2341", "500", "1/20/2014"])
supplier.insert(["Supplier X", "001-1001", "5467", "750", "1/20/2014"])

data = []
for line in open("./test_data/supplier_data.csv"):
    data += [line.strip().split(",")]

for i, row in enumerate(data):
    if i == 0:
        supplier = Table(row)

    else:
        supplier.insert(row)

print supplier

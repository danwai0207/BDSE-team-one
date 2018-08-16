
#-*- coding: utf-8 -*-

tx = []
for row in open("Daily_2018_08_15.csv"):
	row = row.strip().split(",")
	part = row[1].strip()
	date = row[2].strip()

	if part == "TX" and date=="201808":
		tx += [row]

print("\n".join(map(str, tx)))
print("total transcastions: %d" % len(tx))

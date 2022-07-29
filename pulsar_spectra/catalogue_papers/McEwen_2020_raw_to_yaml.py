import json
import csv

with open("McEwen_2020_raw.tsv", "r") as raw_file:
    tsv_file = csv.reader(raw_file, delimiter="\t")
    lines = []
    for line in tsv_file:
        lines.append(line)
    print(lines)

pulsar_dict = {}
for row in lines:
    row = [r.strip() for r in row]
    if len(row) == 0:
        continue
    if row[0].startswith("#") or row[0].startswith("PSR") or row[0] == '' or row[0].startswith('-'):
        continue
    print(row)

    pulsar = row[0].strip().replace("–", "-")

    flux = round(float(row[1]), 1)
    flux_err = round(float(row[2]), 1)
    pulsar_dict[pulsar] = {"Frequency MHz":[350.], "Flux Density mJy":[flux], "Flux Density error mJy":[flux_err]}

with open("McEwen_2020.yaml", "w") as cat_file:
    cat_file.write(json.dumps(pulsar_dict, indent=1))
print(pulsar_dict)
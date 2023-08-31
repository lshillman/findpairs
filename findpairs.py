import sys
import csv

if len(sys.argv) < 3:
    print("use syntax: findpairs.py [character-list.txt] [text-to-search.txt] [optional-output-file.csv]")
    exit()

character_file = ""
source_file = ""
output_file = ""

if len(sys.argv) >= 3:
    character_file = sys.argv[1]
    source_file = sys.argv[2]

if len(sys.argv) >= 4:
    output_file = sys.argv[3]

characters = []
source = ""

with open(character_file) as character_list:
    characters = character_list.read().splitlines()

with open(source_file) as source_text:
    source = source_text.read()

pairList = []

for i in range(len(characters)):
    for j in range(len(characters)):
        if j > i:
            count = source.count(characters[i] + " and " + characters[j]) + source.count(characters[j] + " and " + characters[i])
            if count > 0:
                pairList.append({"Character 1": characters[i], "Character 2": characters[j], "Count": count})
pairList = sorted(pairList, key=lambda pair: pair["Count"], reverse=True)

for pair in pairList:
    print(pair["Character 1"] + "," + pair["Character 2"] + "," + str(pair["Count"]))

if output_file != "":
    with open(output_file, "w") as pairs_csv:
        pair_writer = csv.DictWriter(pairs_csv, fieldnames=["Character 1", "Character 2", "Count"])
        pair_writer.writeheader()
        for pair in pairList:
            pair_writer.writerow(pair)
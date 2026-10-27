import json
import pathlib
import re

t = pathlib.Path(__file__).with_name("last_assigned_feed.json").read_text()
ids = [int(x) for x in re.findall(r'"id":(\d+)', t)]
# first match is top-level "assignedtome" id string? Actually pattern matches "id":416409 inside results
# also matches "id":"assignedtome" - no digit after for string
print("raw matches", len(ids))
# filter to only numeric from results - the file has "id":"assignedtome" - no that's not digit
print(ids[:5], "...", ids[-5:])
print("23107 at", ids.index(23107))
print("unique", len(set(ids)))
print("ids[99]", ids[99])
for i in (76, 77, 78, 99, 100, 101, 121, 122):
    print(i, ids[i])
fixed = ids[:77] + ids[100:]
print("fixed len", len(fixed), "first", fixed[0], "last", fixed[-1])
pathlib.Path(__file__).with_name("_assigned_ids_one_line.txt").write_text(
    ",".join(str(i) for i in fixed), encoding="ascii"
)

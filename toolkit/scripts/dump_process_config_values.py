import json
import re
import sys
from pathlib import Path

demo = Path(sys.argv[1])
display = sys.argv[2]
data = json.loads(demo.read_text(encoding="utf-8"))
for stage in data["ProcessModelData"]["StageConfigs"]:
    for sp in stage["StageProcessConfigs"]:
        if sp["Properties"]["DisplayName"] != display:
            continue
        wa = sp["Properties"]["WorkunitArguments"]
        for m in re.finditer(r'name="([^"]+)"[^>]*>([^<]*)</argument>', wa):
            name, val = m.group(1), m.group(2)
            if val and val not in ("NA", "false", "true") or name.startswith("Show"):
                print(f"{name}={val}")

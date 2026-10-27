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
        names = re.findall(r'name="([^"]+)"', wa)
        print("\n".join(names))

"""Extract wikitext block from 360_Flow_Demo_Setup_DRAFT.md."""
from pathlib import Path

draft = Path("projects/process-platform/flow/360_Flow_Demo_Setup_DRAFT.md")
text = draft.read_text(encoding="utf-8")
start = text.index("```wikitext\n") + len("```wikitext\n")
end = text.index("\n```", start)
wikitext = text[start:end]
out = Path("outputs/360_Flow_Demo_Setup_wikitext.txt")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(wikitext, encoding="utf-8")
print(f"Wrote {len(wikitext)} chars to {out}")

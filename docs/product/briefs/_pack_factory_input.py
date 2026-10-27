import zipfile
from pathlib import Path

base = Path(__file__).resolve().parent
src = base / "ifar-file-first-processing-workspace"
out = base / "ifar-file-first-ai-factory-input.zip"
wf_dir = src / "wireframes"
wf_zip = base / "_wf-only.zip"

if wf_dir.is_dir():
    if wf_zip.exists():
        wf_zip.unlink()
    with zipfile.ZipFile(wf_zip, "w", zipfile.ZIP_DEFLATED) as wz:
        for f in sorted(wf_dir.iterdir()):
            if f.is_file():
                wz.write(f, arcname=f.name)
    repo_wf = src / "ifar-file-first-wireframes.zip"
    if repo_wf.exists():
        repo_wf.unlink()
    repo_wf.write_bytes(wf_zip.read_bytes())

SKIP_NAMES = {"ifar-file-first-wireframes.zip", "_pack_wireframes.py"}
SKIP_SUFFIX = {".zip"}  # only skip zip at workspace root; we add fresh ones

extra_files = [
    (base.parent / "360_Information_Act_Request_DRAFT.md", "reference-module-wiki-draft/360_Information_Act_Request_DRAFT.md"),
]
pfr_root = Path(r"c:\Users\MortenJensen\source\repos\te-industry-public360\docs\bmad")
extra_files += [
    (pfr_root / "ifar-pfr-research.md", "reference-pfr/ifar-pfr-research.md"),
    (pfr_root / "ifar-pfr-index.csv", "reference-pfr/ifar-pfr-index.csv"),
]

if out.exists():
    out.unlink()

with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
    zf.write(src / "BUNDLE-README-AI-SOFTWARE-FACTORY.md", "README-AI-SOFTWARE-FACTORY.md")

    for path in sorted(src.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(src)
        if rel.parts[0] == "reference-handoff":
            arc = Path("reference-handoff") / rel.relative_to("reference-handoff")
            zf.write(path, arc.as_posix())
            continue
        if path.name in SKIP_NAMES:
            continue
        if path.suffix == ".zip" and len(rel.parts) == 1:
            continue
        zf.write(path, ("workspace/" + rel.as_posix()))

    zf.write(src / "ado-epic-draft.md", "reference-handoff/ado-epic-draft.md")

    for fs, arc in extra_files:
        if fs.exists():
            zf.write(fs, arc)

    if wf_zip.exists():
        zf.write(wf_zip, "reference-wireframes/ifar-file-first-wireframes.zip")
        zf.write(wf_zip, "workspace/ifar-file-first-wireframes.zip")

print("Wrote", out, out.stat().st_size, "bytes")

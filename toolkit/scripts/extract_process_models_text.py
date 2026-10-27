"""Extract text from all .docx and .pptx in process models folder to .txt files."""
import zipfile
import xml.etree.ElementTree as ET
import re
from pathlib import Path

PROCESS_MODELS = Path(__file__).resolve().parent / "process models"
OUT_DIR = PROCESS_MODELS / "extracted_text"
OUT_DIR.mkdir(exist_ok=True)

# Word namespaces
W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
W_NS_MAP = {"w": W_NS}

# PowerPoint namespaces
A_NS = "http://schemas.openxmlformats.org/drawingml/2006/main"
A_NS_MAP = {"a": A_NS}


def extract_docx(filepath: Path) -> str:
    """Extract paragraph text from a .docx file."""
    lines = []
    with zipfile.ZipFile(filepath, "r") as z:
        with z.open("word/document.xml") as f:
            tree = ET.parse(f)
    root = tree.getroot()
    for body in root.findall(".//{%s}body" % W_NS):
        for p in body.findall("{%s}p" % W_NS):
            texts = []
            for node in p.iter():
                if node.tag.endswith("}t") and node.text is not None:
                    texts.append(node.text)
                if node.tag.endswith("}tab"):
                    texts.append("\t")
            if texts:
                line = "".join(texts).strip()
                if line:
                    lines.append(line)
    text = "\n".join(lines)
    return re.sub(r"\n{3,}", "\n\n", text)


def extract_pptx(filepath: Path) -> str:
    """Extract text from all slides in a .pptx file."""
    parts = []
    with zipfile.ZipFile(filepath, "r") as z:
        names = sorted(n for n in z.namelist() if n.startswith("ppt/slides/slide") and n.endswith(".xml"))
        for name in names:
            with z.open(name) as f:
                tree = ET.parse(f)
            root = tree.getroot()
            slide_texts = []
            for elem in root.iter():
                if elem.tag.endswith("}t") and elem.text:
                    slide_texts.append(elem.text)
                if elem.tail and elem.tail.strip():
                    slide_texts.append(elem.tail)
            if slide_texts:
                parts.append("\n".join(slide_texts))
    return "\n\n---\n\n".join(parts)


def main():
    for path in sorted(PROCESS_MODELS.iterdir()):
        if path.suffix.lower() == ".docx":
            text = extract_docx(path)
            out_path = OUT_DIR / (path.stem + ".txt")
        elif path.suffix.lower() == ".pptx":
            text = extract_pptx(path)
            out_path = OUT_DIR / (path.stem + ".txt")
        else:
            continue
        out_path.write_text(text, encoding="utf-8")
        print(f"Extracted: {path.name} -> {out_path.name} ({len(text)} chars)")


if __name__ == "__main__":
    main()

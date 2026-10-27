"""Extract text from docx (word/document.xml) to plain text."""
import zipfile
import xml.etree.ElementTree as ET
import re

DOCX_PATH = "02.01-Tietoevry-Bilag 2-Vedlegg-Leverandørens utfyllende svar til kravtabell.docx"
OUT_PATH = "RFP_Leverandørens_svar_utdrag.txt"

# Word XML namespaces
W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W_NS}

def get_text_from_element(elem):
    parts = []
    for t in elem.iter(f"{{{W_NS}}}t"):
        if t.text:
            parts.append(t.text)
        if t.tail:
            parts.append(t.tail)
    return "".join(parts)

def extract_paragraphs(root):
    for body in root.findall(".//w:body", NS):
        for p in body.findall("w:p", NS):
            texts = []
            for node in p.iter():
                if node.tag.endswith("}t") and node.text is not None:
                    texts.append(node.text)
                if node.tag.endswith("}tab"):
                    texts.append("\t")
            if texts:
                yield "".join(texts)

def main():
    with zipfile.ZipFile(DOCX_PATH, "r") as z:
        with z.open("word/document.xml") as f:
            tree = ET.parse(f)
    root = tree.getroot()
    lines = []
    for p in extract_paragraphs(root):
        line = p.strip()
        if line:
            lines.append(line)
    text = "\n".join(lines)
    # Collapse multiple newlines
    text = re.sub(r"\n{3,}", "\n\n", text)
    with open(OUT_PATH, "w", encoding="utf-8") as out:
        out.write(text)
    print(f"Wrote {len(text)} chars to {OUT_PATH}")

if __name__ == "__main__":
    main()

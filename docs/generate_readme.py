from pathlib import Path

docs_path = Path("docs/docs")

files = [
    ("Home", "index.md"),
    ("Installation", "installation.md"),
    ("Usage", "usage.md"),
    ("Tutorials", "tutorials.md"),
    ("Best Practices", "bestpractices.md"),
    ("Troubleshooting", "troubleshooting.md"),
    ("Contributing", "contributing.md"),
]

with open("./README.md", "w", encoding="utf-8") as out:
    out.write("# TidyDataCLI Documentation\n\n")

    out.write("## 📚 Table of Contents\n\n")
    for title, _ in files:
        anchor = title.lower().replace(" ", "-")
        out.write(f"- [{title}](#{anchor})\n")
    out.write("\n")

    for title, filename in files:
        md_file = docs_path / filename
        if md_file.exists():
            out.write(f"<details>\n<summary><strong>{title}</strong></summary>\n\n")
            content = md_file.read_text(encoding="utf-8")
            out.write(content.strip() + "\n")
            out.write("\n</details>\n\n")
        else:
            print(f"⚠️ File not found: {filename}")

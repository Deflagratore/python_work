from pathlib import Path

path = Path("text.txt")

contents = path.read_text()
print(contents)

righe = []

for riga in contents.splitlines():
    righe.append(riga)

print(righe)

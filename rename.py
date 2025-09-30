from pathlib import Path
p = Path(r"C:\Users\igrol\Downloads")
filename = "debilizm"

file = next(p.glob(filename + ".*"), None)

if file.exists() is True:
	file.rename(file.with_suffix(".py"))
    print(f"Renamed {file} to {file.stem}.txt")
else:
	print(None)


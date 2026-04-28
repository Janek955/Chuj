import matplotlib.pyplot as plt

def format_unit(unit):
    unit = unit.strip()

    replacements = {
        "dC": "°C",
        "dF": "°F",
        "Ohm": "Ω",
        "ohm": "Ω"
    }

    return replacements.get(unit, unit)

def format_prefix(prefix):
    prefix = prefix.strip()

    if prefix == "#":
        return ""  # brak prefiksu

    mapping = {
        "m": "m",
        "mili": "m",
        "u": "µ",
        "mikro": "µ",
        "k": "k",
        "kilo": "k",
        "M": "M",
        "mega": "M"
    }

    return mapping.get(prefix, prefix)

x = []
y = []

with open("data.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# metadane
title = lines[0].strip()
labels = lines[1].split()
units = lines[2].split()

prefixes = lines[3].split()
if len(prefixes) < 2:
    prefixes += ["#"] * (2 - len(prefixes))

x_unit = format_prefix(prefixes[0]) + format_unit(units[0])
y_unit = format_prefix(prefixes[1]) + format_unit(units[1])

# dane
for line in lines[4:]:
    parts = line.split()
    if len(parts) == 2:
        try:
            x.append(float(parts[0]))
            y.append(float(parts[1]))
        except ValueError:
            continue

x_label = f"{labels[0]} [{x_unit}]"
y_label = f"{labels[1]} [{y_unit}]"


# wykres
plt.plot(x, y, marker='o')
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.title(title)
plt.grid()

plt.show()


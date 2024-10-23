import math

triangles = {
    "Tr1": {"sides": "3 4 5"},
    "Tr2": {"sides": "6 8 10"},
    "Tr3": {"sides": "7 24 25"},
    "Tr4": {"sides": "10 15 20"},
    "Tr5": {"sides": "9 12 15"},
    "Tr6": {"sides": "5 12 13"}
    }

def cb (sides):
    a, b, c = map(float, sides.split())
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

for name, info in triangles.items():
    sides = info["sides"]
    area = cb (sides)
    info["area"] = area

triagles_max = max(triangles, key=lambda name: triangles[name]["area"])

print(f"Трикутник з найбільшою площею: {triagles_max}")

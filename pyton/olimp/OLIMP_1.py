n = int(input())
s = input().strip()
favorite_colors = set(s)

countries = []
for idx in range(n):
    parts = input().strip().split()
    name = parts[0]
    colors = parts[1]
    R = sum(1 for color in colors if color in favorite_colors)
    C = len(colors)
    countries.append((R, C, idx, name))

countries_sorted = sorted(countries, key=lambda x: (x[0], x[1]))

print(' '.join(country[3] for country in countries_sorted))

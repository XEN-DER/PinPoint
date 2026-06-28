with open('src/components/Map.astro', 'r', encoding='utf-8') as f:
    content = f.read()

# I will replace the leaflet map filter to invert the colors to make it look like a radar map.
content = content.replace(
    'filter: sepia(0.08) saturate(0.95) hue-rotate(5deg);',
    'filter: invert(1) hue-rotate(180deg) brightness(0.9) contrast(1.2) grayscale(0.2);'
)

with open('src/components/Map.astro', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated Map.astro filter')

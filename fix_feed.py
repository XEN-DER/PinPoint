with open('src/pages/feed.astro', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
skip = False
for i, line in enumerate(lines):
    if i >= 12 and i <= 21:
        continue
    if '<Map />' in line:
        new_lines.append('            <LeafletMap />\n')
    else:
        new_lines.append(line)

with open('src/pages/feed.astro', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
print('Fixed feed.astro')

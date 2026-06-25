import sys

with open('temp_index_copy.txt', 'r', encoding='utf-16') as f:
    lines = f.readlines()

def extract_section(section_id, out_file, title, subtitle):
    start = -1
    end = -1
    for i, line in enumerate(lines):
        if f'id="{section_id}"' in line:
            start = i
            break
            
    if start != -1:
        # Search FORWARDS for the corresponding </section>
        # We need to count <section> tags to handle nested sections if any, but in our case they are top-level
        depth = 0
        for i in range(start, len(lines)):
            if '<section' in lines[i]:
                depth += 1
            if '</section>' in lines[i]:
                depth -= 1
                if depth == 0:
                    end = i
                    break

    if start != -1 and end != -1:
        out = [
            '---\n',
            'import Layout from \'../layouts/Layout.astro\';\n'
        ]
        
        # If feed-section, import Map
        if section_id == 'feed-section':
            out.append('import Map from \'../components/Map.astro\';\n')
            
        out.extend([
            '---\n\n',
            f'<Layout title=\"{title} - Pinpoint\">\n',
            '  <div class=\"max-w-4xl mx-auto px-6 pt-12 pb-4 animate-toast-slide-up\">\n', # Use toast-slide-up or something else. I'll just remove the class to avoid collision
            f'    <h1 class=\"text-hero-display text-ink\">{title}</h1>\n',
            f'    <p class=\"text-body text-lg mt-2\">{subtitle}</p>\n',
            '  </div>\n'
        ])
        
        # Remove padding from the section so it fits in the layout cleanly
        for line in lines[start:end+1]:
            line = line.replace('py-20', 'py-8')
            out.append(line)
            
        out.append('</Layout>\n')
        
        with open(out_file, 'w', encoding='utf-8') as f:
            f.writelines(out)
        print(f'Created {out_file}')
    else:
        print(f'Failed to find {section_id}')

extract_section('gamification-section', 'src/pages/leaderboard.astro', 'Leaderboard', 'Earn points and rank up by reporting and verifying issues.')
extract_section('analytics-section', 'src/pages/impact.astro', 'Impact & Analytics', 'See the real-time difference we are making in the community.')
extract_section('feed-section', 'src/pages/feed.astro', 'Active Issues', 'Browse, verify, and resolve issues reported in your neighborhood.')
extract_section('hotspots-section', 'src/pages/hotspots.astro', 'Hotspots Map', 'Visualize problem areas and neighborhood clusters in real-time.')


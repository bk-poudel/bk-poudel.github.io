#!/usr/bin/env python3
import os
import re

# List of project files that might have the h1 issue
project_files = [
    "adaptable-phantom-prototype.html",
    "campus-plastic-waste-transformation.html", 
    "chicken-egg-incubator.html",
    "haptic_enabled_smart_goggles.html",
    "logistics_robot.html",
    "project-bioprinter.html",
    "real-time-embedded-systems.html",
    "roller-coaster-simulation.html",
    "throwing_a_ball.html"
]

projects_dir = "/home/bibek/Github_repositories/bk-poudel.github.io/projects"

def fix_h1_tag(filename):
    filepath = os.path.join(projects_dir, filename)
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and fix malformed h1 tags after close-button
        pattern = r'(\s*<a href="../index\.html#projects" class="close-button"[^>]*>\s*<i class="fas fa-times"></i>\s*</a>\s*)([^<]+)(</h1>)'
        
        def replacement(match):
            button_part = match.group(1)
            title_text = match.group(2).strip()
            h1_end = match.group(3)
            return f'{button_part}\n        <h1>{title_text}{h1_end}'
        
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed H1 tag in {filename}")
        else:
            print(f"No H1 issues found in {filename}")
        
    except Exception as e:
        print(f"Error processing {filename}: {e}")

def main():
    for filename in project_files:
        print(f"Checking {filename}...")
        fix_h1_tag(filename)

if __name__ == "__main__":
    main()

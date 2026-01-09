#!/usr/bin/env python3
import os
import re
# List of project files to update (excluding template.html and already processed files)
project_files = [
    "mppi_dynamic_object_tracking.html",
    "optimal_grasp_diffusion.html",
]
projects_dir = "/home/bibek/Github_repositories/bk-poudel.github.io/projects"
# CSS for the close button
close_button_css = """        .close-button {
            position: absolute;
            top: 1rem;
            right: 1rem;
            width: 40px;
            height: 40px;
            background: var(--primary);
            border: none;
            border-radius: 50%;
            color: white;
            font-size: 1.2rem;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s ease;
            z-index: 10;
            text-decoration: none;
            box-shadow: 0 2px 10px rgba(0,0,0,0.2);
        }
        .close-button:hover {
            background: var(--accent);
            transform: scale(1.1);
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
            color: white;
            text-decoration: none;
        }
        .close-button:active {
            transform: scale(0.95);
        }"""
# HTML for the close button
close_button_html = """        <a href="../index.html#projects" class="close-button" title="Back to Projects">
            <i class="fas fa-times"></i>
        </a>"""
def update_project_file(filename):
    filepath = os.path.join(projects_dir, filename)
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        # Add CSS after .project-content::before block
        css_pattern = r"(\s*\.project-content::before\s*\{[^}]*\})"
        css_replacement = r"\1" + "\n" + close_button_css
        if re.search(css_pattern, content, re.DOTALL):
            content = re.sub(
                css_pattern, css_replacement, content, count=1, flags=re.DOTALL
            )
            print(f"Added CSS to {filename}")
        else:
            print(f"Warning: Could not find .project-content::before in {filename}")
        # Add HTML button after <div class="project-content">
        html_pattern = r'(\s*<div class="project-content">\s*)(<h1>)'
        html_replacement = r"\1" + close_button_html + "\n        \2"
        if re.search(html_pattern, content):
            content = re.sub(html_pattern, html_replacement, content, count=1)
            print(f"Added HTML button to {filename}")
        else:
            print(
                f'Warning: Could not find <div class="project-content"> pattern in {filename}'
            )
        # Write back to file
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Successfully updated {filename}")
    except Exception as e:
        print(f"Error updating {filename}: {e}")
def main():
    for filename in project_files:
        print(f"\nProcessing {filename}...")
        update_project_file(filename)
if __name__ == "__main__":
    main()

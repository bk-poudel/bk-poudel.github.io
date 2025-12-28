import os
import re

folders = [
    "autonomous_navigation",
    "Behavior_Cloning_Lunar_Lander",
    "Bio-Printer_Images",
    "classic_controllers",
    "FAMS",
    "miscellenous-images",
    "Pick_and_Place",
    "Plastic_Waste_Images",
    "Robot_Navigation",
    "Roller_Coaster_Simulation",
    "Smart_googles",
    "throwing_a_ball",
    "value_iteration",
    "z1_arm"
]

def update_file(filepath, is_project_file):
    with open(filepath, 'r') as f:
        content = f.read()
    
    original_content = content
    
    for folder in folders:
        # Regex to match src="...folder/..." or href="...folder/..."
        # We want to capture the prefix (src=" or src="./ or src="../)
        
        if is_project_file:
            # In projects/ folder, we expect ../FOLDER or ../../FOLDER
            # We want to replace ../FOLDER with ../assets/project_images/FOLDER
            
            # Case 1: ../FOLDER
            pattern = r'(src|href)=([\"\'])\.\./' + re.escape(folder) + r'/'
            replacement = r'\1=\2../assets/project_images/' + folder + '/'
            content = re.sub(pattern, replacement, content)
            
            # Case 2: ../../FOLDER (just in case)
            pattern = r'(src|href)=([\"\'])\.\./\.\./' + re.escape(folder) + r'/'
            replacement = r'\1=\2../../assets/project_images/' + folder + '/'
            content = re.sub(pattern, replacement, content)

        else:
            # In root index.html
            # We expect FOLDER or ./FOLDER or even ../FOLDER (which was likely a bug but we fix it)
            
            # Case 1: FOLDER/
            pattern = r'(src|href)=([\"\'])' + re.escape(folder) + r'/'
            replacement = r'\1=\2assets/project_images/' + folder + '/'
            content = re.sub(pattern, replacement, content)
            
            # Case 2: ./FOLDER/
            pattern = r'(src|href)=([\"\'])\./' + re.escape(folder) + r'/'
            replacement = r'\1=\2assets/project_images/' + folder + '/'
            content = re.sub(pattern, replacement, content)
            
            # Case 3: ../FOLDER/ (Fixing the bug in index.html)
            pattern = r'(src|href)=([\"\'])\.\./' + re.escape(folder) + r'/'
            replacement = r'\1=\2assets/project_images/' + folder + '/'
            content = re.sub(pattern, replacement, content)

    if content != original_content:
        print(f"Updating {filepath}")
        with open(filepath, 'w') as f:
            f.write(content)

# Update index.html
if os.path.exists("index.html"):
    update_file("index.html", is_project_file=False)

# Update projects/*.html
if os.path.exists("projects"):
    for filename in os.listdir("projects"):
        if filename.endswith(".html"):
            update_file(os.path.join("projects", filename), is_project_file=True)

print("Done updating references.")

import os
import shutil

# ============================================================
# EDIT THIS PATH - Replace with your main folder path
# ============================================================
# Windows example: r"C:\Users\YourName\Downloads\Palo Alto Cybersecurity Foundation Notes"
# Mac/Linux example: "/Users/YourName/Downloads/Palo Alto Cybersecurity Foundation Notes"

project_root = r"C:\Users\MAYUR\Downloads\Palo Alto Cybersecurity Foundation Notes"

# ============================================================

# Module folder names
modules = {
    "Module_1_Cyber-Landscape": 1,
    "Module_2_Cyber-Threats": 2,
    "Module_3_Cyberattack_Types": 3,
    "Module_4_Security_Models": 4,
    "Module_5_AI_in_Cybersecurity": 5,
    "Module_6_Security_Operating_Platform": 6,
}

print("\n" + "="*70)
print("🚀 ORGANIZING NOTION EXPORTS FOR GITHUB")
print("="*70)

# Check if path exists
if not os.path.exists(project_root):
    print(f"\n❌ ERROR: Folder not found!")
    print(f"Path: {project_root}")
    print("\nPlease check your folder path and try again.")
    exit()

print(f"\n✅ Found project folder: {project_root}\n")

# Process each module
for module_folder, module_num in modules.items():
    module_path = os.path.join(project_root, module_folder)
    
    # Check if module folder exists
    if not os.path.exists(module_path):
        print(f"⚠️  SKIP: {module_folder} (folder not found)")
        continue
    
    print(f"\n{'='*70}")
    print(f"📁 PROCESSING: {module_folder}")
    print(f"{'='*70}")
    
    # Get all items in module folder
    items = os.listdir(module_path)
    extracted_count = 0
    renamed_count = 0
    
    # STEP 1: Extract .md files from subfolders
    print("\n[STEP 1] Extracting files from subfolders...")
    
    for item in items:
        item_path = os.path.join(module_path, item)
        
        # If it's a folder
        if os.path.isdir(item_path):
            print(f"  📂 Found folder: {item}")
            
            # Find .md files inside
            for file in os.listdir(item_path):
                if file.endswith('.md'):
                    src = os.path.join(item_path, file)
                    # Replace spaces with underscores
                    new_name = file.replace(' ', '_')
                    dst = os.path.join(module_path, new_name)
                    
                    # Copy file up to module root
                    shutil.copy(src, dst)
                    print(f"    ✅ Extracted: {file} → {new_name}")
                    extracted_count += 1
            
            # Delete empty folder
            shutil.rmtree(item_path)
            print(f"    🗑️  Deleted empty folder")
    
    if extracted_count == 0:
        print("  (No subfolders found)")
    
    # STEP 2: Rename all files (spaces to underscores)
    print("\n[STEP 2] Renaming all .md files...")
    
    for file in os.listdir(module_path):
        if file.endswith('.md'):
            old_path = os.path.join(module_path, file)
            
            # Check if it's the module INDEX file
            if 'Module' in file and not file.startswith('Topic'):
                # Rename to INDEX.md
                new_name = 'INDEX.md'
                new_path = os.path.join(module_path, new_name)
                
                if old_path != new_path:
                    try:
                        os.rename(old_path, new_path)
                        print(f"  ✅ {file} → INDEX.md")
                        renamed_count += 1
                    except Exception as e:
                        print(f"  ❌ Error renaming {file}: {e}")
            
            # Rename topic files (spaces to underscores)
            elif 'Topic' in file:
                new_name = file.replace(' ', '_')
                new_path = os.path.join(module_path, new_name)
                
                if old_path != new_path:
                    try:
                        os.rename(old_path, new_path)
                        print(f"  ✅ {file} → {new_name}")
                        renamed_count += 1
                    except Exception as e:
                        print(f"  ❌ Error renaming {file}: {e}")
    
    if renamed_count == 0:
        print("  (All files already properly named)")
    
    # STEP 3: Show final structure
    print(f"\n[STEP 3] Final file structure:")
    
    final_files = sorted([f for f in os.listdir(module_path) if f.endswith('.md')])
    
    if len(final_files) == 0:
        print("  (No markdown files found)")
    else:
        for i, file in enumerate(final_files, 1):
            print(f"    {i}. {file}")
    
    print(f"\n✅ {module_folder} COMPLETE!")
    print(f"   Extracted: {extracted_count} files")
    print(f"   Renamed: {renamed_count} files")

print("\n" + "="*70)
print("✨ ALL MODULES ORGANIZED SUCCESSFULLY!")
print("="*70)

print("\n📝 NEXT STEPS:")
print("   1. ✅ Verify each module folder (check files look good)")
print("   2. ✅ Add README.md to root folder")
print("   3. ✅ Create GitHub repository")
print("   4. ✅ Upload to GitHub")

print("\n" + "="*70)
print("Ready to upload to GitHub! 🚀\n")

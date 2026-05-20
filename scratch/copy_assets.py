import os
import shutil

src_dir = "/Users/i2carvajal/Documents/Proyectos/CopperWeb/web completa/Copper Giant - High-Quality Copper Deposits in the Americas4_files"
dest_dir = "/Users/i2carvajal/Documents/Proyectos/CopperWeb/assets"

os.makedirs(dest_dir, exist_ok=True)
os.makedirs(os.path.join(dest_dir, "coreshack"), exist_ok=True)
os.makedirs(os.path.join(dest_dir, "gallery"), exist_ok=True)
os.makedirs(os.path.join(dest_dir, "videos"), exist_ok=True)

# Copy files
for file_name in os.listdir(src_dir):
    src_file = os.path.join(src_dir, file_name)
    if not os.path.isfile(src_file):
        continue
        
    if file_name.startswith("copper-giant-the-coreshack-") and file_name.endswith(".webp"):
        shutil.copy2(src_file, os.path.join(dest_dir, "coreshack", file_name))
    elif file_name.startswith("gallery-") and file_name.endswith(".jpg"):
        shutil.copy2(src_file, os.path.join(dest_dir, "gallery", file_name))
    elif file_name.startswith("hqdefault") and file_name.endswith(".jpg"):
        shutil.copy2(src_file, os.path.join(dest_dir, "videos", file_name))
    elif file_name.startswith("copper-giant-mocoa-") and file_name.endswith(".jpg"):
        shutil.copy2(src_file, os.path.join(dest_dir, file_name))

print("Assets copied successfully!")

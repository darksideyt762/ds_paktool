import os
import zipfile

# Paths
BASE_DIR = os.path.expanduser("~/ds_paktool")
PAKS_DIR = os.path.join(BASE_DIR, "PAKS")
UNPACK_DIR = os.path.join(BASE_DIR, "UNPACK")

def setup_directories():
    """Setup the folder structure for ds_paktool."""
    os.makedirs(PAKS_DIR, exist_ok=True)
    os.makedirs(UNPACK_DIR, exist_ok=True)
    print(f"Folder structure created at {BASE_DIR}")
    print(f"Place your .pak files in the PAKS folder.")

def unpack_pak(pak_file, output_dir):
    """Unpack a .pak file."""
    pak_name = os.path.splitext(os.path.basename(pak_file))[0]
    pak_output_dir = os.path.join(output_dir, pak_name)

    # Subdirectories for the unpacked .pak file
    unpack_subdir = os.path.join(pak_output_dir, "unpack")
    repack_subdir = os.path.join(pak_output_dir, "repack")
    results_subdir = os.path.join(pak_output_dir, "results")

    os.makedirs(unpack_subdir, exist_ok=True)
    os.makedirs(repack_subdir, exist_ok=True)
    os.makedirs(results_subdir, exist_ok=True)

    try:
        with zipfile.ZipFile(pak_file, 'r') as zip_ref:
            zip_ref.extractall(unpack_subdir)
        print(f"Unpacked '{pak_file}' successfully to '{unpack_subdir}'.")
    except Exception as e:
        print(f"Error unpacking {pak_file}: {e}")

if __name__ == "__main__":
    setup_directories()

    pak_files = [f for f in os.listdir(PAKS_DIR) if f.endswith(".pak")]
    if not pak_files:
        print(f"No .pak files found in {PAKS_DIR}.")
    else:
        for pak_file in pak_files:
            unpack_pak(os.path.join(PAKS_DIR, pak_file), UNPACK_DIR)
        print(f"All .pak files have been processed.")
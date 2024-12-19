import os

# Paths for the directories
BASE_DIR = os.path.expanduser("~/ds_paktool")  # The base folder where the tool will be placed
PAKS_DIR = os.path.join(BASE_DIR, "PAKS")  # Folder where users will put their .pak files
UNPACK_DIR = os.path.join(BASE_DIR, "UNPACK")  # Folder for unpacked files

def setup_directories():
    """Create necessary directories if they don't exist."""
    try:
        # Create the base folder and subfolders
        os.makedirs(PAKS_DIR, exist_ok=True)
        os.makedirs(UNPACK_DIR, exist_ok=True)
        print(f"Folders created at: {BASE_DIR}")
        print("Place your .pak files in the PAKS folder.")
    except Exception as e:
        print(f"Error creating directories: {e}")

def unpack_pak(pak_file, output_dir):
    """Unpack the .pak file into the designated directory."""
    pak_name = os.path.splitext(os.path.basename(pak_file))[0]  # Extract filename without extension
    pak_output_dir = os.path.join(output_dir, pak_name)

    # Subdirectories for unpacking the .pak file
    unpack_subdir = os.path.join(pak_output_dir, "unpack")
    repack_subdir = os.path.join(pak_output_dir, "repack")
    results_subdir = os.path.join(pak_output_dir, "results")

    try:
        # Create subdirectories if they don't exist
        os.makedirs(unpack_subdir, exist_ok=True)
        os.makedirs(repack_subdir, exist_ok=True)
        os.makedirs(results_subdir, exist_ok=True)

        # Simulating unpacking (For demo purposes, we will just create a text file in 'unpack' folder)
        with open(os.path.join(unpack_subdir, "example_unpacked.txt"), 'w') as f:
            f.write("This is an unpacked file.")

        print(f"Unpacked '{pak_file}' into '{unpack_subdir}'")
    except Exception as e:
        print(f"Error unpacking {pak_file}: {e}")

if __name__ == "__main__":
    # Setup folder structure
    setup_directories()

    # Simulate processing .pak files (for now, we’ll assume a pak file exists in PAKS folder)
    pak_files = [f for f in os.listdir(PAKS_DIR) if f.endswith(".pak")]
    if not pak_files:
        print("No .pak files found in the PAKS folder.")
    else:
        for pak_file in pak_files:
            unpack_pak(os.path.join(PAKS_DIR, pak_file), UNPACK_DIR)
        print("All .pak files have been processed.")

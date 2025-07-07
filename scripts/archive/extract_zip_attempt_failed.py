# NOTE: This script was an initial approach to ZIP extraction
# Didn't work due to encoding/path issues — preserved for future testing

import zipfile
from pathlib import Path

# Paths
source_folder = Path(
    r"\\wsl$\Ubuntu\home\cleavertbt\1DataProjects\HealthcareProject\data\raw_zips\marketplace_pufs_zips")
destination_folder = Path(
    r"\\wsl$\Ubuntu\home\cleavertbt\1DataProjects\HealthcareProject\data\marketplace_pufs")

# Make sure destination exists
destination_folder.mkdir(parents=True, exist_ok=True)

# Process each .zip file
for zip_file in source_folder.glob("*.zip"):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        for member in zip_ref.namelist():
            if member.endswith(".csv"):
                # Save the file using just its base name
                target_path = destination_folder / Path(member).name

                # Avoid overwriting if it already exists
                if not target_path.exists():
                    with zip_ref.open(member) as source, open(target_path, 'wb') as target:
                        target.write(source.read())
                    print(f"✅ Extracted: {target_path.name}")
                else:
                    print(f"⚠️ Skipped (already exists): {target_path.name}")

print("\n✅ All available CSVs from ZIPs have been extracted.")

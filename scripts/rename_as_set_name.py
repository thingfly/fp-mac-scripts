import os
import pathlib
import clipboard as c

artwork_files_location = "../run/artwork-files"

if not os.path.exists(artwork_files_location):
    os.mkdir(artwork_files_location)

set_names = c.paste().split()
artwork_files = os.listdir(artwork_files_location)

print("The following files will be renamed:")

for artwork_file in artwork_files:
    file_name = pathlib.Path(artwork_file).stem
    file_extension = pathlib.Path(artwork_file).suffix

    for set_name in set_names:
        if file_name in set_name:
            new_name = f"{set_name}{file_extension}"
            print(f"  {artwork_file} -> {new_name}")
            os.rename(f"{artwork_files_location}/{artwork_file}", f"{artwork_files_location}/{new_name}")
            break

print()
print("Finished")
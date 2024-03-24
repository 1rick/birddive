import os
import shutil

def copy_static(src_dir, dest_dir):
    # Check if source directory exists
    if not os.path.exists(src_dir):
        print(f"Source directory {src_dir} does not exist. Exiting.")
        return

    # Create destination directory if it does not exist
    os.makedirs(dest_dir, exist_ok=True)

    # Copy each item from src_dir to dest_dir
    for item in os.listdir(src_dir):
        s = os.path.join(src_dir, item)
        d = os.path.join(dest_dir, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)

    print(f"Static content copied from {src_dir} to {dest_dir}.")

def copy_cname(src_dir, dest_dir):
    cname_file = 'CNAME'
    src_cname_path = os.path.join(src_dir, cname_file)

    if os.path.exists(src_cname_path):
        shutil.copy2(src_cname_path, dest_dir)
        print(f"{cname_file} file copied from {src_dir} to {dest_dir}.")
    else:
        print(f"{cname_file} file does not exist in {src_dir}.")

if __name__ == '__main__':
    input_static_dir = 'input/static'
    output_static_dir = 'output/static'
    root_output_dir = 'output'

    copy_static(input_static_dir, output_static_dir)
    copy_cname('input', root_output_dir)  # Assumes CNAME is in the 'input' directory

import os
import shutil

from copystatic import copy_files_recursive
from generate import generate_pages_recursive

import os
import shutil


dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main():
	print(f"Deleting the public directory ({dir_path_public})...")
	if os.path.exists(dir_path_public):
		shutil.rmtree(dir_path_public)
	print("\n")

	print(f"Copying static files to public directory...")
	copy_files_recursive(dir_path_static, dir_path_public)
	print("\n")

	print(f"Generating pages (using {template_path})...")
	generate_pages_recursive(
		os.path.join(dir_path_content),
		template_path,
		os.path.join(dir_path_public),
	)
	print("\n")


main()

import os

from block_markdown import (
	markdown_to_html_node,
	extract_title
)


def generate_page(from_path, template_path, dest_path):
	"""
	1. Print a message like "Generating page from from_path to dest_path using template_path".
	2. Read the markdown file at from_path and store the contents in a variable.
	3. Read the template file at template_path and store the contents in a variable.
	4. Use your markdown_to_html_node function and .to_html() method to convert the markdown file to an HTML string.
	5. Use the extract_title function to grab the title of the page.
	6. Replace the {{ Title }} and {{ Content }} placeholders in the template with the HTML and title you generated.
	7. Write the new full HTML page to a file at dest_path. Be sure to create any necessary directories if they don't exist.
	"""
	print(f"Generating page from {from_path} to {dest_path} using {template_path}")

	with open(template_path) as template_file:
		template_content = template_file.read()
	
	with open(from_path) as markdown_file:
		markdown_content = markdown_file.read()

	html_node = markdown_to_html_node(markdown_content)
	html_content = html_node.to_html()

	title = extract_title(markdown_content)

	final_html_content = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

	dest_dir_path = os.path.dirname(dest_path)
	if not os.path.exists(dest_dir_path):
		os.mkdir(dest_dir_path)

	with open(dest_path, 'w') as dest:
		dest.write(final_html_content)

from textnode import TextType, TextNode


def main():
	node = TextNode("Hello, world!", TextType.BOLD, "https://google.com")
	print(node)


main()

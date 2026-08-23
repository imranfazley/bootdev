# def get_book_text(path):
# 	with open(path) as f:
# 		file_contents = f.read()
# 	# print(file_contents)
# 	word_count = file_contents.split()
# 	print(f"Found {len(word_count)} total words")

from stats import get_num_words

def main():
	get_num_words("./books/frankenstein.txt")

main()

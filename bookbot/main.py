import sys
from stats import get_num_words, get_character_count, chars_dict_to_sorted_list

def get_book_text(path):
	with open(path) as f:
		file_contents = f.read()
	return file_contents

def print_report(path,word_count,sorted_result):
	print('============ BOOKBOT ============')
	print('Analyzing book found at', path)
	print('----------- Word Count ----------')
	print(word_count)
	print('--------- Character Count -------')
	for x in sorted_result:
		if x[0].isalpha():
			print(f'{x[0]}: {x[1]}')
	print('============= END ===============')

def main():
	# file_path = "./books/frankenstein.txt"
	if len(sys.argv) < 2:
		print('Usage: python3 main.py <path_to_book>')
		sys.exit(1)
	file_path = sys.argv[1]
	file_contents = get_book_text(file_path)
	# get_num_words(file_contents)
	wcount = get_num_words(file_contents)
	sorted_result = chars_dict_to_sorted_list(file_contents)
	print_report(file_path,wcount,sorted_result)
	
main()
# print("greetings boots")
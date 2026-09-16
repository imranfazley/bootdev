def get_num_words(text_file):
	# with open(path) as f:
	# 	file_contents = f.read()
	# print(file_contents)
	word_count = text_file.split()
	return (f"Found {len(word_count)} total words")

def get_character_count(text_file):
	# with open(path) as f:
	# 	file_contents = f.read()
	lowered = text_file.lower()

	char_count = {}
	for x in lowered:
		if x in char_count:
			char_count[x] += 1
		else:
			char_count[x] = 1
	# print(char_count)
	return char_count

def sort_on(character: tuple[str,int] ) -> int:
	return character[1]

def chars_dict_to_sorted_list(text_file):
	dictionary = get_character_count(text_file)
	# convert dictionary to tuple
	tuple_to_sort = dictionary.items()
	sorted_list = []
	sorted_list= sorted(tuple_to_sort, reverse=True, key=sort_on)
	# print(sorted_list)
	return sorted_list
def get_num_words(path):
	with open(path) as f:
		file_contents = f.read()
	# print(file_contents)
	word_count = file_contents.split()
	print(f"Found {len(word_count)} total words")
def main():
	msg = input().split()
	final = []
	
	for text in msg:
		final += [text[1::2]]

	print(" ".join(final))

main()
input_file = "words.txt"
output_file = "ocr.txt"
search_str = "ocr"

with open(input_file, "r") as f:
    words = f.read().splitlines()

matches = [word for word in words if search_str in word]

with open(output_file, "w") as f:
    for word in matches:
        f.write(word + "\n")

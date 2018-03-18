def curse(file):
    file = open(file)
    file_lines = file.readline()

    curse_list = ["fuck", "shit", "ass", "bitch"]

    for text in file_lines:
        text_list = [x.lower() for x in text.split(" ")]

        for i, word in enumerate(text_list):
            if word in curse_list:
                print("Oh no curse word here!")
                return True

        return False

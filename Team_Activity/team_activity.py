with open("books_and_chapters.txt") as kb_file:
    user_choice = input("From which volume of scriptures would you like to learn about? (Old Testament, New Testament, Book of Mormon, Doctrine and Covenants, Pearl of Great Price) ")

    largest_so_far = -1
    largest_book = ""

    for line in kb_file:
        line = line.strip()
        parts = line.split(":")

        book = parts[0]
        chapter = int(parts[1])
        scripture = parts[2]

        if scripture.lower() == user_choice.lower():
            print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapter}")

            if chapter > largest_so_far:
                largest_so_far = chapter
                largest_book = book


print(f"The book with the most chapters in the {user_choice} is: {largest_book}")
print(f"It has {largest_so_far} chapters.")
import nltk

def split_book(book, paragraph_max_words = 1024):
    book_paragraphs = []

    # Split the content into sentences
    sentences = nltk.sent_tokenize(book)

    # Delete sentences that contains stop words
    stop_words = ["Copyright", "Table Of Contents", "title Page", "All rights reserved", "www.", ".org", "@", "e-books", "®", "ISBN:", "©",".com "]
    deleted_sentences = []

    # Loop through all the sentences
    for j in range(len(sentences)):
        # Check if the sentence is a table of content
        words = nltk.word_tokenize(sentences[j])
        chapter_counter = sum(1 for word in words if word.lower() == "chapter")
        stave_counter = sum(1 for word in words if word.lower() == "stave")
        part_counter = sum(1 for word in words if word.lower() == "part")
        digits_counter = sum(1 for word in words if word in ["three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven"])
        number_counter = sum(1 for word in words if word in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"])
        romanian_counter = sum(1 for word in words if word in ["II", "III", "IV", "VI", "VII", "XII"])

        # Delete the sentence if it is a table of content
        if chapter_counter > 3 or stave_counter > 3 or part_counter > 8 or digits_counter > 10 or number_counter > 10 or romanian_counter > 6:
            deleted_sentences.append(j)

        # Delete the sentence if it contains stop words
        for i in range(len(stop_words)):
            if stop_words[i].lower() in sentences[j].lower() and j not in deleted_sentences:
                deleted_sentences.append(j)

    # Delete sentences from the end to the beginning
    for i in range(len(deleted_sentences)):
        del sentences[deleted_sentences[len(deleted_sentences) - (i + 1)]]


    # Iterate through each sentence
    current_paragraph = []
    for sentence in sentences:
        words = sentence.split()
        # Check if adding the current sentence exceeds the word limit
        if len(current_paragraph) + len(words) <= paragraph_max_words:
            current_paragraph.extend(words)
        else:
            # Add the paragraph to array of paragraphs
            ready_paragraph = ' '.join(current_paragraph)
            book_paragraphs.append(ready_paragraph)
            # Reset current paragraph
            current_paragraph = words

    # Check if there is a last paragraph that hasn't been added
    if current_paragraph:
        # Add the paragraph to array of paragraphs
        ready_paragraph = ' '.join(current_paragraph)
        book_paragraphs.append(ready_paragraph)

    print("\nThe book has been splited successfully !!\n")
    return book_paragraphs

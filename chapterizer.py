import os
import nltk

def chapterize_book(book_path, max_words_per_chunk = 1024):
    # Read the content of the book from the file
    with open(book_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split the content into sentences
    sentences = nltk.sent_tokenize(content)
    
    print("length of sentences before deletion : ", len(sentences))

    # Delete paragraphs that contains stop words
    stop_words = ["Copyright", "Table Of Contents", "title Page", "All rights reserved", "www.", ".com ", "@", "e-books"]

    deleted_paragraphs = []
    for j in range(len(sentences)):
        for i in range(len(stop_words)):
            if stop_words[i].lower() in sentences[j].lower() and j not in deleted_paragraphs:
                #print("------------------------------------------------------------------------------------------")
                #print("Deleted sentence : ")
                #print("################################################################")
                #print(sentences[j])
                #print("################################################################")
                #print("It's Stop word : ")
                #print(stop_words[i])
                #print("------------------------------------------------------------------------------------------")
                deleted_paragraphs.append(j)

    for i in range(len(deleted_paragraphs)):
        del sentences[deleted_paragraphs[i]]

    print("length of sentences after deletion : ", len(sentences))

    #print('')
    #print('First 25 paragraph: ')
    #print('')
    #for i in range (15):
    #    print(sentences[len(sentences) - (15 - i)])
    #    print('------------------------------------------------')

    # Initialize variables
    current_chunk = []
    chunk_count = 0
    book_name = os.path.splitext(os.path.basename(book_path))[0]
    output_folder = book_name + " chunks"

    # Create a new folder to store the chunks
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through each sentence
    for sentence in sentences:
        words = sentence.split()
        # Check if adding the current sentence exceeds the word limit
        if len(current_chunk) + len(words) <= max_words_per_chunk:
            current_chunk.extend(words)
        else:
            # Save the current chunk as a separate text file
            chunk_count += 1
            chunk_filename = os.path.join(output_folder, f"{chunk_count}.txt")
            with open(chunk_filename, 'w') as f:
                f.write(' '.join(current_chunk))
            # Reset current chunk
            current_chunk = words

    # Save the last chunk as a separate text file
    if current_chunk:
        chunk_count += 1
        chunk_filename = os.path.join(output_folder, f"{chunk_count}.txt")
        with open(chunk_filename, 'w') as f:
            f.write(' '.join(current_chunk))

    print("Book has been split successfully !!")


book = r"D:\Gethub\SummaryFlow\TextNovels\Wizard and Glass.txt"
chapterize_book(book)

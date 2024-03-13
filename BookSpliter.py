import glob
import os
import nltk

no_content_table = 0

def split_book(book_path, paragraph_max_words = 512):
    print("Max size of paragraph is ", paragraph_max_words)
    book_paragraphs = []
    # Read the content of the book from the file
    with open(book_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split the content into sentences
    sentences = nltk.sent_tokenize(content)
    
    #print("length of sentences before deletion : ", len(sentences))

    # Delete first & last sentence
    del sentences[0]
    del sentences[len(sentences) - 1]

    # Delete sentences that contains stop words
    stop_words = ["Copyright", "Table Of Contents", "title Page", "All rights reserved", "www.", ".org", "@", "e-books", "®", "ISBN:", "©",".com "]
    hasContenttable = False
    deleted_sentences = []
    for j in range(len(sentences)):

        # Check if it is the table of content
        words = nltk.word_tokenize(sentences[j])
        chapter_counter = sum(1 for word in words if word.lower() == "chapter")
        stave_counter = sum(1 for word in words if word.lower() == "stave")
        part_counter = sum(1 for word in words if word.lower() == "part")
        digits_counter = sum(1 for word in words if word in ["three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven"])
        number_counter = sum(1 for word in words if word in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"])
        romanian_counter = sum(1 for word in words if word in ["II", "III", "IV", "VI", "VII", "XII"])

        if chapter_counter > 3 or stave_counter > 3 or part_counter > 8 or digits_counter > 10 or number_counter > 10 or romanian_counter > 6:
            deleted_sentences.append(j)
            hasContenttable = True
            #print("------------------------------------------------------------------------------------------")
            #print("Book Name: ", os.path.splitext(os.path.basename(book_path))[0])
            #print("Deleted sentence : ")
            #print()
            #print(sentences[j])
            #print()
            #print("It's Table Of Contens")
            #print("------------------------------------------------------------------------------------------")

            # Create the table_contents folder if it doesn't exist
            #table_contents_path = "D:\\Gethub\\SummaryFlow\\TableContent"
            #os.makedirs(table_contents_path, exist_ok=True)

            # Write the sentence to a text file
            #output_filename = os.path.join(table_contents_path, os.path.splitext(os.path.basename(book_path))[0] + ".txt")
            #with open(output_filename, 'a', encoding='utf-8') as output_file:
            #    output_file.write(sentences[j] + "\n")

        for i in range(len(stop_words)):
            if stop_words[i].lower() in sentences[j].lower() and j not in deleted_sentences:
                deleted_sentences.append(j)
                #print("------------------------------------------------------------------------------------------")
                #print("Deleted sentence : ")
                #print("################################################################")
                #print(sentences[j])
                #print("################################################################")
                #print("It's Stop word : ")
                #print(stop_words[i])
                #print("------------------------------------------------------------------------------------------")

    # Calculate number of books that has no content table
    global no_content_table
    if hasContenttable == False:
        no_content_table += 1
        #print("------------------------------------------------------------------------------------------")
        #print("Book Name:  (", os.path.splitext(os.path.basename(book_path))[0], ")  Does not has Table Of Content")

    # Delete sentences from the end to the beginning
    for i in range(len(deleted_sentences)):
        del sentences[deleted_sentences[len(deleted_sentences) - (i + 1)]]


    #print("length of sentences after deletion : ", len(sentences))

    # Initialize variables
    current_paragraph = []
    paragraph_count = 0
    book_name = os.path.splitext(os.path.basename(book_path))[0]
    output_path = "D:\\Gethub\\SummaryFlow\\SplitedNovels\\"
    output_folder = output_path + book_name + " paragraphs"

    # Create a new folder to store the paragraph
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through each sentence
    for sentence in sentences:
        words = sentence.split()
        # Check if adding the current sentence exceeds the word limit
        if len(current_paragraph) + len(words) <= paragraph_max_words:
            current_paragraph.extend(words)
        else:
            # Save the current paragraph as a separate text file
            paragraph_count += 1
            paragraph_filename = os.path.join(output_folder, f"{paragraph_count}.txt")
            with open(paragraph_filename, 'w', encoding='utf-8') as f:
                f.write(' '.join(current_paragraph))
            
            # Add the paragraph to array of paragraphs
            ready_paragraph = ' '.join(current_paragraph)
            book_paragraphs.append(ready_paragraph)
            # Reset current paragraph
            current_paragraph = words

    # Save the last paragraph as a separate text file
    if current_paragraph:
        paragraph_count += 1
        paragraph_filename = os.path.join(output_folder, f"{paragraph_count}.txt")
        with open(paragraph_filename, 'w', encoding='utf-8') as f:
            f.write(' '.join(current_paragraph))
        
        # Add the paragraph to array of paragraphs
        ready_paragraph = ' '.join(current_paragraph)
        book_paragraphs.append(ready_paragraph)

    print(book_name, " splited successfully !!")
    return book_paragraphs


#book = r"D:\Gethub\SummaryFlow\WholeNovels\animal_farm.txt"
#book_splits = split_book(book)
#print ("Number of paragraphs is ", len(book_splits))
#print (book_splits[0])

# Define the folder containing the text files
#folder_path = r"D:\Gethub\SummaryFlow\WholeNovels"

# Loop through all the text files in the folder
#for file_path in glob.glob(os.path.join(folder_path, "*.txt")):
    # Pass each file's path to the process_file function
#    split_book(file_path)
#print("Number of books without content table is ", no_content_table)
#print("Number of books with content table is ", (284 - no_content_table))
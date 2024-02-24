import os
import pandas as pd
import shutil

summaries_folder = r"D:\Gethub\SummaryFlow\All_summaries"
input_folder = r"D:\Gethub\SummaryFlow\All_novels"
wrong_names_folder = r"D:\Gethub\SummaryFlow\Wrong_names"

df = pd.read_excel('D:\Gethub\SummaryFlow\BookSummariesDataset.xlsx')


## Rename text files with correct form
## Iterate through the PDFs in the input folder
#for txt_filename in os.listdir(input_folder):
    ## Split the string based on the delimiter "_-_"
    #parts = txt_filename.split("_-_")
    ## Get the first part (before "_-_")
    #result = parts[0]
    ## Replace "_" with whitespace
    #result = result.replace("_", " ")
    ## Get the original path and the new path for the renamed file
    #original_path = os.path.join(input_folder, txt_filename)
    #new_filename = result + ".txt"
    #new_path = os.path.join(input_folder, new_filename)
    ## Rename the file
    #os.rename(original_path, new_path)

# Iterate through the books in the input folder
for txt_filename in os.listdir(input_folder):
    # Get the filename without extension
    txt_filename_no_ext = os.path.splitext(txt_filename)[0]
    flag = False
    # Iterate through the first 800 rows
    for index, row in df.head(800).iterrows():
        if txt_filename_no_ext == row['Book title']:
            summary_filename = txt_filename
            summary_path = os.path.join(summaries_folder, summary_filename)
            # Check if the summary file already exists in the output folder to avoid duplicates
            if not os.path.exists(summary_path):
                with open(summary_path, 'a', encoding='utf-8') as file:
                    file.write(row['Plot summary'])
                    print(f"{txt_filename_no_ext} || Successfully saved !")
            flag = True
            break
    # Check if the book named wrong
    if flag == False:
        # Move the book to wrong names folder
        worng_named_book = os.path.join(input_folder, txt_filename)
        shutil.move(worng_named_book, wrong_names_folder)
print("------------------------------------------------------------------")
print("Processing Completed Successfully!!")
print("------------------------------------------------------------------")
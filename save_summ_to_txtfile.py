import os
import pandas as pd


summaries_folder = r"D:\Gethub\SummaryFlow\All_summaries"
input_folder = r"D:\Gethub\SummaryFlow\All_novels_textfiles"
# Create the output folder if it doesn't exist
if not os.path.exists(summaries_folder):
    os.makedirs(summaries_folder)


df = pd.read_excel('D:\Gethub\SummaryFlow\BookSummariesDataset.xlsx')


# Delete columns from excel sheet
#columns_to_delete = ['Wikipedia ID', 'Freebase ID', 'Publication date', 'Genres']
# Drop the specified columns
#df.drop(columns=columns_to_delete, inplace=True)
# Save the modified DataFrame back to Excel
#df.to_excel('D:\Gethub\GP\BookSummariesDataset.xlsx', index=False)


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


# Loop through the first 700 rows
for index, row in df.head(1000).iterrows():
    #print(row['Book title'])
    # Iterate through the PDFs in the input folder
    for txt_filename in os.listdir(input_folder):
        # Get the filename without extension
        txt_filename_no_ext = os.path.splitext(txt_filename)[0]
        print('txt_filename : ', txt_filename_no_ext)
        if txt_filename_no_ext == row['Book title']:
            summary_filename = txt_filename
            summary_path = os.path.join(summaries_folder, summary_filename)
            # Check if the text file already exists in the output folder to avoid duplicates
            if not os.path.exists(summary_path):
                with open(summary_path, 'a', encoding='utf-8') as file:
                    #for i in pdf_extractor.OutputTextFinal:
                    file.write(row['Plot summary'])
                    print(f"{summary_filename} || Successfully saved !")
print("Processing completed.")
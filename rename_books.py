import os
import pandas as pd

input_folder = r"D:\Gethub\SummaryFlow\NEW_novels"

extension = ".txt"

## Rename text files with correct form
## Iterate through the PDFs in the input folder
for txt_filename in os.listdir(input_folder):
    original_path = os.path.join(input_folder, txt_filename)
    filename_without_ext = os.path.splitext(txt_filename)[0]
    if extension in filename_without_ext:
        new_filename = filename_without_ext
    else:
        new_filename = txt_filename
    new_path = os.path.join(input_folder, new_filename)
    ## Rename the file
    os.rename(original_path, new_path)
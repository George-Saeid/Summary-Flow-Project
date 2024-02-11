import os
from PDFExtractor2 import PDFExtractor

# Define input and output folders
input_folder = r"C:\Users\lap me\Desktop\GP\novels_pdf_400-500"
output_folder = r"D:\Gethub\GP\novels_textfiles_400-500"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate through the PDFs in the input folder
for pdf_filename in os.listdir(input_folder):
    if pdf_filename.endswith(".pdf"):
        pdf_path = os.path.join(input_folder, pdf_filename)
        text_filename = os.path.splitext(pdf_filename)[0] + ".txt"
        text_path = os.path.join(output_folder, text_filename)

        # Check if the text file already exists in the output folder to avoid duplicates
        if not os.path.exists(text_path):
            pdf_extractor = PDFExtractor(pdf_path, output_folder)
            pdf_extractor.run()
            with open(text_path, 'w', encoding='utf-8') as file:
                for i in pdf_extractor.OutputTextFinal:
                    file.write(i + '\n')
            print(f"{text_filename} || Successfully Extracted")
        else:
            print(f"({text_filename}) || Already Extracted")

print("Processing completed.")

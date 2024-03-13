import os

from PDFExtractor2 import PDFExtractor

# Define input and output folders
input_folder = r"D:\Gethub\SummaryFlow\The alchemist"  # Replace with your input folder path
output_folder = r"D:\Gethub\SummaryFlow"

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
            try:
                pdf_extractor = PDFExtractor(pdf_path, output_folder)
                pdf_extractor.run()
                with open(text_path, 'w', encoding='utf-8') as file:
                    for i in pdf_extractor.OutputTextFinal:
                        file.write(i + '\n')
                print(f"{text_filename} || Successfully Extracted")
            except Exception as e:
                print(f"Error processing {pdf_filename}: {e}")
                continue
        else:
            print(f"({text_filename}) || Already Extracted")

print("Processing completed.")

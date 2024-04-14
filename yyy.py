summary_list = ["the boy is good", "the girl is good", "the dog is good"]


summarized_book = []
# Loop through summaries
#for i in range(len(summary_list)):
#    # Combine all summarise into a single paragraph
#    combined_paragraph = ''.join(summary_list)
#    # Append the combined paragraph to the new book list
#    summarized_book.append(combined_paragraph)
result_book = "\n".join(summary_list)
# Recursively summarize the generated book
print('A level is summarized successfully!!')
print('Summarized book : ')
print(result_book)
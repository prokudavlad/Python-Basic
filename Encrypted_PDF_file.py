import PyPDF2

# Opening the PDF file to be password protected
pdf_file = open('file_name.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Create an object PDF Writer
pdf_writer = PyPDF2.PdfWriter()

# Iterate through each page in a PDF file and add it to the PDF Writer object
for page_num in range(len(pdf_reader.pages)):
    pdf_writer.add_page(pdf_reader.pages[page_num])

# Set a password for a PDF file
pdf_writer.encrypt('your_password')

# Save the protected PDF file to disk
result_pdf = open('file_name-protected.pdf', 'wb')
pdf_writer.write(result_pdf)

# Closing files
result_pdf.close()
pdf_file.close()

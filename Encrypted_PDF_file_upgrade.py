import PyPDF2

# Opening a protected PDF file
pdf_file = open('file_name-protected.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Checking if a PDF file is password protected
if pdf_reader.is_encrypted:

    # Enter password to open PDF file
    pdf_reader.decrypt('your_password')

# Creating a PDF Writer Object
pdf_writer = PyPDF2.PdfWriter()

# Iterate through each page in a PDF file and add it to the PDF Writer object
for page_num in range(len(pdf_reader.pages)):
    pdf_writer.add_page(pdf_reader.pages[page_num])

# Removing the password for a PDF file
pdf_writer.encrypt('', use_128bit=False)

# Save the modified PDF file to disk
result_pdf = open('file_name_unprotected.pdf', 'wb')
pdf_writer.write(result_pdf)

# Closing files
result_pdf.close()
pdf_file.close()

# __Python-basic__
___
1. Creating a password for a PDF file, with the installation of the PyPDF2 library.
2. You can install it using pip:
__pip install PyPDF2__
3. To accomplish this task, you can use this code to create a PDF file.

[Code guide Python]


(https://pypi.org/project/PyPDF2/)

___

4. If an error occurs - __PyPDF2.errors.DeprecationError: PdfFileReader is deprecated and was removed in PyPDF2 3.0.0. Use PdfReader instead__

    
   * 4.1 Using PdfFileReader in PyPDF2 is no longer science fiction as of version 3.0.0. Instead, you must use PdfReader.
   * 4.2 This code opens a PDF file named "file_name.pdf", adds each page to a PDF Writer object, sets the password "your_password" and saves a protected file named "file_name-protected.pdf".
   
(https://pypi.org/project/pdfreader/)
___
5. We add the ability to remove this password or replace it with another one.
To remove the password from a protected PDF file, you must use the decrypt() method of the PdfReader object. Here is an example code:

* 5.1 This code opens a protected PDF file named "file_name-protected.pdf", checks if it is password protected, and if so, enters the password "your_password" to open it. The code then creates a PDF Writer object and adds each page of the PDF file to it. It then removes the password using the encrypt() method, which specifies the password as an empty string. Finally, the code saves the modified PDF file with the name "file_name-unprotected.pdf".

(https://www.geeksforgeeks.org/python-strings-decode-method/)

___
6. Extract audio track from video.
    6.1 To extract an audio track from an mp4 video file, you need to install the ffmpeg library, which allows you to work with video and audio files in Python.
    6.2 Installing the ffmpeg library:

___!pip install ffmpeg-python___

(https://pypi.org/project/ffmpeg-python/)

    6.3 This script uses ffmpeg to read the input video file, extract the audio track and save it to the output mp3 file. Simple path to source video file and path to write audio file into input_file and output_file variables respectively and load the script.

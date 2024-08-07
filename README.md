## Merge Word, PDF, and Image Files into a Single PDF


### Objective
This Python script merges multiple Word, PDF, and image files into a single PDF document. It provides a user-friendly interface for selecting input and output folders and specifying the output filename.

### Skills Learned
* Python programming fundamentals (file I/O, function definition, error handling)
* Working with PDF files (PyPDF2 library)
* Converting Word documents to PDF (docx2pdf library)
* Image processing (PIL library)
* Basic GUI development (tkinter library)

### Tools Used
Python libraries:
- PyPDF2
- Docx2pdf
- Pillow
- Tkinter

You can install them using pip:

```bash
pip install PyPDF2 docx2pdf Pillow tkinter
```
### Steps

#### 1) Create Input and Output Folders:
   - Create two folders on your desktop named "PDFinput" and "PDFoutput".
   - Place the files you want to merge into the "PDFinput" folder.
   - Change the input and output paths on the code to be the new folders you created

#### 2) Run the script:
   - Execute the Python script/
   - A dialog box will appear prompting you to enter the desired output filename
   - The merged PDF will be saved in the "PDFoutput" folder
   

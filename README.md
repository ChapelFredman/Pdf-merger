## Merge Word, PDF, and Image Files into a Single PDF

### Overview
This Python script merges Word documents, PDFs, and images into a single PDF file. It offers user-friendly features like error handling, progress indication (can be added), and customizable output filenames.

### Installation
Ensure you have the following libraries installed:

* `PyPDF2`
* `docx2pdf`
* `Pillow`
* `tkinter`

You can install them using pip:

```bash pip install PyPDF2 docx2pdf Pillow tkinter```

### Usage:

1) Place your Word, PDF, and image files in the specified input folder.
2) Run the script.
3) A dialog box will appear asking for the desired output filename.
4) The merged PDF will be saved in the specified output folder.

### Script Functionality:

Converts Word documents to PDF format.
Merges PDF and image files into a single PDF.
Provides a user-friendly interface for specifying the output filename.
Handles empty input folders with an error message.

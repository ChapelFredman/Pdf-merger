import os
from PyPDF2 import PdfMerger
import docx2pdf
from PIL import Image
import tkinter as tk
from tkinter import messagebox, simpledialog
import logging

def get_output_filename():
    """Prompts the user for the output filename and returns it."""
    root = tk.Tk()
    root.withdraw()
    filename = simpledialog.askstring("Output File", "Enter the desired output filename:")
    if filename:
        return filename.strip()  # Remove leading/trailing spaces
    else:
        # Handle case where user cancels the input dialog
        messagebox.showerror("Error", "Please enter a filename.")
        exit(1)  # Exit the program

def merge_files(input_folder, output_folder):
    """Merges Word, PDF, and image files from a folder into a single PDF on output folder.

    Args:
        input_folder: The path to the input folder.
        output_folder: The path to the output folder.
        output_filename: (Optional) The name of the output PDF file.
    """

    if not os.listdir(input_folder):
        messagebox.showerror("Error", "Input folder is empty.")
        return

    output_filename = get_output_filename()  # Get user input for filename
    
    if not output_filename.endswith(".pdf"):
        output_filename += ".pdf"
        
    merger = PdfMerger()

    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        try:
            if filename.endswith(".docx"):
                pdf_file = os.path.join(output_folder, filename[:-5] + ".pdf")
                docx2pdf.convert(file_path, pdf_file)
                merger.append(pdf_file)
            elif filename.endswith(".pdf"):
                merger.append(file_path)
            elif filename.endswith(".jpg") or filename.endswith(".png"):
                pdf_file = os.path.join(output_folder, filename[:-4] + ".pdf")
                image = Image.open(file_path)
                image.save(pdf_file, "PDF")
                merger.append(pdf_file)
        except Exception as e:
            logging.error(f"Error processing file {filename}: {e}")

    output_file = os.path.join(output_folder, output_filename)
    with open(output_file, "wb") as output:
        merger.write(output)

    merger.close()

input_folder = r"path to input folder"
output_folder = r"path to output folder"
os.makedirs(output_folder, exist_ok=True)
merge_files(input_folder, output_folder)

'''
PDF Merger Script

This script merges all PDF files in the input folder into a single PDF.

Dependencies:
  - PyPDF2 (pip install PyPDF2)

Usage:
  python merge_pdfs.py input_pdf/ output_merged_pdf/

Outputs:
  A single merged PDF saved as output_merged_pdf/merged_output.pdf
  
Note: 
  In input_pdf directory, for simplicity, place number initially with the name of the PDF files 
  to control the order of merging. Example: 1_abc.pdf, 2_xyz.pdf, ... etc., OR 1 abc, 2 xyz, ... etc., 
  PdF files will be merged in the same sequence.
'''
import os
import sys
import argparse
import shutil
from PyPDF2 import PdfMerger

def clean_output_folder(output_merged_pdf: str) -> None:
    """
    Deletes all contents of the output_merged_pdf folder if it exists.
    """
    if os.path.exists(output_merged_pdf):
        print(f"Cleaning output folder: {output_merged_pdf}")
        shutil.rmtree(output_merged_pdf)
    os.makedirs(output_merged_pdf)

def merge_all_pdfs(input_folder: str, output_merged_pdf: str, output_filename: str = "merged_output.pdf") -> None:
    if not os.path.isdir(input_folder):
        print(f"Error: Input folder not found: {input_folder}")
        sys.exit(1)

    # Clean output folder before merging
    clean_output_folder(output_merged_pdf)

    output_path = os.path.join(output_merged_pdf, output_filename)
    pdf_files = sorted([f for f in os.listdir(input_folder) if f.lower().endswith('.pdf')])
    if not pdf_files:
        print("No PDF files found to merge.")
        return

    merger = PdfMerger()
    for pdf_file in pdf_files:
        file_path = os.path.join(input_folder, pdf_file)
        try:
            merger.append(file_path)
            print(f"Added: {file_path}")
        except Exception as e:
            print(f"Error adding '{file_path}': {e}")

    try:
        merger.write(output_path)
        merger.close()
        print(f"\nMerged PDF saved to: {output_path}")
    except Exception as e:
        print(f"Error saving merged PDF: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Merge all PDFs in a folder into one PDF.")
    parser.add_argument('input_folder', help='Folder containing PDF files to merge')
    parser.add_argument('output_merged_pdf', help='Folder to save the merged PDF')
    args = parser.parse_args()

    merge_all_pdfs(args.input_folder, args.output_merged_pdf)
'''
PDF to JPEG Batch Converter

This script converts all PDF files (single or multi-page) in a folder into JPEG images.

Dependencies:
  - pdf2image (pip install pdf2image)
  - Pillow (pip install pillow)
  - poppler-utils (system package; install via apt/brew/etc.)

Usage:
  python pdf_to_jpeg.py input_folder output_folder [--dpi 200]

Outputs:
  JPEG images saved in subfolders named after each PDF file.
'''
import os
import sys
import argparse
import shutil
from pdf2image import convert_from_path

def clean_output_folder(output_folder: str) -> None:
    """
    Deletes all contents of the output folder if it exists.
    """
    if os.path.exists(output_folder):
        print(f"Cleaning output folder: {output_folder}")
        shutil.rmtree(output_folder)
    os.makedirs(output_folder)

def convert_pdf_to_jpeg(pdf_path: str, output_subfolder: str, dpi: int = 200) -> None:
    os.makedirs(output_subfolder, exist_ok=True)
    try:
        pages = convert_from_path(pdf_path, dpi=dpi)
    except Exception as e:
        print(f"Error: Failed to convert '{pdf_path}'. {e}")
        return

    for idx, page in enumerate(pages, start=1):
        output_path = os.path.join(output_subfolder, f"page_{idx}.jpg")
        try:
            page.convert('RGB').save(output_path, 'JPEG')
            print(f"Saved: {output_path}")
        except Exception as e:
            print(f"Error: Could not save page {idx} for '{pdf_path}'. {e}")

def batch_convert_pdfs(input_folder: str, output_folder: str, dpi: int = 200) -> None:
    if not os.path.isdir(input_folder):
        print(f"Error: Input folder not found: {input_folder}")
        sys.exit(1)

    # Clean output folder
    clean_output_folder(output_folder)

    pdf_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.pdf')]

    if not pdf_files:
        print("No PDF files found in the input folder.")
        return

    for pdf_file in pdf_files:
        pdf_path = os.path.join(input_folder, pdf_file)
        pdf_name = os.path.splitext(pdf_file)[0]
        output_subfolder = os.path.join(output_folder, pdf_name)
        print(f"\nProcessing '{pdf_file}'...")
        convert_pdf_to_jpeg(pdf_path, output_subfolder, dpi)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert all PDFs in a folder to JPEG images.")
    parser.add_argument('input_folder', help='Folder containing PDF files')
    parser.add_argument('output_folder', help='Folder to save JPEG images')
    parser.add_argument('--dpi', type=int, default=200, help='Resolution in DPI (default: 200)')
    args = parser.parse_args()

    batch_convert_pdfs(args.input_folder, args.output_folder, args.dpi)
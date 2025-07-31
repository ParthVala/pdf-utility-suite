# PDF Utility Suite

A simple collection of Python scripts for working with PDF files:

* **`pdf_to_jpeg.py`**: Convert all PDF files in a folder to JPEG images, one image per page.
* **`merge_pdfs.py`**: Merge all PDF files in a folder into a single PDF document.

---

## 🚀 Features

1. **Batch PDF ➡️ JPEG**

   * Converts each page of every `.pdf` in `input_pdf/` into `page_1.jpg`, `page_2.jpg`, …
   * Saves images into subfolders under `output_images/`, named after each PDF file.
   * Automatically cleans `output_images/` on each run.

2. **Batch PDF Merge**

   * Merges all `.pdf` files in `input_pdf/` (sorted by name) into one file.
   * Outputs `merged_output.pdf` to `output_merged_pdf/`, cleaning that folder first.

---

## 📋 Prerequisites

* Python 3.7+
* [Poppler](https://poppler.freedesktop.org/) system package
* pip packages:

  * `pdf2image`
  * `Pillow`
  * `PyPDF2`

> **Note**: The project assumes you keep your virtual environment directory out of version control (e.g., named `venv/`). Add it to your `.gitignore`:
>
> ```gitignore
> venv/
> ```

---

## 🔒 Security & Offline Use

* **Local Processing Only**: All PDF conversions and merges happen entirely on your machine. The scripts do not perform any network calls or send data externally.
* **Offline Operation**: Once you have installed the required dependencies (`pdf2image`, `Pillow`, `PyPDF2`, and Poppler), you can run the tools without any internet connection. Ideal for air-gapped or secure environments.

---

## 🛠️ Setup & Installation

1. **Clone repository**

   ```bash
   git clone <your-repo-url>
   cd pdf-utility-suite
   ```

2. **Create a Python virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate      # macOS/Linux
   venv\Scripts\activate.bat    # Windows
   ```

3. **Install Python dependencies**

   ```bash
   pip install --upgrade pip
   pip install pdf2image Pillow PyPDF2
   ```

4. **Install Poppler**

   * **macOS**:

     ```bash
     brew install poppler
     ```
   * **Ubuntu/Linux**:

     ```bash
     sudo apt-get update
     sudo apt-get install poppler-utils
     ```
   * **Windows**:

     1. Download from [Poppler for Windows](http://blog.alivate.com.au/poppler-windows/)
     2. Unzip and add the `bin/` folder to your `PATH`.

---

## 📂 Directory Structure

```
pdf-utility-suite/
├── pdf_to_jpeg.py         # Batch PDF ➡️ JPEG script
├── merge_pdfs.py          # Batch PDF merge script
├── input_pdf/             # Place your source PDFs here
├── output_images/         # Generated JPEGs
├── output_merged_pdf/     # Merged PDF output
├── .gitignore             # Exclude venv/, __pycache__/, etc.
└── README.md              # This file
```

---

## ⚙️ Usage

### 1. Convert PDFs to JPEGs

```bash
python pdf_to_jpeg.py input_pdf/ output_images/ [--dpi 200]
```

* `input_pdf/`: Folder containing one or more `.pdf` files.
* `output_images/`: Destination folder for JPEGs (will be cleaned first).
* `--dpi`: (optional) Resolution in dots-per-inch (default: `200`).

Each PDF creates its own subfolder under `output_images/`.

### 2. Merge PDFs into One

```bash
python merge_pdfs.py input_pdf/ output_merged_pdf/
```

* `input_pdf/`: Folder containing one or more `.pdf` files.
* `output_merged_pdf/`: Destination folder for the merged PDF (will be cleaned first).

Result: `output_merged_pdf/merged_output.pdf`

---
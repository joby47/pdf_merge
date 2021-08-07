# pdf_merge
A simple utility to merge images - such as scanned pages - into a single PDF document.

## Introdruction
Many printers have an automatic feed scanner feature. This allows multi-page documents to be scanned, without the user having to place each page on the scanner bed by hand. However, some scanners (including mine!) with an automatic feed are not able to scan two sided (duplex) documents. Instead, they are limited to scanning the "upwards" side of each piece of paper placed in the feed.

This simple Python module aims to assist with scanning two-sided, multi-page documents using such scanners. Its purpose is to combine the individual image files obtained from the automatic feed scanning into a single PDF document.

## Usage
The purpose of the pdf_merge module is create a single PDF file of a document, the pages of which have been scanned into separate image files. 

The image files should be saved in two separate directories. The first directory should contain the image files for the odd-numbered pages. When sorted in alphabetical order by filename, these page should be sorted in order, from **first to last**. The second directory should contain the image files for the even-numbered pages. When sorted in alphabetical order by filename, these page should be sorted in reverse order, from **last to first**. 

Images are manipulated using the [Pillow library](https://pillow.readthedocs.io/en/stable/index.html "Pillow homepage"). As such all file formats supported by this library are supported (including BMP, JPEG, PDF, TIFF, ...).

To use this module, the user must supply the following information:
1. The path of the directory containing the odd-numbered pages as image files.
2. The path of the directory containing the even-numbered pages as image files.
3. The filename (and path) which the resulting PDF document should be saved as.

There are three ways in which this information can be supplied. These are described bellow.

### Command line interface
The user may choose to simply execute the Python module. This can be done by opening the terminal (or command prompt), navigating to the directory containing the pdf_merge.py file and entering `python3 pdf_merge.py`. This will launch a command line interface which will prompt the user to enter the necessary information.

### Command line arguments
The user may elect to supply the necessary information by command line arguments. Three arguments should be provided, giving the information in the order listed above.

`python3 pdf_merge.py odd_dir even_dir outfile.pdf`

### Call the method
Alternatively, this utility can be used within another Python program by calling the `merge_images` method.

```python
import pdf_merge
...
odds_dir = '../example/odd'
evens_dir = '../example/even'
outfile = '../example/scanned.pdf'
pdf_merge.merge_images(odds_dir, evens_dir, outfile)
```


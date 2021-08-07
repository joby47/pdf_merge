# pdf_merge
A simple utility to merge images - such as scanned pages - into a single PDF document.

## Introdruction
Many printers have an automatic feed scanner feature. This allows multi-page documents to be scanned, without the user having to place each page on the scanner bed by hand. However, some scanners (including mine!) with an automatic feed are not able to scan two sided (duplex) documents. Instead, they are limited to scanning the "upwards" side of each piece of paper placed in the feed.

This simple Python module aims to assist with scanning two-sided, multi-page documents using such scanners. Its purpose is to combine the individual image files obtained from the automatic feed scanning into a single PDF document.

## Dependencies
This module uses the [Pillow library](https://pillow.readthedocs.io/en/stable/index.html "Pillow homepage") to load and maniplulate the images. Pillow must be installed for the module to work. If Pillow is not currently installed on your machine, please see the [Pillow installation instructions](https://pillow.readthedocs.io/en/stable/installation.html "Installation - Pillow"). In most cases, this amounts to using `python3 -m pip install --upgrade Pillow`.

## Preparation
In order to get the scanned document in to the appropriate format to use with pdf_merge, please follow the steps bellow.
1. Begin by scanning the odd-numbered pages in the order they appear in the document. Place the document to be scanned into the scanner feed as you usually would. Select the option to scan to individual images (e.g. JPEG) from the scanner menu and scan the document.
2. Save the image files of the odd-numbered pages into a single directory which contains no other files.
3. Now scan the even-numbered pages. Place the document into the scanner feed 'backwards' by flipping it on its long edge. The reveerse side of the last page should now be on top. Scan the pages to individual image files as before
4. Save the image files of the even-numbered pages into a separate empty directory.
5. Use the pdf_merge modules to merge the image files into a single PDF document.

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

![Example of using the CLI](/example/CLI_example.png)

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

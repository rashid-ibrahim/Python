from os import getcwd, listdir, rename
from os.path import isfile, join
from PyPDF2 import PdfFileWriter, PdfFileReader

"""
Source code compiled with PyInstaller
Use command:
    pyinstaller {file_name} --onefile
--onefile condeses the code into a single exe.
-w hide any console output from the users.
"""


# def name_reader(page):
#     """
#     At some point in the future I need to write out this function to read out a specific spot on each page of the pdf
#     files and then use that as the name for the files.
#
#     :param page: A single page of the pdf being parsed.
#     :return: File name for the given input page.
#     """
#     pass


def main():
    location = getcwd()
    files = [f for f in listdir(location) if isfile(join(location, f)) and f.endswith('.pdf')]

    count = 0
    skip = 0

    for file in files:
        ofile = open(file, 'rb')
        pdf = PdfFileReader(ofile)

        # Only try to split the PDF if it has more than one page.
        if pdf.getNumPages() > 1:
            # After this loop there will be an unchanged original and then a new one for each page.
            for i in range(pdf.numPages):
                output = PdfFileWriter()
                output.addPage(pdf.getPage(i))

                # This line is where I would need to add character retrieval to put the actual file name.
                # page_name = name_reader(pdf.getPage(i)) then I could replace the {file} variable below.
                with open(f'{file[:-4]}_page_{i+1}.pdf', 'wb') as outputStream:
                    output.write(outputStream)
                count += 1
        else:
            skip += 1
        ofile.close()

        try:
            rename(fr'{location}\{file}', fr'{file[:-4]}_Original.pdf')
        except Exception as e:
            # We don't really care what the exception is when renaming the files. If it doesn't work we just move on.
            pass

    return count, skip


if __name__ == '__main__':
    print('Splitting all multi page PDFs into their own document.')
    docs_split, docs_skipped = main()
    print(f'{docs_split} were broken apart and {docs_skipped} were skipped because they only have one page.')
    input('Press Any Key to Exit')

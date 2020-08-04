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
    try:
        location = getcwd()
        files = [f for f in listdir(location) if isfile(join(location, f)) and f.endswith('.pdf')]

        for file in files:
            ofile = open(file, 'rb')
            pdf = PdfFileReader(ofile)

            # After this loop there will be an unchanged original and then a new one for each page.
            for i in range(pdf.numPages):
                output = PdfFileWriter()
                output.addPage(pdf.getPage(i))

                # This line is where I would need to add character retrieval to put the actual file name.
                # page_name = name_reader(pdf.getPage(i)) then I could replace the {file} variable below.
                with open(f'{file[:-4]}_page_{i+1}.pdf', 'wb') as outputStream:
                    output.write(outputStream)

            ofile.close()
            print(f'renaming: {location}/{file}')
            rename(fr'{location}\{file}', fr'{file[:-4]}_Original.pdf')

    except Exception as e:
        input(f'Exception happened: {e}')

    return 1


if __name__ == '__main__':
    main()
    input('Waiting... press any key to continue')

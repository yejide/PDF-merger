import PyPDF2


def pdfMerger(file_names, output):
    merger = PyPDF2.PdfFileMerger()
    for file_name in file_names:
        with open(file_name, 'rb') as f:
            merger.append(file_name)
    with open(output, "wb") as f:
        merger.write(f)


output = "combined_files.pdf"
file_names = ["example1.pdf", "example2.pdf"]
pdfMerger(file_names, output)

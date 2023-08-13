from PyPDF2 import PdfReader, PdfWriter

pages = [1, 2]

with open("PDF Splitter/merged.pdf", "rb") as f:
    reader = PdfReader(f)
    writer = PdfWriter()
    rest_writer = PdfWriter()

    for page in range(len(reader.pages)):
        if page in pages:
            writer.add_page(reader.pages[page])
        else:
            rest_writer.add_page(reader.pages[page])

    with open("selected.pdf", "wb") as f2:
        writer.write(f2)

    with open("rest.pdf", "wb") as f2:
        rest_writer.write(f2)
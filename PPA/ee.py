import PyPDF2

def pdf_to_table(pdf_file):
  """Converts a PDF file to a table format.

  Args:
    pdf_file: The path to the PDF file.

  Returns:
    A list of lists, where each sublist represents a row in the table.
  """

  pdf_reader = PyPDF2.PdfReader(pdf_file)
  num_pages = len(pdf_reader.pages)

  table = []
  for page_num in range(num_pages):
    page = pdf_reader.pages[page_num]
    text = page.extract_text()

    # Split the text into lines.
    lines = text.split('\n')

    # Find the table rows.
    table_rows = []
    for line in lines:
      if line.strip():
        table_rows.append(line.split())

    table.append(table_rows)

  return table


if __name__ == '__main__':
  pdf_file = 'F:\PPA\ECS.pdf'
  table = pdf_to_table(pdf_file)

  print(table)
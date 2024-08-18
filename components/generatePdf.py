import fitz

def generatePdf(data):
  """
  Generates a PDF document with the provided API data.
  """
  try:
    doc = fitz.open()
    page = doc.new_page()
    # Add title and author
    page.insert_text((20, 100), 'API Users Data', fontname='Helvetica-Bold', fontsize=20)
    # Add table header
    page.insert_text((30, 150), 'ID', fontname='Helvetica-Bold', fontsize=14)
    page.insert_text((50, 150), 'Name', fontname='Helvetica-Bold', fontsize=14)
    page.insert_text((170, 150), 'Email', fontname='Helvetica-Bold', fontsize=14)
    page.insert_text((320, 150), 'Username', fontname='Helvetica-Bold', fontsize=14)
    page.insert_text((420, 150), 'Phone', fontname='Helvetica-Bold', fontsize=14)

    # Add table data
    for i, user in enumerate(data, start=1):
      page.insert_text((30, 150 + (i * 50)), f'{user["id"]}', fontname='Helvetica', fontsize=10)
      page.insert_text((50, 150 + (i * 50)), f'{user["name"]}', fontname='Helvetica', fontsize=10)
      page.insert_text((170, 150 + (i * 50)), f'{user["email"]}', fontname='Helvetica', fontsize=10)
      page.insert_text((320, 150 + (i * 50)), f'{user["username"]}', fontname='Helvetica', fontsize=10)
      page.insert_text((420, 150 + (i * 50)), f'{user["phone"]}', fontname='Helvetica', fontsize=10)

    doc.save("list_api_users.pdf")
    return doc.write()
  except Exception as e:
    print(f'Error generating PDF: {e}')
  finally:
    print('PDF generation completed')


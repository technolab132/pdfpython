from PyPDF2 import PdfReader
try:
    from docx import Document
except ImportError:
    # If the above import fails, try to handle it gracefully
    try:
        from warnings import PendingDeprecationWarning
        # Rest of your code
    except ImportError:
        print("Error: Unable to import required modules.")
        exit()

def extract_headings_pdf(file_path):
    headings = []
    try:
        with open(file_path, 'rb') as file:
            pdf_reader = PdfReader(file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                headings.extend(line.strip() for line in text.split('\n') if line.strip())
    except Exception as e:
        print(f"Error extracting headings from PDF: {e}")
    
    print(headings)
    return headings


def extract_headings_docx(file_path):
    headings = []
    try:
        doc = Document(file_path)
        for paragraph in doc.paragraphs:
            if paragraph.style.name.startswith('Heading'):
                headings.append(paragraph.text)
    except Exception as e:
        print(f"Error extracting headings from DOCX: {e}")

    print(headings)
    return headings

def generate_table_of_contents(headings):
    toc = {'title': 'Table of Contents', 'children': []}  # Root level
    current_level = 1
    current_parent = toc

    for heading in headings:
        level = heading.count(' ') // 2 + 1
        node = {'title': heading, 'children': []}

        if level == 1:
            toc['children'].append(node)
            current_parent = node
        elif level > current_level:
            current_parent['children'].append(node)
            current_parent = node
        elif level == current_level:
            current_parent['children'].append(node)
        else:
            for _ in range(current_level - level):
                current_parent = current_parent['children'][-1]
            current_parent['children'].append(node)

        current_level = level

    return toc['children']  

def print_table_of_contents(toc, indent=0):
    for node in toc:
        title = node['title']
        print(' ' * indent + f"{title}")
        if 'children' in node and node['children']:
            print_table_of_contents(node['children'], indent + 2)


def main(file_path):
    if file_path.lower().endswith('.pdf'):
        headings = extract_headings_pdf(file_path)
    elif file_path.lower().endswith('.docx'):
        headings = extract_headings_docx(file_path)
    else:
        print("Unsupported file format.")
        return

    table_of_contents = generate_table_of_contents(headings)
    # print_table_of_contents(table_of_contents)

if __name__ == "__main__":
    file_path = "document.pdf"
    main(file_path)

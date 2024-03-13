# import fitz  # PyMuPDF

# def extract_text_from_pdf(pdf_path):
#     try:
#         doc = fitz.open(pdf_path)
#         text = ""
#         for page_num in range(doc.page_count):
#             page = doc[page_num]
#             text += page.get_text()
#         return text
#     except Exception as e:
#         print(f"Error extracting text from PDF: {e}")
#         return None
#     finally:
#         if doc:
#             doc.close()

# if __name__ == "__main__":
#     pdf_path = "document.pdf"
    
#     extracted_text = extract_text_from_pdf(pdf_path)

#     if extracted_text:
#         print("\nExtracted Text:")
#         print(extracted_text.replace(".", "").replace(",", ""))
#     else:
#         print("Text extraction failed.")


# import fitz  # PyMuPDF

# def extract_text_from_pdf(pdf_path):
#     try:
#         doc = fitz.open(pdf_path)
#         paragraphs = []

#         for page_num in range(doc.page_count):
#             page = doc[page_num]
#             sentences = page.get_text("text").split('.')

#             for i in range(0, len(sentences), 2):
#                 paragraph = ".".join(sentences[i:i + 2]).strip()
#                 if paragraph:
#                     paragraphs.append(paragraph)

#         return paragraphs
#     except Exception as e:
#         print(f"Error extracting text from PDF: {e}")
#         return None
#     finally:
#         if doc:
#             doc.close()

# if __name__ == "__main__":
#     pdf_path = "meet.pdf"

#     extracted_paragraphs = extract_text_from_pdf(pdf_path)

#     if extracted_paragraphs:
#         print("\nExtracted Paragraphs:")
#         for idx, para in enumerate(extracted_paragraphs, 1):
#             print(f"Paragraph {idx}:\n{para}\n")
#     else:
#         print("Text extraction failed.")


# ----------------------------------------------------------------

# import fitz  # PyMuPDF
# import openai

# # Set your OpenAI API key
# openai.api_key = "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"

# def generate_headings(paragraph):
#     # Call the OpenAI API to generate headings
#     messages = [
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": f"Create a concise header for the following paragraph:\n\n\"{paragraph}\""}
#     ]
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",  # Use the correct model for chat completions
#         messages=messages,
#         max_tokens=20,  # Adjust the max_tokens parameter as needed
#         temperature=0.6  # Adjust the temperature parameter as needed
#     )
#     return response.choices[0].message["content"].strip()

# def extract_text_from_pdf(pdf_path):
#     try:
#         doc = fitz.open(pdf_path)
#         paragraphs = []

#         for page_num in range(doc.page_count):
#             page = doc[page_num]
#             sentences = page.get_text("text").split('.')

#             for i in range(0, len(sentences), 2):
#                 paragraph = ".".join(sentences[i:i + 2]).strip()
#                 if paragraph:
#                     paragraphs.append(paragraph)

#         return paragraphs
#     except Exception as e:
#         print(f"Error extracting text from PDF: {e}")
#         return None
#     finally:
#         if doc:
#             doc.close()

# if __name__ == "__main__":
#     pdf_path = "document.pdf"

#     extracted_paragraphs = extract_text_from_pdf(pdf_path)

#     if extracted_paragraphs:
#         print("\nExtracted Paragraphs:")
#         for idx, para in enumerate(extracted_paragraphs, 1):
#             heading = generate_headings(para)
#             print(f"Heading: {heading}\nParagraph {idx}:\n{para}\n")
#     else:
#         print("Text extraction failed.")




import fitz  # PyMuPDF
import openai
from html import escape

# Set your OpenAI API key
openai.api_key = "key"

def generate_headings(paragraph):
    # Call the OpenAI API to generate headings
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"The following paragraph contains factual information. Create a concise and accurate heading that summarizes the key points without interpretation. Ensure the heading reflects the actual truth and facts presented in the paragraph:\n\n\"{paragraph}\""}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the correct model for chat completions
        messages=messages,
        max_tokens=20,  # Adjust the max_tokens parameter as needed
        temperature=0.6  # Adjust the temperature parameter as needed
    )
    return response.choices[0].message["content"].strip()

def extract_text_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        paragraphs = []

        for page_num in range(doc.page_count):
            page = doc[page_num]
            sentences = page.get_text("text").split('.')

            for i in range(0, len(sentences), 2):
                paragraph = ".".join(sentences[i:i + 2]).strip()
                if paragraph:
                    paragraphs.append(paragraph)

        return paragraphs
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return None
    finally:
        if doc:
            doc.close()

def generate_html_document(headings, paragraphs):
    # Create an HTML document with headings and paragraphs
    html_content = "<html>\n<head>\n<title>Generated Document</title>\n</head>\n<body>\n"

    for heading, paragraph in zip(headings, paragraphs):
        html_content += f"<h2>{escape(heading)}</h2>\n<p>{escape(paragraph)}</p>\n"

    html_content += "</body>\n</html>"

    return html_content

if __name__ == "__main__":
    pdf_path = "document.pdf"

    extracted_paragraphs = extract_text_from_pdf(pdf_path)

    if extracted_paragraphs:
        print("\nExtracted Paragraphs:")
        headings = [generate_headings(para) for para in extracted_paragraphs]

        # Save the HTML document to a file
        html_content = generate_html_document(headings, extracted_paragraphs)
        with open("output_document1.html", "w", encoding="utf-8") as html_file:
            html_file.write(html_content)

        print("HTML document generated successfully.")
    else:
        print("Text extraction failed.")

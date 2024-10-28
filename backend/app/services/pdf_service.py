import PyPDF2

def extract_text_and_chunk(file_path):
    text = ""
    with open(file_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text()

    # Simple chunking based on word count
    words = text.split()
    chunk_size = 100  # Adjust as needed
    chunks = [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks

from apps.check_scanner.utils.file.pdf_utils import extract_text_from_pdf_util


def extract_text_util(file) -> str:
    """
        Extract text from a PDF file
        :param file - PDF file
        :return: Extracted text from the PDF file
    """
    if file.name.endswith('.pdf'):
        text = extract_text_from_pdf_util(file)
    return text
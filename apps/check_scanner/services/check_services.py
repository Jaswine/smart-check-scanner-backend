from typing import List

from django.contrib.auth.models import User

from apps.check_scanner.models import Check
from apps.check_scanner.utils.file.pdf_utils import extract_text_from_pdf_util
from apps.check_scanner.utils.file_utils import extract_text_util
from apps.check_scanner.utils.gemini_utils import generate_text


def fild_all_checks() -> List[Check]:
    """
        Get all active checks from the database
        :return: List[Check]
    """
    return Check.objects.all()

def create_check(user: User, file) -> Check:
    """
        Create a new check and save it to the database
        :param user: User object
        :param file: File object
        :return: Check object if successful, None otherwise
    """
    try:
        return Check.objects.create(user=user, file=file)
    except Exception as e:
        print(f"Error creating check: {e}")
        return None

def check_save_extracted_text(check: Check,
                              content: str) -> Check | None:
    """
        Save the extracted text to the database
        :param check: Check object
        :param content: Extracted text
        :return: Check object if successful, None otherwise
    """
    try:
        check.extracted_text = content
        check.status = 'processing'
        check.save()
        return check
    except Exception as e:
        print(f"Error saving extracted text: {e}")
        return None

def check_save_generated_text(check: Check,
                              recommendations: str = '',
                              status: str = 'failed') -> Check | None:
    """
        Save the generated text to the database
        :param check: Check object
        :param recommendations: Generated text
        :param status: Status of the check ('completed' or 'failed')
        :return: Check object if successful, None otherwise
    """
    try:
        check.recommendations = recommendations
        check.status = status
        check.save()
        return check
    except Exception as e:
        print(f"Error saving generated text: {e}")
        return None

def check_handling(user: User, file) -> Check | None:
    """
        Handle the check by extracting text from the PDF file, generating gemini recommendations,
        and saving the results to the database
        :param user: User object
        :param file: File object
        :return: Check object if successful, None otherwise
    """
    check = create_check(user, file)
    extracted_text = extract_text_util(check.file)
    check_save_extracted_text(check, extracted_text)
    recommendations = generate_text(extracted_text)
    if recommendations:
        check_save_generated_text(check, recommendations, 'completed')
        return check
    check_save_generated_text(check)
    return None
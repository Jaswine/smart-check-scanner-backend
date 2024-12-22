
def text_handling_util(text) -> str:
    """
        Handle text for checking and generating gemini recommendations
        :param text: Text from the PDF file
        :return: Generated gemini recommendations
    """
    print("Text: \n\n", text)
    text = text.split('---------------------------------------------------------')
    all_products = text[2].split('\n')
    products, p = " ", " "

    for product in all_products:
        p += product
        p += ' '

        if '$' in product:
            products += p
            p = "; "
    return products
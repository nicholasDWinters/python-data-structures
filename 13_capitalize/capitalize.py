def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    phrase.replace(' ', '.')
    new_word = phrase.capitalize()
    new_word.replace('.', ' ')

    return new_word

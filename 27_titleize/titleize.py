def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    low_phrase = phrase.lower()
    word_list = low_phrase.split(' ')

    return ' '.join([word.capitalize() for word in word_list])

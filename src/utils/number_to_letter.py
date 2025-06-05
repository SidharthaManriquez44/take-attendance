def number_to_letter(number) -> list[str]:
    """
    Converts a number to the corresponding letters of the alphabet (Ex. 4 -> ['A', 'B', 'C', 'D']).

    :return: A list of uppercase letters.
    """
    if not 1 <= number <= 26:
        raise ValueError("Number must be between 1 and 26.")

    return [chr(i) for i in range(ord('A'), ord('A') + number)]

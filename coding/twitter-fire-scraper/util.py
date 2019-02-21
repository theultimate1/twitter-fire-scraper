import colorama


def strtobool(v):
    return v.lower() in ["yes", "true", "t", "1"]


def colorama_reset():
    print colorama.Fore.WHITE,
    print colorama.Back.BLACK,


def colorama_highlight_red(text, keyword):
    """
    Highlights text red for a terminal.
    :param text: Text.
    :param keyword: Keyword to highlight.
    :return: Highlighted text.
    """
    return text.replace(keyword, (colorama.Fore.WHITE + colorama.Back.RED +
                                  keyword +
                                  colorama.Fore.WHITE + colorama.Back.BLACK))

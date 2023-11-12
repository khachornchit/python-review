from colorama import init, Fore, Back, Style


def print_colored_text(text, fore_color=None, back_color=None, style=None):
    formatted_text = ''
    if fore_color:
        formatted_text += fore_color
    if back_color:
        formatted_text += back_color
    if style:
        formatted_text += style
    formatted_text += text + Style.RESET_ALL
    print(formatted_text)


if __name__ == '__main__':
    init()

    print_colored_text('some red text', Fore.RED)
    print_colored_text('and with a green background', Back.GREEN)
    print_colored_text('and in dim text', Style.DIM)
    print_colored_text('back to normal now')

def font_color_choose(texto, cor):
    # font_color_choose('Texto legal', "\033[0;30m")
    print(cor + texto + '\033[0m')

def font_color(texto, cor):
    # font_color('Texto legal', "UNDERLINE, white")
    cor = cor.upper()
    cor = cor.replace(",","+")

    WHITE = "\033[38;2;255;255;255m"
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"

    WHITE_BG = "\033[48;2;255;255;255m"
    BLACK_BG = "\033[1;40m"
    RED_BG = "\033[1;41m"
    GREEN_BG = "\033[1;42m"
    YELLOW_BG = "\033[1;43m"
    BLUE_BG = "\033[1;44m"
    MAGENTA_BG = "\033[1;45m"
    CYAN_BG = "\033[1;46m"
    LIGHT_GRAY_BG = "\033[1;47m"
    DARK_GRAY_BG = "\033[1;100m"
    LIGHT_RED_BG = "\033[1;101m"
    LIGHT_GREEN_BG = "\033[1;102m"
    LIGHT_YELLOW_BG = "\033[1;103m"
    LIGHT_BLUE_BG = "\033[1;104m"
    LIGHT_MAGENTA_BG = "\033[1;105m"
    LIGHT_CYAN_BG = "\033[1;106m"

    if bool(cor) == True:
        print(eval(cor) + texto + '\033[0m')



# font_color('Mensagem colorida!', 'cor em ansi')
# \033[38;2;<r>;<g>;<b>m     #Select RGB foreground color
# \033[48;2;<r>;<g>;<b>m     #Select RGB background color
# EXAMPLE:
# \033[38;2;255;82;197;48;2;155;106;0mText
# https://raccoon.ninja/pt/dev-pt/tabela-de-cores-ansi-python/

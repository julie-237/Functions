SPACE = " "
UI_WIDTH = 100
VERTICAL_LINE_TEXTURE = "****"
VERTICAL_BORDER_WIDTH = len(VERTICAL_LINE_TEXTURE)
SPACE_TAKEN_BY_VERTICAL_BORDER = VERTICAL_BORDER_WIDTH * 2


def custom_centerized_printer(text):
    text_to_print = text if len(text) % 2 == 0 else text + SPACE
    paddingLenght = (UI_WIDTH - len(text_to_print) - SPACE_TAKEN_BY_VERTICAL_BORDER) / 2
    function_padding = SPACE * int(paddingLenght)
    print(VERTICAL_LINE_TEXTURE + function_padding + text_to_print + function_padding + VERTICAL_LINE_TEXTURE)
    return function_padding

print("toto")
blandine = custom_centerized_printer("toto")
print(VERTICAL_LINE_TEXTURE + "-" * len(blandine) + "toto")


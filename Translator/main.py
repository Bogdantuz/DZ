from googletrans import Translator


def translate_file(
        file_name: str = 'input.txt',
        *,
        print_output: bool = True,
        output_to_file: bool = False,
        name_of_output_file: str = 'output.txt'
):
    translator = Translator()

    with open(file_name, encoding='utf-8') as input_file:
        input_file = f'{input_file.read()}'
        result = translator.translate(input_file).text

        if print_output is True:
            print(result)


    if output_to_file is True:
        with open(name_of_output_file, 'w', encoding='utf-8') as output_file:
            output_file.write(result)
        
    return result


def translate_text(
        text,
        *,
        print_output: bool = True,
        output_to_file: bool = False,
        name_of_output_file: str = 'output.txt'
):
    translator = Translator()
    result = translator.translate(text).text

    if print_output is True:
        print(result)

    if output_to_file is True:
        with open(name_of_output_file, 'w', encoding='utf-8') as output_file:
            output_file.write(result)

    return result


if __name__ == '__main__':
    translate_file('Translator/input.txt', output_to_file=True)
    translate_text('Hello, World!')
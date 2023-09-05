from gendiff.formatters import stylish, plain, json


def get_formatter(make_format):

    FORMATS = {
        'stylish': stylish.make_format,
        'plain': plain.make_format,
        'json': json.make_format
    }

    output_format = FORMATS.get(make_format)

    if not output_format:
        raise ValueError('The format is not supported')
    return output_format

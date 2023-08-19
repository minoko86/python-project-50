from gendiff.formatters import stylish, plain, json


def formatting(format):

    INFERENCE_FORMATS = {
        'stylish': stylish.format,
        'plain': plain.format,
        'json': json.format
    }

    output_format = INFERENCE_FORMATS.get(format)

    if not output_format:
        raise ValueError('The format is not supported')
    return output_format

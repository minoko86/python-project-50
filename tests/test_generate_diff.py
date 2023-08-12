import pytest
import os
from gendiff import generate_diff


@pytest.fixture(scope="function")
def received_files(request):
    file1, file2, result_file_name, format_name = request.param

    fixtures_path = os.path.join(os.path.dirname(__file__), "fixtures")

    with open(os.path.join(fixtures_path, result_file_name)) as result_file:
        return (
            os.path.join(fixtures_path, file1),
            os.path.join(fixtures_path, file2),
            result_file.read(),
            format_name,
        )


@pytest.mark.parametrize(
    argnames="received_files",
    argvalues=[
        (
            'tree1.json',
            'tree2.json',
            "result.txt",
            "stylish"
        ),
        (
            'tree1.yml',
            'tree2.yml',
            "result.txt",
            "stylish"
        ),
        (
            'tree1.json',
            'tree2.json',
            "result_plain.txt",
            "plain"
        ),
        (
            'tree1.json',
            'tree2.json',
            "json_result.json",
            "json"
        ),
    ],
    indirect=True
)
def test_generate_diff(received_files):
    file1_path, file2_path, result, format_name = received_files

    assert result == generate_diff(file1_path, file2_path, format_name)

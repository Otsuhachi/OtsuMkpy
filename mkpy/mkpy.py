import argparse
import re

from pathlib import Path
from subprocess import Popen

parser = argparse.ArgumentParser()
parser.add_argument('name', help='Name of the file to create.')
parser.add_argument('-c',
                    '--case',
                    choices=['u', 'l', 'd', 'p', 'upper', 'lower', 'default', 'paiza'],
                    default='paiza',
                    help='File naming convention. Default case is paiza.')


def create_paiza_name(name: str) -> str:
    """Create a name for the naming convention "paiza".

    Args:
        name (str): File name.

    Raises:
        ValueError: If "name" is out of format.

    Returns:
        str: "name" formatted in the format "paiza".
    """
    if (find := re.search('^([a-zA-Z])(\\d{1,3})$', name.strip())):
        initial, num = find.groups()
        return initial.upper() + f'{int(num):03d}'
    else:
        raise ValueError


def main() -> None:
    """Create a Python file based on the command line arguments.
    """
    args = parser.parse_args()
    name: str = args.name
    case: str = args.case
    if case in ('l', 'lower'):
        name = name.lower()
    elif case in ('u', 'upper'):
        name = name.upper()
    elif case in ('p', 'paiza'):
        name = create_paiza_name(name)
    name = name.strip() + '.py'
    fp = Path(name)
    if not fp.exists():
        fp.touch()

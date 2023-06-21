"""
CLI UTIL to validate version numbers.
Uses basic python, no extra imports.
"""
import argparse


def format_version(version:str):
    """
    Takes in a string that is a typical version M.M.P (1.0.2) for example.
    :param version: str
    :return: list [1,0,2]
    """
    try:
        return [int(number) for number in version.split('.')]
    except ValueError:
        return 0

def validate_versions(version1: str, version2: str) -> int:
    """
    Validate versions ensures that the two numbers

    There is an edge case in the problem.
    Where both versions are the same passed in it returns -1 as the first isn't greater.

    :param version1: a string ie "1.0.0"
    :param version2: a string of "1.2.0"
    :return: int
    """
    # Format it so they're easier to handle.
    version1 = format_version(version1)
    version2 = format_version(version2)

    if version1 == 0 or version2 == 0:
        # Invalid data was supplied, early exit.
        return 0

    # Even out both sides for edge cases.
    version2.extend([0] * (len(version1) - len(version2)))
    version1.extend([0] * (len(version2) - len(version1)))

    # Compare versions
    for i in range(len(version1)):
        if version1[i] > version2[i]:
            return 1
        elif version1[i] < version2[i]:
            return -1

    # Same version
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()#
    parser.add_argument('--version1', type=str, required=True)
    parser.add_argument('--version2', type=str, required=True)
    args = parser.parse_args()
    print(validate_versions(args.version1, args.version2))

from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="higher-lower",
    description="Functions for finding numbers using higher/lower",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/higher-lower",
    project_urls={
        "Issues": "https://github.com/simonw/higher-lower/issues",
        "CI": "https://github.com/simonw/higher-lower/actions",
        "Changelog": "https://github.com/simonw/higher-lower/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["higher_lower"],
    install_requires=[],
    extras_require={"test": ["pytest", "hypothesis"]},
    tests_require=["higher-lower[test]"],
    python_requires=">=3.6",
)

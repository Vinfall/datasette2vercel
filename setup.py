import os

from setuptools import setup

VERSION = "0.15.0"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette2vercel",
    description="Datasette plugin to deploy on Vercel",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison, Vinfall",
    url="https://github.com/Vinfall/datasette2vercel",
    project_urls={
        "Issues": "https://github.com/Vinfall/datasette2vercel/issues",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["datasette2vercel"],
    entry_points={"datasette": ["publish_vercel = datasette2vercel"]},
    install_requires=["datasette>=0.59"],
    extras_require={"test": ["pytest"]},
    tests_require=["datasette2vercel[test]"],
)

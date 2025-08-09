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
    url="https://github.com/Vinfall/datasette2vercel",
    version=VERSION,
    packages=["datasette2vercel"],
    entry_points={"datasette": ["publish_vercel = datasette2vercel"]},
)

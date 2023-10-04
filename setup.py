import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme_file:
    readme_content = readme_file.read()

setup(
    name="compose",
    version="0.0.1",
    author="Fabrice Normandin",
    author_email="fabrice.normandin@gmail.com",
    long_description_content_type="text/markdown",
    long_description=readme_content,
    url="https://github.com/lebrice/compose",
    package_data={"compose": ["py.typed"]},  # NOTE: Not sure why I'm doing this here.
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["compose"],
    python_requires=">=3.8",
)

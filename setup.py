#!/usr/bin/env python3
import pathlib

from setuptools import setup

HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="dmr-kaitai",
    description="Various DMR related protocols implemented with kaitai-first approach",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/OK-DMR/dmr-kaitai",
    author="Marek Sebera",
    author_email="marek.sebera@gmail.com",
    license="AGPL-3.0",
    version="0.1",
    packages=[
        "okdmr",
        "okdmr.kaitai",
        "okdmr.kaitai.etsi",
        "okdmr.kaitai.homebrew",
        "okdmr.kaitai.hytera",
        "okdmr.kaitai.motorola",
    ],
    zip_safe=True,
    scripts=[],
    keywords="dmr kaitai ham mmdvm homebrew radio hytera motorola",
    python_requires="~=3.7",
    install_requires=[
        "kaitaistruct>=0.9",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Environment :: Console",
        "Topic :: Communications :: Ham Radio",
        "Operating System :: POSIX :: Linux",
        "Typing :: Typed",
        "Framework :: Pytest",
        "Framework :: Flake8",
        "Intended Audience :: Telecommunications Industry",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
    ],
)

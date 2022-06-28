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
    version="1.0",
    packages=[
        "okdmr.kaitai.etsi",
        "okdmr.kaitai.homebrew",
        "okdmr.kaitai.hytera",
        "okdmr.kaitai.motorola",
        "okdmr.kaitai.tools",
    ],
    zip_safe=True,
    entry_points={
        "console_scripts": [
            "debug-motorola-ars=okdmr.kaitai.tools.debug_motorola:DebugMotorola.ars",
            "debug-motorola-tmp=okdmr.kaitai.tools.debug_motorola:DebugMotorola.tmp",
            "debug-hytera-rrs=okdmr.kaitai.tools.debug_hytera:DebugHytera.rrs",
            "debug-hytera-tmp=okdmr.kaitai.tools.debug_hytera:DebugHytera.tmp",
            "debug-hytera-ipsc=okdmr.kaitai.tools.debug_hytera:DebugHytera.ipsc",
            "debug-hytera-rcp=okdmr.kaitai.tools.debug_hytera:DebugHytera.rcp",
            "debug-hytera-dds=okdmr.kaitai.tools.debug_hytera:DebugHytera.dds",
            "debug-hytera-hdap=okdmr.kaitai.tools.debug_hytera:DebugHytera.hdap",
            "debug-hytera-hrnp=okdmr.kaitai.tools.debug_hytera:DebugHytera.hrnp",
            "debug-hytera-hstrp=okdmr.kaitai.tools.debug_hytera:DebugHytera.hstrp",
            "debug-hytera-lp=okdmr.kaitai.tools.debug_hytera:DebugHytera.lp",
            "debug-hytera-dtp=okdmr.kaitai.tools.debug_hytera:DebugHytera.dtp",
            "debug-hytera-tp=okdmr.kaitai.tools.debug_hytera:DebugHytera.tp",
            "debug-homebrew=okdmr.kaitai.tools.debug_homebrew:DebugHomebrew.homebrew",
            "debug-mmdvm=okdmr.kaitai.tools.debug_homebrew:DebugHomebrew.mmdvm",
        ],
    },
    scripts=[],
    keywords="dmr kaitai ham mmdvm homebrew radio hytera motorola",
    python_requires="~=3.7",
    install_requires=[
        "kaitaistruct>=0.9",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Environment :: Console",
        "Topic :: Communications :: Ham Radio",
        "Topic :: Software Development :: Libraries",
        "Operating System :: POSIX :: Linux",
        "Typing :: Typed",
        "Framework :: Pytest",
        "Intended Audience :: Telecommunications Industry",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
    ],
)

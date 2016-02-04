#!/usr/bin/env python

from glob import glob


from setuptools import setup


def parse_requirements(filename):
    with open(filename, "r") as f:
        for line in f:
            if line.startswith("git+http"):
                continue
            if line and line[:2] not in ("#", "-e"):
                yield line.strip()


setup(
    name="setup",
    version="0.0.1",
    description="mailserver setup tool",
    install_requires=list(parse_requirements("requirements.txt")),
    scripts=glob("bin/*"),
)

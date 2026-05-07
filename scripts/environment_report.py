#!/usr/bin/env python
"""Print a lightweight environment report."""

from __future__ import annotations

import importlib.metadata
import platform
import sys
import os


def package_version(name):
    try:
        return importlib.metadata.version(name)
    except importlib.metadata.PackageNotFoundError:
        return "not installed"


def main():
    print("Python:", sys.version.replace("\n", " "))
    print("Platform:", platform.platform())
    print("Machine:", platform.machine())
    print("Processor:", platform.processor())
    print("CPU count:", os.cpu_count())
    for pkg in ["mpmath", "pytest"]:
        print(f"{pkg}: {package_version(pkg)}")


if __name__ == "__main__":
    main()

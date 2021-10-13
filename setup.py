# import sys

# from pkg_resources import VersionConflict, require
# from setuptools import setup

# try:
#     require("setuptools>=38.3")
# except VersionConflict:
#     print("Error: version of setuptools is too old (<38.3)!")
#     sys.exit(1)


# if __name__ == "__main__":
#     setup(use_pyscaffold=True)


from setuptools import setup

with open("README.rst") as f:
    long_description = f.read()

with open("requirements.txt") as f:
    install_requires = f.read().splitlines()

setup(
    name="text_scrambler",
    version="0.1.0",
    packages=[
        "text_scrambler",
    ],
    url="https://text-scrambler.readthedocs.io",
    license="MIT",
    author="GLNB",
    author_email="glnb.dev@gmail.com",
    description="text_scrambler, a tool to scramble texts",
    long_description=long_description,
    install_requires=install_requires,
    project_urls={
        "Documentation": "https://text-scrambler.readthedocs.io",
        "Source": "https://github.com/GuillaumeLNB/text-scrambler",
    },
)

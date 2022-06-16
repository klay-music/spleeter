import setuptools


__VERSION__ = "2.3.0"


setuptools.setup(
    name="spleeter",
    version=__VERSION__,
    author="",
    packages=setuptools.find_packages(where="spleeter"),
    package_dir={"": ""},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)

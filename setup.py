import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mkfont12",
    version="0.1.1",
    author="tantanGH",
    author_email="tantanGH@github",
    license='MIT',
    description="True Type font to X680x0 12dot font data converter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tantanGH/mkfont12",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'mkfont12=mkfont12.mkfont12:main'
        ]
    },
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    install_requires=["Pillow"],
)

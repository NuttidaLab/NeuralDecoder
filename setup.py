import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="InspectorRSA",
    version="0.0.1",
    author="Rudramani Singha",
    author_email="rgs2151@columbia.com",
    description="A package for investigating Representational Similarity Analysis tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NuttidaLab/RSA_Investigations",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        # list your dependencies here, read from requirements.txt
        line.strip() for line in open('requirements.txt')
    ],
)
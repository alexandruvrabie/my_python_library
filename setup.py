from setuptools import setup, find_packages

setup(
    name="code_ph",
    version="0.0.1",
    author="Alexandru Vrabie",
    author_email="sandzel666@gmail.com",
    url="",
    description="Description of lib",
    packages=find_packages(),
    install_requires=[
          'requests',
          'tqdm'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    entry_points={"console_scripts": ["code_ph = code_ph.main:main"]},
)

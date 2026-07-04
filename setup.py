from setuptools import setup, find_packages
import os

# Read the contents of README.md
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="oncodatasets",
    version="0.1.0",
    author="Renzo Caceres Rossi",
    author_email="arenzocaceresrossi@gmail.com",
    description=(
        "A curated collection of oncological, clinical trial, and cancer survival datasets for "
        "data analysis, statistical modeling, and machine learning research. "
        "Includes breast cancer diagnostics, lung and bladder cancer survival analysis, tumor gene expression profiles, "
        "dose-response carcinogen experiments in laboratory animals, patient-reported quality of life (QoL) metrics, "
        "epidemiological incidence and mortality rates, and clinical trial outcomes from curated R packages on CRAN."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lightbluetitan/oncodatasets-py",
    project_urls={
        "Bug Tracker": "https://github.com/lightbluetitan/oncodatasets-py/issues",
        "Documentation": "https://github.com/lightbluetitan/oncodatasets-py",
        "Source Code": "https://github.com/lightbluetitan/oncodatasets-py",
    },
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "oncodatasets": [
            "data/*.csv",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",

        # Audience
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Healthcare Industry",

        # License
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",

        # Topics
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Software Development :: Libraries :: Python Modules",

        # Python Versions
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",

        # OS
        "Operating System :: OS Independent",

        # Language
        "Natural Language :: English",
    ],
    keywords=[
        "oncology", "cancer research", "datasets", "survival analysis", "clinical trials",
        "breast cancer", "lung cancer", "leukemia", "biomedical data", "epidemiology",
        "biostatistics", "tumor genetics", "gene expression", "carcinogenesis", "dose-response",
        "experimental design", "prognostic factors", "data science", "statistics",
        "research", "open science", "open data", "medical statistics",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pandas>=1.5,<3.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov",
            "black",
            "flake8",
            "mypy",
        ],
        "docs": [
            "mkdocs",
            "mkdocs-material",
        ],
    },
    license="GNU General Public License v3 or later (GPLv3+)",
    zip_safe=False,
)
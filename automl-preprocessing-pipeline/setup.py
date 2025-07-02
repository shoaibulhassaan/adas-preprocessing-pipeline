from setuptools import setup, find_packages

setup(
    name="preprocessing_pipeline",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "scikit-learn",
    ],
    author="Shoaib Ul Hassan",
    description="AutoML-style preprocessing pipeline for CSV data",
    include_package_data=True,
    zip_safe=False,
)

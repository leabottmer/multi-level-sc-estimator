from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='multi-levelSC',  # Replace with your package name
    version='0.1.0',           # Increment for new releases
    author='Lea Bottmer',
    author_email='lbottmer@stanford.edu',
    description='This package implements the multi-level synthetic control estimator from "Synthetic Control with Disaggregated Data" (Bottmer, 2025).',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/leabottmer/multi-level-sc-estimator',  # Your GitHub repo URL
    packages=find_packages(),  # Automatically finds all packages in your project
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Or your chosen license
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version required
    install_requires=[
        # List your package dependencies here, e.g.,
        # 'numpy>=1.20',
        # 'pandas',
    ],
    # entry_points={
    #     'console_scripts': [
    #         'your_command = your_package_name.module:main_function',
    #     ],
    # },
)

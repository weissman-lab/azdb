from setuptools import setup, find_packages

setup(
    name='azdb',
    version='0.1',
    packages=find_packages(),
    install_requires=['databricks', 'pandas'
        # List your project's dependencies here.
        # e.g., 'requests>=2.25.1',
    ],
    # Optional metadata
    author='Gary Weissman',
    author_email='garyw@upenn.edu',
    description='A simple python interface for querying Azure databases',
    license='MIT',
    keywords='azure, sql, databases',
)

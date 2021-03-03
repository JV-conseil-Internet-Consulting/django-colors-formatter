from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name = "django-colors-formatter",
    version = "1.0",
    packages = find_packages(),
    exclude_package_data = { 'django_colors_formatter': ['*.pyc'] },
    author="JV conseil",
    author_email="contact@jv-conseil.net",
    description = "Zero-config logging formatter that uses the built-in DJANGO_COLORS setting",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords = "django colors logging formatter DJANGO_COLORS",
    url = "https://github.com/JV-conseil-Internet-Consulting/django-colors-formatter",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

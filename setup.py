import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="jsondbparser",
	version='1.2.1',
	author="Ternowoi Egor",
	author_email="annom2017@mail.ru",
	description="Json-based configuration parser, similar to configparser",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/TheAngryPython/DB-py",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=2.8',
)

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
	name = 'ISA88py',
	version = '0.0.1', 				
	license='MIT',
	description = 'A Python implementation of the state machine defined in ISA 88 / PackML / IEC 61512',
	long_description = long_description,
	long_description_content_type="text/markdown",
	author = 'Aljosha Koecher',
	#author_email = 'your.email@domain.com',
	url = 'https://github.com/aljoshakoecher/ISA88py',
	download_url = 'https://github.com/aljoshakoecher/ISA88py/releases/v.0.0.1',
	keywords = ['StateMachine', 'ISA88', 'Finite State Machine', 'FSM'],
	install_requires=[
    
	],
    tests_require = [
		'pytest',
        'pytest-order'
    ],
	classifiers=[
		'Development Status :: 3 - Alpha',      # "3 - Alpha", "4 - Beta" or "5 - Production/Stable" -> current state of your package
		'Intended Audience :: Developers',      # Define that your audience are developers
		'Topic :: Software Development :: Build Tools',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: 3.9',
	],
	package_dir={"": "src"},
	packages=setuptools.find_packages(where="src"),
	)
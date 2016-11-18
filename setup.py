"""Install setup."""
import setuptools

setuptools.setup(
    name="petrinet_explore",
    version="0.0.1",
    url="git@github.com:xguse/petrinet_explore.git",

    author="Gus Dunn",
    author_email="w.gus.dunn@gmail.com",

    description="Project to explore my ability to explotie petrinets to build and experiment with petrinets from biological pathway formatted data.",
    # long_description=open('README.rst').read(),

    packages=setuptools.find_packages('src'),
    package_dir={"": "src"},


    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    entry_points={
    "console_scripts": [
        "petrinet_explore = petrinet_explore.cli.main:run",
        ]
    },
)

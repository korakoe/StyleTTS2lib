import pathlib
from setuptools import find_packages, setup



with open("requirements.txt", "r", encoding="utf-8") as f:
    required = f.read().splitlines()

setup(
    name="styletts2lib",
    version="0.25.0",
    description="a repository for StyleTTS2",
    long_description=pathlib.Path("README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    Homepage="https://github.com/korakoe/StyleTTS2lib",
    url="https://github.com/korakoe/StyleTTS2lib",
    Issues="https://github.com/korakoe/StyleTTS2lib/issues",
    authors=[{"name": "ButterCream", "email": "korakoe@gmail.com"}],
    license="MIT License",
    package_dir={"": "src"},
    packages=find_packages("src"),
    include_package_data=True,
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    install_requires=required,
)

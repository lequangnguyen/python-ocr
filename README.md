# A Simple Python Optical Character Recognition Application

## Getting Started

### Prerequisites

Kindly ensure you have the following installed on your machine:

- [ ] [Python 3]
- [ ] [Tesseract](https://github.com/tesseract-ocr/tesseract/wiki#installation)
- [ ] [Poppler](https://poppler.freedesktop.org/)
- [ ] [Poetry](https://python-poetry.org/)
- [ ] Git
- [ ] An IDE or Editor of your choice

Please change configuration of Tesseract and Poppler paths in config.ini file following their paths on your own computer in order to run app
### Running the Application

1. Clone the repository
```
$ git clone https://github.com/lequangnguyen/python-ocr.git
```

2. Check into the cloned repository
```
$ cd python-ocr
```

3. You are using Poetry to nstall the dependencies in pyproject.toml
```
$ poetry install
```

4. Run OCR server
```
For example:
$ python main.py --input=input_files/scansmpl_1.png --output=scansmpl_1.txt --verbose
Options:
  --input TEXT   file input path  [required] . Only accept extensions including .jpg, .jpeg, .png, .pdf
  --output TEXT  file output path  [required]. Output file extension should be .txt or .text!
  --verbose      output detailed logs, [optional]
  --help         Show this message and exit.

```

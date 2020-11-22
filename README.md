# Multilingual Document Search for Covid-19

## About
Multilingual Document Search for [Covid-19 documents published by MoHFW](https://www.mohfw.gov.in/) in bengali, hindi, tamil, malayalam, marathi, Sindhi and Telugu.

## Inspiration
A multi-language document search platform has the potential to reach and benefit a wide audience.  India's has 22 constitutionally recognized [official languages](https://en.wikipedia.org/wiki/Languages_with_official_status_in_India "Languages with official status in India") and there are [121 languages which are spoken by ~10,000 people](https://indianexpress.com/article/india/more-than-19500-mother-tongues-spoken-in-india-census-5241056/).  We leverage Facebook`s open-sourced the LASER toolkit,  which offers multilingual sentence representations for around 90 languages, written in 28 different alphabets and embeddes all languages jointly in a single shared space (rather than having a separate model for each), to perform multi-lingual similarity search on the documents. 

## Running the app
### Setup using plain python:
- Create the migrations for  the app: 
  `python manage.py makemigrations`
- Run the migrations:
  `python manage.py migrate`

### Running the project (without docker)
- Open a command line window and go to the project's directory.
- `pip install -r requirements.txt && pip install -r dev-requirements.txt`
- `npm install`
- Run the frontend server
	- `npm run start`
- Run the backend server
	- Open another command line window.
	- `workon cov2020` or `source cov2020/bin/activate` depending on if you are using virtualenvwrapper or just virtualenv.
	- From the `root` directory, run `python backend/manage.py runserver`
- The demo is accessible at http://localhost:3000/

### Adding new pypi libs
Add the libname to either requirements.in or dev-requirents.in, then either upgrade the libs with `make upgrade` or manually compile it and then,  install.
`pip-compile requirements.in > requirements.txt` or `make upgrade`
`pip install -r requirements.txt`


## What`s next?
- Document Summarization
- Voice-enabled search

## References
- [MoHFW India](https://www.mohfw.gov.in/)
- [PyCharm IDE](https://www.jetbrains.com/pycharm/)
- [Language-Agnostic Sentence Representations](https://github.com/facebookresearch/LASER)
- [Django](https://www.djangoproject.com/)
- [React](https://facebook.github.io/react/)


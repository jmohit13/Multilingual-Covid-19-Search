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
- Open a command line window and go to the project's root directory.
- Setup the virtual environment. 
	- mkvirtualenv --python=/usr/bin/python3 cov2020
	- workon cov2020
- Install project requirements
	- make compile_install_requirements
		- This install the packages mentioned in the requirements.in file.
		- The requirements can also be installed using the requirements.txt file.
			- `pip install -r requirements.txt && pip install -r dev-requirements.txt`
	- Install the additional dependencies by running `sh initial_setup.sh`
	- Install the npm modules for the frontend
		- `npm install`
- Run the frontend server
	- `npm run start`
- Run the backend server
	- Open another command line window.
	- `workon cov2020` or `source cov2020/bin/activate` depending on if you are using virtualenvwrapper or just virtualenv.
	- From the `root` directory, run `python backend/manage.py runserver`
- The demo is accessible at http://localhost:3000/

### Multi-lingual Search
- Users will be able to retrieve the most relevant documents published by MoHFW, India matching their query.
- Sample Queries
	- Hindi
		- "जिले में पिछले माह से कोरोना की रफ्तार बढ़ गई है। अगस्त में हर रोज औसतन 22 नए मरीज मिल रहे थे, जो इस माह सितंबर में बढ़कर 25 हो गए हैं। कोरोना की रिपोर्ट पॉजिटिव आने के बाद मरीजों की कांट्रेक्ट ट्रेसिंग करने वाले स्वास्थ्य विभाग के डाटा मैनेजर हेमंत कुलश्रेष्ठ बताते हैं कि संक्रमित मरीजों में से 50 फीसद लोग मोहल्लों में क्लीनिक चलाने वाले डॉक्टरों के पास सर्दी, खांसी, बुखार का इलाज करा चुके होते हैं, जब उन्हें आराम नहीं मिलता है, तब वे राज्य सरकार द्वारा स्थापित किए गए फीवर क्लीनिक पर पहुंचते हैं। यहां जांच के बाद वे कोरोना संक्रमित पाए जाते हैं, लेकिन तब तक वे कई लोगों को संक्रमित कर चुके होते हैं।"
	- Malayalam
		- കോവിഡ് മുക്തരാകുന്ന പലര്‍ക്കും രോഗലക്ഷണങ്ങള്‍ നീണ്ടു നിൽക്കുന്നതായാണ് ആരോഗ്യവകുപ്പിന്‍റെ കണ്ടെത്തല്‍. ചെറുപ്പക്കാര്‍ക്ക് പോലും ദീര്‍ഘകാലത്തേക്കു ശ്വാസകോശ പ്രശ്നങ്ങളും മറ്റും കാണുന്നു. 10 മുതല്‍ 15 ശതമാനം പേര്‍ക്കും സാരമായ ആരോഗ്യപ്രശ്നങ്ങള്‍ ബാധിക്കുന്നതായാണ് നിരീക്ഷണം. ഇതിന്റെ അടിസ്ഥാനത്തിലാണ് വ്യാപകമായി പോസ്റ്റ് കോവിഡ് ക്ലിനിക്കുകൾ സ്ഥാപിക്കാനുള്ള തീരുമാനം. പ്രാഥമിക ആരോഗ്യകേന്ദ്രങ്ങള്‍, സാമൂഹ്യ ആരോഗ്യകേന്ദ്രങ്ങള്‍, കുടുംബ ആരോഗ്യകേന്ദ്രങ്ങള്‍ എന്നിവിടങ്ങളില ക്ലിനിക്കുകൾ തുടങ്ങാനാണു നിര്‍ദേശം.

## What`s next?
- Cron Jobs for Web Crawling
- Document Summarization
- Voice-enabled search

## References
- [MoHFW India](https://www.mohfw.gov.in/)
- [PyCharm IDE](https://www.jetbrains.com/pycharm/)
- [Language-Agnostic Sentence Representations](https://github.com/facebookresearch/LASER)
- [Django](https://www.djangoproject.com/)
- [React](https://facebook.github.io/react/)


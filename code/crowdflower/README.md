

## Copy the code

`git clone --recursive`

or if already cloned

`git submodule update --init --recursive`


## Backend
`./back-end/` contains the backend engine of the validate pipeline described in Section 3.2

`deploy.sh` is the entry script to start everything automatically

`routes.py` implements all the validation rules

refer to the `requirements.txt` for all the python requirements

Download the following projects into `./back-end/3rdparty/`

* [Language Tool](https://languagetool.org/download/) tested for 3.0, check the path `./back-end/3rdparty/LanguageTool-3.0/languagetool.jar`
* [CoreNLP](http://nlp.stanford.edu/software/stanford-corenlp-full-2015-04-20.zip) check the path `./back-end/3rdparty/stanford-corenlp-full-2015-04-20/stanford-corenlp-3.5.2.jar`
* [CoreNLP Python Wrapper](https://github.com/raingo/stanford_corenlp_pywrapper) check the path `./back-end//home/yli/workplace/web-apps/gif-caption-CF/3rdparty/stanford_corenlp_pywrapper/build.sh`

## Frontend
`./front-end/` contains the frontend of the semantic validation and the supporting files for crowd flower

1. **./front-end/layout/instructions.md** is the instructions shown to workers
1. **./front-end/data/** contains the scripts to handle crowd float judgments, such as notifying workers

## Rating
`table3-rating` contains the interface to survey answers from the questions in Table 3

Requires flask

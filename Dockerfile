FROM python:3.10.0a2-buster

#Mentioning name for reference
MAINTAINER SUNDEEP_SINGH BAATH

#Creating a work directory 
WORKDIR Users/Melbourne

#Copying the required files to be uploaded along with the docker image
ADD main.py .
ADD requirements.txt .
ADD static/css/app.css  static/css/
ADD templates/app.html templates/
ADD static/js/app.js static/js/
ADD model/columns.json model/
ADD model/HousingPrice.pickle model/
ADD model/melb_data.csv model/
ADD model/Melb_Mean.csv model/
ADD model/Melb_New.ipynb model/


#Running the files required by professor
#CMD [ "python", "main.py" ]
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main.py"]
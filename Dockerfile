# start by pulling the python image
FROM python:3.8-alpine

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

#füge die anderen Python Files hinzu
ADD imputationMean.py /
ADD imputationMedian.py /
ADD imputationMode.py /
ADD deleteMissingValues.py /

CMD ["view.py", "imputationMean.py", "imputationMedian.py", "imputationMode.py", "deleteMissingValues.py"]

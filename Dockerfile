FROM python:3.9
WORKDIR ./
COPY ./requirement.txt ./requirement.txt
RUN pip install -r requirement.txt
COPY ./datagen2.py ./datagen2.py
CMD ["python3","./datagen2.py"]

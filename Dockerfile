FROM python:3.9
WORKDIR ./
COPY ./requirement.txt ./requirement.txt
RUN pip install -r requirement.txt
COPY ./datagen6.py ./datagen6.py
CMD ["python3","./datagen6.py"]

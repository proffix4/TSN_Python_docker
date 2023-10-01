FROM python:3.11.5

LABEL authors="talipov_sn"

WORKDIR /opt/tsn_python_docker

RUN pip3 install requests

COPY main.py .

CMD [ "python3", "main.py"]
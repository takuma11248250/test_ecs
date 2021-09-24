FROM python:3
USER root

RUN apt-get update && apt-get install -y --no-install-recommends \
	curl \
	unzip

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN ./aws/install

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

COPY ./requirements.txt ./opt/column_re.py ./opt/header_transform_rule.json ./
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "column_re.py"]
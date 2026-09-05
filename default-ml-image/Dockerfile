FROM pytorch/pytorch:2.6.0-cuda12.4-cudnn9-runtime

WORKDIR /opt/prefect/default-ml-image/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

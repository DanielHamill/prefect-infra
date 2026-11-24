# Python 3.12 (bettermdptools, used by the RL report, needs >= 3.12; the
# previous pytorch/pytorch:2.6.0 base was Python 3.11). torch and the cuML
# wheels from pip bundle their own CUDA libraries, so GPU jobs still work
# through the NVIDIA runtime.
FROM python:3.12-slim

ENV PIP_NO_CACHE_DIR=1 PYTHONUNBUFFERED=1
WORKDIR /opt/prefect/default-ml-image/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /api-gateway
WORKDIR /api-gateway
COPY requirements.txt /api-gateway/
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /api-gateway/
ARG URL=0.0.0.0:8000
CMD ["sh", "-c", "alembic upgrade head && uvicorn main:app --host 0.0.0.0 --port 8000 --reload"] 
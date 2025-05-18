FROM python:3.12-slim

# set working directory
WORKDIR /app

# create virtual environment to isolate the project dependencies from
# system-level packages
RUN python3 -m venv /env

# Setting these environment variables are the same as running
# source /env/bin/activate. (activating the venv)
ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

# copy requirements to the working dir
COPY requirements.txt .

RUN pip install pip --upgrade
RUN pip install --no-cache-dir -r requirements.txt

# copy application code into the working dir
COPY ./app ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

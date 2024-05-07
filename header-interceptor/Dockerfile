FROM python:3.8

EXPOSE 5000

WORKDIR /opt/header-interceptor

# Install requirements
RUN pip install --upgrade pip \
    && pip install flask requests

# Copying project
COPY . .

# Start application with unbuffered options
CMD ["python", "-u", "app.py"]

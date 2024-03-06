# Use the official Python image as base
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
ENV WORKDIR=/app
WORKDIR $WORKDIR

# Copy the project files to the container
COPY . $WORKDIR

# Install dependencies
#RUN pip install --no-cache-dir -r config/local/requirements.txt

RUN apt-get update && \ 
    apt-get install -y gettext && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir -r config/local/requirements.txt

# Copy env
COPY config/local/.env.local /.env

# Copy entrypoint script and make it executable
COPY config/local/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set entrypoint script
ENTRYPOINT ["/entrypoint.sh"]
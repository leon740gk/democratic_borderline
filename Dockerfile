FROM python:3.8.6-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV SRC=./
ENV SRVPROJDIR=/srv

# Update the default application repository sources list
RUN apt-get update && apt-get install -y \
  gcc \
  procps \
  git \
  vim \
  nginx \
  supervisor \
  tmux \
  htop

# Create application subdirectories
WORKDIR $SRVPROJDIR
RUN mkdir media static logs
VOLUME ["$SRVPROJDIR/logs/"]

# Copy application source code to SRCDIR
COPY $SRC $SRVPROJDIR

# Install Python dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r $SRVPROJDIR/requirements.txt

## Port to expose
EXPOSE 80

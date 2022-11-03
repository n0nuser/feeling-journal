###########
# BUILDER #
###########

# pull official base image
FROM python:3.10-bullseye as builder

# install python dependencies
WORKDIR /home/feeling
COPY requirements.txt .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt


#########
# FINAL #
#########
FROM python:3.10-slim-bullseye

ENV HOME=/var/www
ENV APP_HOME=/var/www/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY --from=builder /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/
COPY feeling/static/webfonts/pacifico.ttf /usr/local/share/fonts/pacifico.ttf
COPY feeling/static/webfonts/sourcesanspro-bold.otf /usr/local/share/fonts/sourcesanspro-bold.otf
COPY feeling/static/webfonts/sourcesanspro-regular.otf /usr/local/share/fonts/sourcesanspro-regular.otf

USER root
RUN groupadd -r feeling && useradd -m -r -g feeling feeling
RUN apt-get -y update \
  && apt-get install -y libpango-1.0-0 libpangoft2-1.0-0 libjpeg-dev libopenjp2-7-dev libffi-dev \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

WORKDIR $APP_HOME
COPY feeling .
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh && mkdir staticfiles && chown -R feeling:feeling .

USER feeling
ENV PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/mssql-tools/bin

EXPOSE 8000

LABEL org.opencontainers.image.title="n0nuser/feeling-journal"                                 \
      org.opencontainers.image.description="\
      A web application built with Python and Django."    \
      org.opencontainers.image.source="https://github.com/n0nuser/feeling-journal"             \
      org.opencontainers.image.authors="Pablo González Rubio (https://n0nuser.es)"     \
      org.opencontainers.image.licenses="GPL-3.0"


# CMD ["gunicorn", "feeling.asgi:application", "--bind", ":8000", "--workers", "4", "-k", "uvicorn.workers.UvicornWorker"]
ENTRYPOINT "/entrypoint.sh"
#FROM python:3.11.11
FROM debian:bookworm

EXPOSE 8000

WORKDIR /root

# django dev env
ENV DEBUG_VALUE=1

# app envs
ENV ZDS_VENV="zdsenv"
ENV ZDS_VENV_VERSION="20.24.5"
#ENV ZDS_PIP_VERSION="20.24.5"
ENV ZDS_NODE_VERSION="18"

RUN apt-get update && apt-get install -y git wget curl unzip coreutils python3-virtualenv python3-dev python3-pip python3-venv python3-setuptools python3-sqlparse python3-lxml libxml2-dev libxslt-dev libz-dev libjpeg62-turbo libjpeg62-turbo-dev libfreetype6 libfreetype6-dev libffi-dev build-essential imagemagick librsvg2-bin xzdec dh-autoreconf

RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash && \
    export NVM_DIR=/root/.nvm && \
    [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" && \
    nvm install --lts && \
    npm install -g yarn && \
    git clone --depth 1 https://www.github.com/xterler159/zds-site.git && \
    cd zds-site/zmd && \
    npm install && \
    cd node_modules/zmarkdown && \
    npm run server && \ 
    cd $HOME/zds-site && \
    pip install --break-system-packages -r requirements-dev.txt && \
    python3 manage.py migrate && \
    python3 manage.py loaddata fixtures/*.yaml && \
    python3 manage.py load_factory_data fixtures/advanced/aide_tuto_media.yaml && \
    python3 manage.py load_fixtures --size=low --all

WORKDIR zds-site/

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
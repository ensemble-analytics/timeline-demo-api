FROM python:3.11

WORKDIR /

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Copy poetry.lock* in case it doesn't exist in the repo
COPY ./pyproject.toml ./poetry.lock* /

# Allow installing dev dependencies to run tests
RUN bash -c "poetry install"

ENV PYTHONPATH=/

COPY ./app /app
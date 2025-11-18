FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

# Install minimal build deps required by some wheels (kept small)
RUN apt-get update \
 && apt-get install -y --no-install-recommends build-essential gcc git \
 && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN useradd -m app

# Copy source first, then grant permissions to 'app' user
COPY . /app
RUN chown -R app:app /app && chmod -R u+w /app

USER app

# Copy requirements and install (use --no-cache-dir to save space)
COPY --chown=app:app requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# kick-off HolidayRobot code
CMD ["python", "holidayrobot.py"]
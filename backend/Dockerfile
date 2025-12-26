FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y gcc && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY pyproject.toml .
# A simple way to install deps from pyproject.toml without pdm/poetry in docker if we want simplicity:
# But we used standard deps list style. Let's just install them.
# We'll create a requirements.txt on the fly or just install manually for this demo.
# Better: User should probably generate requirements.txt. 
# For now, let's install the core ones:
RUN pip install "fastapi[all]" tensorflow pandas numpy pydantic-settings sqlmodel yfinance

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

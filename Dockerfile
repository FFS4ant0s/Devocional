FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies (se precisar — ex.: netcat pro wait-for-it ou outros)
RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files (inclusive devocional e wait-for-it.sh)
COPY . .

# Deixar o wait-for-it.sh executável
RUN chmod +x /app/wait-for-it.sh

# Expose port
EXPOSE 8000

# Command to run the app
CMD ["python", "/app/devocional/manage.py", "runserver", "0.0.0.0:8000"]

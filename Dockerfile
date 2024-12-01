FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Update package lists and install system dependencies (e.g., for Python packages requiring compilation)
RUN apt-get update && apt-get install -y --no-install-recommends gcc

# Copy requirements first to leverage Docker caching for dependencies
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose the application port
EXPOSE 5000

# Set the default command to run the application
CMD ["python", "app.py"]

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

EXPOSE 8501

# Command to run the app (Streamlit app assumed to be app.py)
CMD ["streamlit", "run", "app.py"]
# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8501 available for Streamlit
EXPOSE 8501

# Command to run the app (Streamlit app assumed to be app.py)
CMD ["streamlit", "run", "app.py"]
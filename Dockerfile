FROM python:3.9-slim-buster
RUN apt-get update && apt-get install -y \
    libglib2.0-dev \
    libsm6 \
    libxrender-dev \
    libxext6 \
    tk \
    libgl1-mesa-glx \
    libgtk2.0-dev

# Set the working directory inside the container
WORKDIR /app

# Copy the application code and dependencies to the container
COPY . /app

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the server will listen on
EXPOSE 8765

# Start the server when the container starts
CMD ["python", "server.py"]

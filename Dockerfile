FROM python:3.9
RUN apt-get update && apt-get install -y \
    libopencv-dev \
    libboost-dev \
    libgthread-2.0-dev \
    libgtk-3-dev \
    libtbb-dev \
    python3-tk

# Set the working directory inside the container
WORKDIR /app

# Copy the application code and dependencies to the container
COPY . /app


RUN pip install numpy opencv-python tensorflow==2.5.0 pillow
# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt
RUN git clone https://github.com/jgraving/dlclive.git && \
    cd dlclive && \
    git checkout 7d96fbb && \
    python setup.py build && \
    python setup.py install
# Expose the port that the server will listen on
EXPOSE 8765

# Start the server when the container starts
CMD ["python", "server.py"]

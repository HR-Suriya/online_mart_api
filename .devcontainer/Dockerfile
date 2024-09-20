# Use the base Python image
FROM python:3.12.6

# Install required packages
RUN apt-get update && apt-get install -y \
    protobuf-compiler \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /workspace

# Install Poetry
RUN pip install poetry

# Copy project files
COPY . /workspace/

# Compile Protobuf schemas
RUN protoc --python_out=/workspace/app/ --proto_path=/workspace/protobuf /workspace/protobuf/*.proto

# Install dependencies
RUN poetry install

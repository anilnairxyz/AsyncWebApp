# sum_action/Dockerfile

FROM python:3.11-slim

# Set the working directory
WORKDIR /action

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script
COPY calculate_sum.py .

# Entry point to run the script
ENTRYPOINT ["python", "/action/calculate_sum.py"]

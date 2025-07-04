    # Use an official Python runtime as a parent image
    FROM python:3.9-slim-buster

    # Set the working directory in the container
    WORKDIR /app

    # Copy the requirements file and install Python dependencies
    COPY requirements.txt .
    RUN pip install --no-cache-dir -r requirements.txt

    # Copy the Flask application code into the container
    COPY . .

    # Expose port 80 for the Flask application
    EXPOSE 80

    # Set environment variables for Git user identity.
    # These are client-side Git configurations that would be used if this container
    # were to perform Git commit operations. They are read by app.py for display.
    ENV GIT_USER_NAME="user"
    ENV GIT_USER_EMAIL="email@email.com"

    # Command to run the Flask application when the container starts
    CMD ["python", "app.py"]
    
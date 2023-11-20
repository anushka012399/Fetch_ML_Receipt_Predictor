FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the Pipfile and Pipfile.lock to the container
COPY Pipfile Pipfile.lock /app/

# Install Pipenv
RUN pip install pipenv

# Install Python dependencies using Pipenv
RUN pipenv install --system --deploy --ignore-pipfile

# Copy the Streamlit script and the Prophet model pickle file to the container
COPY src/app.py /app
COPY src/prophet_model.joblib /app

# Expose the Streamlit default port
EXPOSE 8542

# Command to run the Streamlit app when the container starts
CMD ["streamlit", "run", "--server.port", "8542", "--server.address", "0.0.0.0", "app.py"]


# Streamlit Receipt Count Predictor for Fetch

This application is a Streamlit-based predictor designed to estimate the total receipt count for Fetch. It requires only a month and a year to make a prediction.

## Usage

Follow the steps below to use this application:

### Prerequisites

1. **Install Docker:**
   - You can install Docker by visiting the [Docker website](https://www.docker.com/get-started) and downloading the appropriate version for your operating system.
   - Alternatively, if you are using macOS and have Homebrew installed, you can install Docker using Homebrew by running the following command in your terminal:
     ```bash
     brew install docker --cask
     ```

### Build and Run the Streamlit Application

2. **Build the Docker Image:**

   Make sure the installed docker app is running.

   Build the Docker image with the Streamlit application by executing the following command in the terminal:
   ```bash
   docker build -t streamlit-app .

3. **Launching the Streamlit Application**

   To start the Streamlit application, run the Docker container using the following command:
   ```bash
   docker run -p 8542:8542 streamlit-app

4. **Accessing the Application**

   Once the Streamlit application is running, open your web browser and navigate to http://0.0.0.0:8542 to utilize the Streamlit Receipt Count Predictor for Fetch.
   
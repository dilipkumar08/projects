# YouTube Channel Data Extraction Project

Welcome to the YouTube Channel Data Extraction Project! This project aims to extract data from YouTube channels using the YouTube Data API, visualize it using Streamlit, and store it in a MongoDB database.

## Overview

This project provides a set of Python scripts and utilities to interact with the YouTube Data API. It allows users to extract various data points from YouTube channels, including channel information, video statistics, and comment data. The extracted data is then stored in a MongoDB database for future analysis and retrieval.

## Features

- **Channel Data Extraction**: Extract basic information about a YouTube channel, such as its title, start date, total views, total subscribers, and total videos.
- **Video Data Extraction**: Retrieve statistics for individual videos, including view count, like count, comment count, and more.
- **Comment Data Extraction**: Extract comments associated with videos, along with information about the commenter.
- **MongoDB Integration**: Store the extracted data in a MongoDB database for persistent storage and future analysis.
- **Interactive Visualization**: Visualize the extracted data using Streamlit, allowing users to interactively explore channel data.

## Getting Started

To get started with the YouTube Channel Data Extraction Project, follow these steps:

1. **Install Dependencies**: Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt

    Obtain YouTube API Key: Obtain an API key from the Google Cloud Console. Enable the YouTube Data API v3 for your project and generate an API key.

    Set Up Environment Variables: Create a .env file in the project directory and set your API key:

    makefile 

API_KEY=your_api_key_here

Run the Streamlit App: Start the Streamlit app to interact with the extracted data:

bash

    streamlit run app.py

Usage

Once the Streamlit app is running, you can:

    Enter a YouTube channel ID to extract and display channel data.
    Use the provided buttons to extract, display, and manipulate data for the specified channel.
    Navigate between different sections to view channel data, video data, and comment data.

Contributing

Contributions to the YouTube Channel Data Extraction Project are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or submit a pull request.

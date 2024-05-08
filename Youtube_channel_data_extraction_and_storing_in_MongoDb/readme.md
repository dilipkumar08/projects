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

## Getting Started (Running the Project)

To get started with the YouTube Channel Data Extraction Project, follow these steps:

1. **Install Dependencies**: Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   
2. Obtain YouTube API Key: Obtain an API key from the [Google Cloud Console](https://console.cloud.google.com/). Enable the YouTube Data API v3 for your project and generate an API key.

3. Set Up Environment Variables: Create a .env file in the project directory 

4. Open the `source_code` directory.
   
5. save the `youtube.py` and `YTDE_FE.py` files.

6. Replace the `API_KEY` variable with your YouTube API key.

7. Run the script using Python:

   ```bash
   streamlit run YTDE_FE.py


## Usage

Once the Streamlit app is running, you can:

- **Enter a YouTube Channel ID**: Input the YouTube channel ID into the text field provided to extract and display channel data.

- **Extract, Display, and Manipulate Data**: Utilize the provided buttons to perform various actions such as extracting data, displaying data, and manipulating data for the specified channel.

- **Navigate Between Sections**: Easily navigate between different sections of the application to view channel data, video data, and comment data. The application provides a seamless experience for exploring the extracted YouTube data.


## Contributing

Contributions to the YouTube Channel Data Extraction Project are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or submit a pull request.


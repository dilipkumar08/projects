# PhonePe Data Visualization and Exploration

## Overview

This Streamlit application offers a comprehensive exploration and visualization tool for PhonePe data stored in a MySQL database. Users can delve into various aspects of PhonePe data, including transactions, insurance, and user activity, through interactive charts and analysis tools.

## Key Functionalities

### Data Visualization:

- Explore various aspects of PhonePe data such as transactions, insurance, and user activity.
- Choose between aggregate, map-based, and top data visualization for each category.
- Utilize interactive charts for data exploration.
- Filter data by year and quarter for deeper insights.

### Analysis:

- Identify top and bottom performing districts and pincodes based on transactions, insurance, or user activity.
- Analyze user data by mobile device brand and app open count.

## How to Use the App

1. **Run the Application**: Ensure Python and Streamlit are installed. Navigate to the project directory in your terminal and run `streamlit run app.py`.
   
2. **Explore the App**:
   - Utilize the sidebar menu to navigate between "Home," "Data Visualization," and "Analysis" sections.
     - **Home**: Provides a brief overview of PhonePe and its features.
     - **Data Visualization**: Select the data category, type, and filter by year and quarter to view visualizations.
     - **Analysis**: Choose the data type and analysis type to explore trends.

## Technical Details

- This application is built using Python libraries such as Streamlit, pandas, and plotly.express for data manipulation and visualization.
- It connects to a MySQL database to retrieve PhonePe data.

## Note

- Certain functionalities might be restricted for data before a specific year or quarter due to changes in data storage structure by PhonePe.

This README provides a basic overview of the application's functionalities. Feel free to explore the app further to gain insights into PhonePe data!

### Requirements.txt

```plaintext
streamlit: The core library for creating Streamlit web applications.
streamlit_option_menu: Enables creating dropdown menus for user interaction.
phonepe: Your custom library containing functions for database interaction, data retrieval, and visualizations for PhonePe data.
pandas: Provides data manipulation and analysis capabilities.
plotly.express: Creates interactive charts for data visualization.

Using the Code

To utilize the provided codebase for your own data visualization and exploration project,
you need to follow a few simple steps. First, ensure you have Python and the required libraries installed.
Once done, clone the repository to your local machine and navigate to the project directory.
Within the project, you'll find the stream.py file, which serves as the entry point for the Streamlit application. 
You can modify this file to customize the application according to your specific requirements. 
Additionally, you need to update the database credentials within the phonepe.py file located in the utils directory, 
ensuring that it reflects the connection details of your MySQL database. After making these adjustments, you can run the application by executing 
the command streamlit run stream.py in your terminal. This will launch the Streamlit server, allowing you to access the application through your web browser.
From there, you can explore and visualize your own dataset, gaining valuable insights tailored to your needs.

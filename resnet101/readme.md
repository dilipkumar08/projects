
---

# ResNet Image Classifier

This repository contains a Streamlit app that uses a pretrained ResNet-101 model to classify images.

## Features

- Upload and display an image
- Classify the image using ResNet-101
- Show confidence score
- Progress bar during processing

## Setup

### Prerequisites

- Python 3.x
- Pip

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/resnet-image-classifier.git
    cd resnet-image-classifier
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Download ImageNet class labels:
    ```bash
    wget https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json -O imagenet_classes.txt
    ```

## Usage

1. Run the app:
    ```bash
    streamlit run app.py
    ```

2. Open [http://localhost:8501](http://localhost:8501) in your browser.

## License


---

Feel free to adjust the URL and any other specific details as needed.

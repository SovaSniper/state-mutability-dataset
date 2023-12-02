# State Mutability Predictor

The State Mutability Predictor is a machine learning model designed to predict the state mutability of Application Binary Interfaces (ABIs) in Ethereum smart contracts. ABIs describe the methods and functionality of smart contracts and are essential for interacting with the Ethereum blockchain.

## Purpose

- **State Mutability Prediction**: The primary purpose of this project is to classify ABIs based on their state mutability. State mutability categorizes functions as either mutable (capable of altering the contract's state) or immutable (read-only, incapable of altering the state).

- **Unverified ABI Analysis**: Many Ethereum smart contracts are deployed with unverified ABIs, making it challenging to understand their behavior. This tool helps classify and analyze unverified ABIs to provide insights into their functionality.

- **BERT-Based Classification**: The model leverages a BERT (Bidirectional Encoder Representations from Transformers) architecture for ABI classification, demonstrating the effectiveness of transformer-based models in text classification tasks.

## Dataset

The dataset used in training and testing the State Mutability Predictor contains over 10,000 ABIs from different smart contracts on various blockchains. This dataset has been preprocessed and balanced to create a standardized dataset for model training. This currently includes ABIs from the following blockchains:
- Ethereum
- Polygon
- Avalanche

The preprocessing and balancing steps ensure that the dataset is representative of different state mutability categories and avoids bias in the model. The dataset is available in a convenient format for training the model.
- `balanced-18k.csv`: Contains 18,000 ABIs, with around 4,500 ABIs for each state mutability category
- `balanced-24k.csv`: Contains 24,000 ABIs, with 8,000 ABIs for each state mutability category

## Getting Started

To get started with the State Mutability Predictor, you can choose to run the provided Jupyter Notebook in Google Colab or set up a local environment on your device. Additionally, you can use the dataset available in this repository, but please note that it contains data imbalances and is not considered balanced.

### Running on Google Colab

1. Click the following link to open the State Mutability Predictor Jupyter Notebook in Google Colab:
   [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/link-to-your-colab-notebook)

2. In Google Colab, make sure to enable GPU support for faster training and inference. Go to `Runtime` > `Change runtime type`, select "GPU" for the Hardware accelerator, and click "Save".

3. Follow the instructions in the Jupyter Notebook for training the state mutability prediction model and making predictions.

### Running Locally

1. Clone this repository to your local machine.

2. Install the required dependencies by running the following command:
```bash
pip install -r requirements.txt
```

## Usage

Detailed instructions and code examples for training the model and making predictions can be found in the project's documentation.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

We'd like to express our gratitude to the Ethereum and blockchain communities for their valuable contributions and to the developers behind the BERT model and transformer architecture for their groundbreaking work.

---

Feel free to add or modify any additional information as per your project's specific details and requirements.

# ThinkLab Sentiment Analyzer

**NLP-based Product Review Sentiment Classification System**

ThinkLab Sentiment Analyzer is a Natural Language Processing application developed to classify customer product reviews into three sentiment categories:

- 🔴 Negative
- 🟡 Neutral
- 🟢 Positive

The project applies a complete NLP workflow, compares multiple Machine Learning and Deep Learning models, selects the best-performing model, and integrates it into a Streamlit web application.

---

## Project Information

| Item | Details |
|---|---|
| Project | NLP-based Product Review Sentiment Classification System |
| Application | ThinkLab Sentiment Analyzer |
| Team | ThinkLab Team |
| Course | CCS3356 Natural Language Processing |
| Dataset | Women's E-Commerce Clothing Reviews |
| Final Model | BERT |
| Final Model Accuracy | 81.82% |
| Final Model Macro F1 | 0.6600 |

---

## Project Overview

Online product reviews provide valuable information about customer opinions and experiences. Manually analyzing large numbers of reviews can be time-consuming and inefficient.

This project uses Natural Language Processing to automatically analyze product reviews and classify them according to their sentiment.

The system follows a complete workflow from dataset preparation to final application deployment.

---

## Dataset

**Dataset:** Women's E-Commerce Clothing Reviews  
**Source:** Kaggle  
**Total Reviews:** 23,486

Customer ratings were mapped into three sentiment classes:

| Rating | Sentiment |
|---|---|
| 1–2 | Negative |
| 3 | Neutral |
| 4–5 | Positive |

### Sentiment Distribution

| Sentiment | Percentage |
|---|---:|
| Positive | 77.5% |
| Neutral | 12.2% |
| Negative | 10.3% |

The dataset is imbalanced, with Positive reviews representing the majority class.

---

## NLP Pipeline

The project follows the main stages of an NLP workflow:

```text
Data Collection
      ↓
Data Preprocessing
      ↓
Exploratory Data Analysis
      ↓
Feature Engineering
      ↓
Model Development
      ↓
Model Evaluation
      ↓
Final Model Selection
      ↓
Application Integration
      ↓
Deployment
```

Different preprocessing and feature representation methods were used depending on the requirements of each Machine Learning and Deep Learning model.

---

## Models Developed

Six models were implemented, evaluated, and compared.

| Model | Type | Accuracy | Macro F1 |
|---|---|---:|---:|
| Logistic Regression | ML | 76.74% | 0.6010 |
| Naive Bayes | ML | 78.13% | 0.5943 |
| Support Vector Machine | ML | **82.06%** | 0.5900 |
| LSTM | DL | 70.22% | 0.4408 |
| CNN | DL | 79.41% | 0.6227 |
| BERT | DL | 81.82% | **0.6600** |

---

## Model Comparison

### Highest Accuracy

**Support Vector Machine (SVM)**

- Accuracy: **82.06%**
- Macro F1: 0.5900

### Best Traditional ML Model by Macro F1

**Logistic Regression**

- Accuracy: 76.74%
- Macro F1: **0.6010**

### Best Deep Learning Model

**BERT**

- Accuracy: **81.82%**
- Macro F1: **0.6600**

---

## Final Model Selection

### BERT

BERT was selected as the final model because it achieved the highest **Macro F1 score of 0.6600**.

Although SVM achieved the highest overall accuracy of **82.06%**, the dataset contains class imbalance. Accuracy alone may therefore give an incomplete representation of performance across all sentiment classes.

Macro F1 gives equal importance to each class, making it more suitable for comparing model performance across Negative, Neutral, and Positive sentiments.

### Final Model Information

| Property | Value |
|---|---|
| Model | BERT (base-uncased) |
| Type | Transformer / Deep Learning |
| Accuracy | 81.82% |
| Macro F1 | 0.6600 |
| Maximum Sequence Length | 128 |
| Output Classes | Negative, Neutral, Positive |

---

## Web Application

The final model is integrated into a Streamlit web application named **ThinkLab Sentiment Analyzer**.

The application provides both individual and bulk sentiment prediction together with model and dataset information.

### Main Features

- Single review sentiment prediction
- Bulk CSV sentiment prediction
- Prediction confidence scores
- Sentiment distribution visualization
- Model comparison dashboard
- CSV result download
- Dataset information
- Final model information
- NLP pipeline overview
- Team contribution information
- Ethics and bias discussion
- Light and dark themes

---

## Application Pages

### Home

Provides an overview of the system including:

- Dataset size
- Final model
- Accuracy
- Macro F1
- Dataset sentiment distribution
- Project summary

### Single Prediction

Allows the user to enter an individual product review and obtain a sentiment prediction.

The predicted sentiment can be:

- Positive
- Neutral
- Negative

### Bulk Prediction

Allows users to upload CSV files containing multiple reviews.

Features include:

- CSV file validation
- Review-column detection
- Maximum 500 reviews per upload
- Empty-review handling
- Prediction progress
- Predicted sentiment
- Confidence scores
- Sentiment distribution
- CSV result download

### Dashboard

Provides model and prediction analytics including:

- Model comparison
- Accuracy comparison
- Macro F1 comparison
- Final model information
- Bulk prediction analytics

### About

Provides additional project information including:

- NLP pipeline
- Dataset information
- Models
- Team members
- Ethics and bias considerations

---

## Repository Structure

```text
ThinkLab-NLP/
│
├── data/
│   └── Dataset-related files
│
├── models/
│   └── Trained model files and supporting model resources
│
├── notebooks/
│   └── NLP preprocessing, experiments and model development
│
├── reports/
│   └── Model comparison and project documentation
│
├── screenshots/
│   └── Project and application screenshots
│
├── src/
│   └── Supporting NLP source code
│
├── videos/
│   └── Project video resources
│
├── webapp/
│   │
│   ├── .streamlit/
│   │   └── config.toml
│   │
│   ├── assets/
│   │   ├── logo.svg
│   │   ├── robot_hero.png
│   │   └── team/
│   │
│   ├── config/
│   │   └── project_data.py
│   │
│   ├── pages/
│   │   ├── 1_Single_Prediction.py
│   │   ├── 2_Bulk_Prediction.py
│   │   ├── 3_Dashboard.py
│   │   └── 4_About.py
│   │
│   ├── services/
│   │   ├── prediction_service.py
│   │   ├── bulk_service.py
│   │   └── ui_service.py
│   │
│   ├── app.py
│   └── requirements.txt
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Running the Web Application Locally

### 1. Clone the repository

```bash
git clone https://github.com/Cpox123/ThinkLab-NLP.git
```

### 2. Open the repository

```bash
cd ThinkLab-NLP
```

### 3. Open the web application directory

```bash
cd webapp
```

### 4. Create a virtual environment

```bash
python -m venv venv
```

### 5. Activate the environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 6. Install dependencies

```bash
pip install -r requirements.txt
```

### 7. Run the application

```bash
streamlit run app.py
```

Streamlit will start the application and provide a local browser URL.

---

## Deployment

A separate repository is maintained for the deployed Streamlit application.

### Main Project Repository

https://github.com/Cpox123/ThinkLab-NLP

### Streamlit Web Application Repository

https://github.com/Cpox123/ThinkLab-NLP-WebApp

The final Streamlit application source is also included in the `webapp/` directory of this main repository.

---

## Technologies Used

### Programming Language

- Python

### Data Processing

- Pandas
- NumPy

### NLP and Machine Learning

- NLTK
- Scikit-learn
- TensorFlow
- Hugging Face Transformers

### Visualization

- Matplotlib

### Web Application

- Streamlit

### Version Control

- Git
- GitHub

---

## Team Members

### Buddhisha Wijerathne — Leader

**Student ID:** CIT-24-01-0118

**Contribution:**  
NLP Pipeline, Model Development, Data Preparation, App Integration & Deployment

### Shalitha Sachithra

**Student ID:** CIT-24-01-0084

**Contribution:**  
NLP Pipeline, Model Development, Evaluation & UI Development

### Pawan Vihanga

**Student ID:** CIT-24-01-0459

**Contribution:**  
NLP Pipeline, Model Development, Testing & Documentation

---

## Team Collaboration

All team members contributed to the NLP pipeline, model development, model comparison, application integration, testing, and final project preparation.

Individual responsibilities were also divided among team members to support the complete development workflow.

---

## Application Testing

The final application was tested using different user inputs and application states.

Testing areas include:

- Positive review prediction
- Neutral review prediction
- Negative review prediction
- Empty review input
- Valid CSV upload
- Invalid CSV input
- Missing review column
- Empty review values
- Bulk row limit
- Prediction confidence output
- Dashboard updates
- CSV result download
- Navigation
- Light theme
- Dark theme

Application testing details can also be maintained in a separate `TESTING.md` file.

---

## Ethics and Bias

The dataset contains customer reviews and may contain class imbalance. This can affect the model's ability to identify minority sentiment classes, especially Neutral reviews.

Model predictions should be treated as automated classifications and should not be considered perfect representations of customer opinions.

The system is trained on a specific product review dataset, so performance may differ when it is used on reviews from other products, platforms, or writing styles.

Macro F1 was considered during model comparison to provide a more balanced evaluation across the three sentiment classes.

---

## Limitations

The current system has several limitations:

- The dataset contains class imbalance.
- The model is trained on women's clothing product reviews.
- Performance may decrease on reviews from unrelated domains.
- Ambiguous reviews may be difficult to classify correctly.
- Sarcasm and complex contextual expressions may be misinterpreted.
- Neutral sentiment can be more difficult to distinguish.
- Bulk prediction is limited to 500 reviews per upload to support stable application usage.

---

## Future Improvements

Possible future improvements include:

- Increasing minority-class training examples
- Further hyperparameter optimization
- Improved class-imbalance handling
- Testing additional Transformer models
- Multilingual sentiment classification
- Explainable AI functionality
- Additional review domains
- More detailed prediction analytics

---

## Git and Collaboration

Git and GitHub were used for project development, version control, individual contributions, collaborative integration, testing, and documentation.

The main project repository contains the NLP pipeline, model development, evaluation, documentation, and final integrated application.

A separate Streamlit repository is maintained for application development and deployment.

---

## Project Summary

The ThinkLab Sentiment Analyzer demonstrates the complete development of an NLP-based sentiment classification system.

Six Machine Learning and Deep Learning models were evaluated, and BERT was selected as the final model based on its Macro F1 performance.

The selected model was integrated into a Streamlit application that supports individual review prediction, bulk sentiment classification, model comparison, analytics, and project documentation.

---

## Copyright

© 2026 ThinkLab Team. All rights reserved.

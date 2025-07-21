# Hotel Reservation Prediction MLOps Application

A complete MLOps pipeline for predicting hotel reservation cancellations using machine learning. This application demonstrates end-to-end ML workflow including data ingestion, preprocessing, model training, deployment, and CI/CD automation.

## 🏨 Overview

This application predicts whether a hotel guest will cancel their reservation based on various booking features. It uses a LightGBM model trained on hotel reservation data and provides a web interface for real-time predictions.

## ✨ Features

- **Machine Learning Pipeline**: Complete ML workflow with data ingestion, preprocessing, and model training
- **Web Application**: Flask-based web interface for making predictions
- **MLOps Integration**: MLflow for experiment tracking and model management
- **CI/CD Pipeline**: Jenkins automation for continuous integration and deployment
- **Cloud Deployment**: Automated deployment to Google Cloud Run
- **Containerization**: Docker support for consistent environments
- **Logging & Monitoring**: Comprehensive logging system

## 🛠️ Technology Stack

- **Machine Learning**: LightGBM, Scikit-learn, Imbalanced-learn
- **Web Framework**: Flask
- **Data Processing**: Pandas, NumPy
- **MLOps**: MLflow
- **Cloud Platform**: Google Cloud Platform (Cloud Run, Container Registry)
- **CI/CD**: Jenkins
- **Containerization**: Docker
- **Configuration**: YAML-based configuration management

## 📊 Model Features

The model predicts reservation cancellations based on:

- **Lead Time**: Days between booking and arrival
- **Special Requests**: Number of special requests made
- **Average Price per Room**: Room pricing information
- **Arrival Details**: Month and date of arrival
- **Market Segment**: Type of market segment (Aviation, Corporate, Online, etc.)
- **Stay Duration**: Number of weeknight and weekend nights
- **Meal Plan**: Type of meal plan selected
- **Room Type**: Reserved room type

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Docker (optional)
- Google Cloud SDK (for deployment)

### Local Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd mlops
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -e .
   ```

4. **Train the model**
   ```bash
   python pipeline/training_pipeline.py
   ```

5. **Run the application**
   ```bash
   python application.py
   ```

6. **Access the application**
   Open your browser and navigate to `http://localhost:8080`

### Docker Deployment

1. **Build the Docker image**
   ```bash
   docker build -t hotel-prediction .
   ```

2. **Run the container**
   ```bash
   docker run -p 8080:8080 hotel-prediction
   ```

## 📁 Project Structure

```
mlops/
├── application.py              # Flask web application
├── pipeline/
│   └── training_pipeline.py   # ML training pipeline
├── src/
│   ├── data_ingestion.py      # Data loading and splitting
│   ├── data_preprocessing.py   # Data cleaning and feature engineering
│   ├── model_training.py      # Model training with MLflow
│   ├── logger.py              # Logging configuration
│   └── custom_exception.py    # Custom exception handling
├── config/
│   ├── config.yaml            # Configuration parameters
│   ├── model_params.py        # Model hyperparameters
│   └── path_config.py         # File paths configuration
├── templates/
│   └── index.html             # Web interface template
├── static/
│   └── style.css              # Web interface styling
├── utils/
│   └── common_function.py     # Utility functions
├── artifacts/                 # Generated artifacts (models, data)
├── logs/                      # Application logs
├── mlruns/                    # MLflow experiment tracking
├── Dockerfile                 # Docker configuration
├── Jenkinsfile               # CI/CD pipeline configuration
├── requirements.txt          # Python dependencies
└── setup.py                  # Package setup
```

## 🔄 CI/CD Pipeline

The Jenkins pipeline automates:

1. **Source Code Management**: Clones repository from GitHub
2. **Environment Setup**: Creates virtual environment and installs dependencies
3. **Docker Build**: Builds and pushes Docker image to Google Container Registry
4. **Cloud Deployment**: Deploys to Google Cloud Run

### Pipeline Stages

- **Code Checkout**: Pulls latest code from GitHub
- **Dependency Installation**: Sets up Python environment
- **Docker Image Build**: Creates containerized application
- **Cloud Deployment**: Deploys to Google Cloud Run with auto-scaling

## 📈 MLflow Integration

- **Experiment Tracking**: Logs model parameters, metrics, and artifacts
- **Model Registry**: Manages model versions and lifecycle
- **Metrics Monitoring**: Tracks accuracy, precision, recall, and F1-score
- **Artifact Storage**: Stores trained models and preprocessing objects

## 🌐 Web Interface

The Flask web application provides:

- **User-friendly Form**: Input fields for all prediction features
- **Real-time Predictions**: Instant results upon form submission
- **Responsive Design**: Works on desktop and mobile devices
- **Clear Results**: Easy-to-understand prediction outcomes

## 📊 Model Performance

The LightGBM model is optimized using:

- **Hyperparameter Tuning**: RandomizedSearchCV for optimal parameters
- **Cross-validation**: Robust model evaluation
- **Feature Selection**: Top 10 most important features
- **Class Balancing**: Handles imbalanced dataset

## 🔧 Configuration

### Model Parameters
Configure model hyperparameters in `config/model_params.py`

### Data Processing
Adjust data processing settings in `config/config.yaml`:
- Feature selection criteria
- Categorical/numerical column definitions
- Data splitting ratios

### Paths
Modify file paths in `config/path_config.py`

## 🚀 Deployment

### Google Cloud Run
The application is automatically deployed to Google Cloud Run through the Jenkins pipeline, providing:
- **Auto-scaling**: Scales based on traffic
- **HTTPS**: Secure connections
- **Global Access**: Available worldwide
- **Cost-effective**: Pay-per-use pricing

## 📝 Logging

Comprehensive logging system tracks:
- Application events
- Model training progress
- Prediction requests
- Error handling

Logs are stored in the `logs/` directory with daily rotation.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 🆘 Support

For issues and questions:
1. Check the logs in the `logs/` directory
2. Review MLflow experiments for model performance
3. Verify configuration files
4. Check Docker container logs if using containerized deployment

---

*This application demonstrates modern MLOps practices including automated pipelines, experiment tracking, and cloud deployment for production-ready machine learning systems.*

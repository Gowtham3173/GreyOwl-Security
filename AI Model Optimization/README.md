# AI Model Optimization Project

### Project Overview

This project focuses on optimizing the threat detection AI model in GreyOwl Security to reduce false positives. By refining model thresholds, preprocessing, and feature weights, we aim to improve detection accuracy and reduce unnecessary alerts.

### How to Contribute

1. Fork the repository and create a new branch for your contribution.
2. Check open issues and follow the guidelines in `docs/CONTRIBUTING.md`.
3. Submit a pull request and describe your changes.

### Directory Structure

- `src/`: Contains scripts for model training and preprocessing.
- `test/`: Contains tests for model validation and preprocessing.

### Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Logging Configuration

#### Setup and Usage

Logs are configured to track key details in the model's prediction process. All logs are saved to `logs/model_logs.log` by default.

1. **Adjust Logging Levels**
   Use the following code to set the logging level (e.g., `INFO`, `DEBUG`, `ERROR`):

   ```python
   from logging_config import set_logging_level
   set_logging_level('DEBUG')  # Enables detailed logging
   ```

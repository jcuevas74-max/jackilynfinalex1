# Student Service Requests Analysis — Streamlit

This project converts the original Jupyter Notebook analysis into a Streamlit web app.

## Files in this folder

- `app.py` — Streamlit application.
- `requirements.txt` — Python packages required by the app.
- `README.md` — Setup and running instructions.

## 1. Install Python

Make sure Python is installed on your computer.

## 2. Open the project folder

Extract this folder if you downloaded the ZIP file. Open the folder in VS Code, or open a terminal in this folder.

## 3. Install dependencies

Run:

```bash
python -m pip install -r requirements.txt
```

## 4. Start the app

Run:

```bash
python -m streamlit run app.py
```

Streamlit will show a local URL in the terminal, usually `http://localhost:8501`. Open that address in your browser.

## 5. Upload your dataset

Use the upload box in the app to select `student_service_requests.csv`.

The app displays:
- Dataset row and column counts
- First 10 rows
- Column data types
- Frequency tables for categorical columns
- A compact data dictionary
- A missing-values summary

Use **Download Data Dictionary (CSV)** to save the generated data dictionary.

## Notes

The CSV file is uploaded through the app, so it does not need to be stored at the original Google Colab path `/content/student_service_requests.csv`.

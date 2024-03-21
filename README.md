# Movie Recommendation System

## Description

This project is a movie recommendation system implemented in Python using the spaCy module. It utilises NLP techniques to analyse movie descriptions and provides recommendations based on user input. The system considers user age to filter out age-appropriate recommendations.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation

1. Install pandas and spaCy using pip:
    ```
    pip install pandas spacy
    ```

2. Download the spaCy English model:
    ```
    python -m spacy download en_core_web_md
    ```

## Usage

- Ensure you have a file named `movies.txt` containing movie titles, descriptions, and ratings in the format `Title : Description : Rating`.
- Run the script `movie_recommendation.py`.

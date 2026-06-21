# California Housing Price Prediction — Linear Regression vs Gradient Boosting vs XGBoost

A comparison of three regression models on the California Housing dataset, built as part of the **Codebasics Machine Learning for Data Science** course (Ensemble Learning module). The goal is to show how boosting techniques improve on a plain linear baseline, and how XGBoost stacks up against standard Gradient Boosting on both **accuracy** and **training speed**.

## Dataset

[California Housing dataset](https://scikit-learn.org/stable/datasets/real_world.html#california-housing-dataset) (built into scikit-learn via `fetch_california_housing`).

- **20,640 rows**, 8 numeric features (median income, house age, average rooms/bedrooms, population, occupancy, latitude, longitude)
- **Target:** `MedHouseVal` — median house value for a district, in $100,000s
- No missing values

## Models Compared

| Model | R2 Score | Training Time |
|---|---|---|
| Linear Regression | 0.59 | — |
| Gradient Boosting (100 estimators) | 0.77 | ~6 sec |
| XGBoost (100 estimators) | **0.83** | **~0.12 sec** |

**Key takeaway:** XGBoost beats Gradient Boosting on accuracy *and* trains roughly 50x faster, thanks to its optimized, parallelized implementation — making it the clear choice here.

## Tech Stack

- Python
- pandas
- scikit-learn (`LinearRegression`, `GradientBoostingRegressor`, train/test split, metrics)
- XGBoost (`XGBRegressor`)

## How to Run

```bash
git clone <your-repo-url>
cd <repo-name>
pip install pandas scikit-learn xgboost
jupyter notebook xgboost_california_housing.ipynb
```

## Project Structure

```
.
├── xgboost_california_housing.ipynb   # Main notebook: data loading, training, comparison
└── README.md
```

## What I Learned

- How to benchmark multiple regression models on the same train/test split using R2 score and MSE
- Why ensemble methods (Gradient Boosting, XGBoost) outperform a single linear model on non-linear data
- How XGBoost's regularization and parallelization give it a major speed advantage over standard Gradient Boosting at similar or better accuracy

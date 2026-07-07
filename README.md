# Smart_Lender

## 🗺️ Project Lifecycle & Workflow Epics

### 🔹 Epic 1: Data Collection & Architecture Design
* **Data Aggregation:** Ingestion of structural loan transaction records containing socio-economic and core financial applicant variables.
* **Pipeline Architecture:** Modeled transactional boundaries ensuring proper tracking of historical prediction entities mapping directly back to distinct operational models.

### 🔹 Epic 2: Visualizing & Exploratory Data Analysis (EDA)
* **Univariate Distribution:** Analysis of target variable balances and distribution properties of numeric fields (e.g., base applicant income metrics).
* **Bivariate & Multivariate Matrices:** Discovery of linear and non-linear correlations linking historical credit clearings to positive system determinations.

### 🔹 Epic 3: High-Fidelity Data Pre-Processing
* **Data Sanitation:** Automated identification and imputation of missing elements; handling duplicated entities across primary indices.
* **Class Resampling:** Resampling strategies applied to structural targets to prevent algorithmic optimization bias.
* **Feature Scalability:** Normalization of high-variance continuous inputs (e.g., matching loan amounts to specific temporal term periods).

### 🔹 Epic 4: Comparative Predictive Modeling
The system evaluates inference inputs across a multi-model stack to benchmark efficiency and baseline scoring distributions:
1.  **Decision Tree Classifier:** Base rules optimization structure mapping clear split conditions.
2.  **Random Forest Ensemble:** Out-of-bag validation using randomized sub-trees to optimize structural variance.
3.  **K-Nearest Neighbors (KNN):** Distance metric grouping to identify cluster boundaries across historical applications.
4.  **XGBoost (Extreme Gradient Boosting):** Optimized gradient boosted decision tree tree structures to achieve peak production evaluation accuracy.

### 🔹 Epic 5: Production Application Interface
* **Backend Framework:** High-performance, lightweight asynchronous Python routing engine written in Flask.
* **Frontend Ecosystem:** Clean, responsive HTML dashboard interface built on modern UI grids with native input controls matching the application schema.
* **Cloud Architecture:** Fully containerized Docker configuration compiled for automated, serverless deployment to cloud runtimes (e.g., Hugging Face Spaces).

---

## 🛠️ Technology Stack & Dependencies
* **Core Logic Language:** Python 3.10+
* **Web Ingestion Application:** Flask, Gunicorn
* **Data Operations Framework:** Pandas, NumPy
* **Inference & Math Models:** Scikit-Learn, XGBoost
* **Container Virtualization:** Docker (Debian/Slim footprint layer)


## DEMO LINK
  (https://huggingface.co/spaces/Pavani24/Smart_Lender)

# ✅ DVC Pipeline Setup - Complete Summary

## 🎯 Current Status: WORKING!

Your ML pipeline is fully functional with DVC tracking. Here's what works and the workarounds for Windows-specific issues.

---

## 🚀 **RECOMMENDED WAY TO RUN EXPERIMENTS**

### Run New Experiment

```powershell
python run_experiment.py
```

This script:

- ✅ Runs the complete pipeline (all 5 stages)
- ✅ Shows metrics and parameters
- ✅ Works reliably on Windows
- ✅ Integrates with DVC for tracking

### View Metrics

```powershell
dvc metrics show
```

Output:

```
Path                  accuracy    auc       precision    recall
reports\metrics.json  0.94005     0.91653   0.8629       0.6859
dvclive\metrics.json  0.94005     0.91653   0.8629       0.6859
```

### View Pipeline Structure

```powershell
dvc dag
```

---

## 📝 Your Pipeline Stages

```yaml
data_ingestion → data_preprocessing → feature_engineering → model_building → model_evaluation
```

1. **Data Ingestion** (`src/data_ingestion.py`)

   - Downloads spam dataset from GitHub
   - Splits into train/test (80/20)
   - Outputs: `data/raw/train.csv`, `data/raw/test.csv`

2. **Data Preprocessing** (`src/data_preprocessing.py`)

   - Text cleaning, tokenization, stemming
   - Label encoding
   - Outputs: `data/interim/train_processed.csv`, `data/interim/test_processed.csv`

3. **Feature Engineering** (`src/feature_engineering.py`)

   - TF-IDF vectorization
   - Outputs: `data/processed/train_tfidf.csv`, `data/processed/test_tfidf.csv`

4. **Model Building** (`src/model_building.py`)

   - Trains Random Forest classifier
   - Outputs: `models/model.pkl`

5. **Model Evaluation** (`src/model_evaluation.py`)
   - Calculates metrics (accuracy, precision, recall, AUC)
   - Outputs: `reports/metrics.json`, `dvclive/metrics.json`

---

## 🔧 DVC Commands That Work

### ✅ Working Commands:

```powershell
# View metrics
dvc metrics show

# View metrics differences
dvc metrics diff

# View pipeline DAG
dvc dag

# Check status
dvc status

# View plots
dvc plots show
```

### ❌ Commands with Windows Issues:

**`dvc repro`** - Has run cache path issues on Windows

```
ERROR: [WinError 3] The system cannot find the path specified
```

**Workaround**: Use `python run_pipeline.py` or `python run_experiment.py`

**`dvc exp run`** - Has permission/lock issues on Windows

```
ERROR: [Errno 13] Permission denied
```

**Workaround**: Use `python run_experiment.py`

---

## 🧪 Running Experiments

### Workflow for Parameter Tuning:

1. **Edit parameters** in `params.yaml`:

```yaml
data_ingestion:
  test_size: 0.20 # Try: 0.15, 0.25, 0.30

feature_engineering:
  max_features: 35 # Try: 50, 100, 200

model_building:
  n_estimators: 22 # Try: 50, 100, 200
  random_state: 2
```

2. **Run experiment**:

```powershell
python run_experiment.py
```

3. **View results**:

```powershell
dvc metrics show
```

4. **Compare** different runs by checking `reports/metrics.json` after each run

---

## 📊 Current Performance

Your model achieves:

- **Accuracy**: 94.01%
- **Precision**: 86.29%
- **Recall**: 68.59%
- **AUC**: 91.65%

This is good performance for spam classification!

---

## 🗂️ File Structure

```
YT-MLOPS-Complete-ML-Pipeline-main/
├── .dvc/                      # DVC configuration
├── .git/                      # Git repository
├── data/
│   ├── raw/                   # Raw CSV files
│   ├── interim/               # Preprocessed text
│   └── processed/             # TF-IDF features
├── models/
│   └── model.pkl              # Trained model
├── reports/
│   └── metrics.json           # Evaluation metrics
├── dvclive/                   # DVCLive tracking
│   ├── metrics.json
│   ├── params.yaml
│   └── plots/
├── src/                       # Source code
│   ├── data_ingestion.py
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── model_building.py
│   └── model_evaluation.py
├── dvc.yaml                   # DVC pipeline definition
├── params.yaml                # Hyperparameters
├── run_pipeline.py            # Run complete pipeline
├── run_experiment.py          # Run as experiment
├── PIPELINE_COMMANDS.md       # Detailed documentation
└── README.md
```

---

## 🎓 Git Workflow

### Current Setup:

```powershell
# You've already done:
git init
git add .
git commit -m "Initial commit for DVC pipeline"
```

### For Future Changes:

```powershell
# After running experiments and changing parameters
git add params.yaml dvc.yaml
git commit -m "Updated parameters: increased n_estimators to 50"

# Push to GitHub
git push origin main
```

---

## 💡 Tips & Best Practices

1. **Version Control**: Commit `dvc.yaml` and `params.yaml` to Git, but not the data/models (DVC handles those)

2. **Experiment Tracking**: Always run `python run_experiment.py` to ensure metrics are logged

3. **Parameter Tuning**: Change one parameter at a time to understand its impact

4. **Documentation**: Update your commit messages with what parameters you changed

5. **Metrics Comparison**: Save `reports/metrics.json` with different names if you want to compare multiple runs

---

## 🔍 Troubleshooting

### Problem: "Permission denied" errors

**Solution**: Close any programs that might have files open (VS Code terminals, Excel, etc.)

### Problem: Can't find Python/DVC

**Solution**: Make sure you're in the virtual environment:

```powershell
.venv\Scripts\Activate.ps1
```

### Problem: NLTK data missing

**Solution**: Scripts automatically download it on first run

### Problem: Module not found

**Solution**:

```powershell
pip install dvc dvclive pandas scikit-learn nltk pyyaml
```

---

## 📚 Next Steps

1. ✅ **Try different parameters** in `params.yaml`
2. ✅ **Run multiple experiments** with `python run_experiment.py`
3. ✅ **Compare results** using `dvc metrics show`
4. ✅ **Document your findings** in commit messages
5. ✅ **Push to GitHub** to share your work

---

## 🎉 Success!

Your DVC pipeline is fully configured and working! You can now:

- ✅ Run reproducible experiments
- ✅ Track parameters and metrics
- ✅ Version control your ML pipeline
- ✅ Compare different model configurations

**Happy experimenting! 🚀**

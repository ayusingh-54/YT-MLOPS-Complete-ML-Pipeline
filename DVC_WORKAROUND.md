# DVC Windows Workaround - Alternative Workflow

## ⚠️ Issue: DVC Cache Commands Don't Work on Windows

The following DVC commands have Windows path/permission issues:
- `dvc repro` - Run cache path error
- `dvc exp run` - Permission denied
- `dvc commit` - Path not found error

## ✅ WORKING ALTERNATIVE WORKFLOW

### Option 1: Use Git for Version Control (Recommended)

Since DVC cache has issues, use Git to track your code and DVC for pipeline definition and metrics only.

#### Step 1: Add data/models to .gitignore (if not already there)
```powershell
# Check if .gitignore exists
if (Test-Path .gitignore) {
    "data/" | Out-File -Append .gitignore
    "models/" | Out-File -Append .gitignore
    "dvclive/" | Out-File -Append .gitignore
}
```

#### Step 2: Run experiments and commit to Git
```powershell
# Run your experiment
python run_experiment.py

# Commit your code and configuration
git add src/ dvc.yaml params.yaml reports/metrics.json
git commit -m "Experiment: changed n_estimators to 50"
git push
```

### Option 2: Disable DVC Cache (Use Copy Mode)

This avoids the cache entirely:

```powershell
# Configure DVC to not use cache
dvc config cache.type copy
dvc config core.hardlink_lock false
dvc config core.no_scm false

# Then try repro without run cache
dvc repro --no-run-cache
```

### Option 3: Use DVC for Tracking Only (No Cache)

Track metrics and parameters without using DVC's cache system:

```powershell
# Run your pipeline
python run_experiment.py

# Use DVC to show metrics (this works!)
dvc metrics show
dvc plots show

# Commit to Git
git add .
git commit -m "Updated experiment results"
```

## 📊 What Still Works with DVC

Even with cache issues, these commands work perfectly:

```powershell
# View metrics - WORKS ✅
dvc metrics show

# Compare metrics - WORKS ✅
dvc metrics diff

# View pipeline DAG - WORKS ✅
dvc dag

# Check status - WORKS ✅
dvc status

# Show plots - WORKS ✅
dvc plots show
```

## 🔧 Recommended Workflow for Your Project

### Daily Workflow:

1. **Edit parameters** in `params.yaml`
2. **Run experiment**:
   ```powershell
   python run_experiment.py
   ```
3. **Check metrics**:
   ```powershell
   dvc metrics show
   ```
4. **Save to Git**:
   ```powershell
   git add params.yaml src/ reports/metrics.json dvc.yaml
   git commit -m "Experiment: describe your changes"
   git push
   ```

### Why This Works:

- ✅ Pipeline runs successfully via Python scripts
- ✅ Metrics are tracked in `reports/metrics.json` and `dvclive/metrics.json`
- ✅ Parameters are versioned in `params.yaml`
- ✅ Code is versioned in Git
- ✅ DVC shows metrics and pipeline structure
- ❌ DVC cache is bypassed (which is fine for small projects)

## 📝 Git Commands for Your Pipeline

### Track Your Experiments:

```powershell
# After running an experiment
git add params.yaml reports/metrics.json
git commit -m "Exp: n_estimators=50, max_features=100"

# View experiment history
git log --oneline

# Compare two experiments
git diff HEAD~1 reports/metrics.json
```

### Create Experiment Branches:

```powershell
# Create branch for parameter tuning
git checkout -b exp/tuning-random-forest

# Make changes, run experiments
python run_experiment.py

# Commit results
git add .
git commit -m "Tuning: best params found"

# Merge back to main
git checkout main
git merge exp/tuning-random-forest
```

## 🎯 Alternative: Use MLflow or Weights & Biases

If you need more robust experiment tracking, consider:

### MLflow (Local):
```powershell
pip install mlflow

# In your model_evaluation.py, add:
import mlflow
mlflow.log_params(params)
mlflow.log_metrics(metrics)

# View experiments
mlflow ui
```

### Weights & Biases (Cloud):
```powershell
pip install wandb

# In your model_evaluation.py, add:
import wandb
wandb.init(project="spam-classifier")
wandb.log(metrics)
```

## 📌 Summary

**Current Status:**
- ✅ Pipeline runs perfectly with `python run_experiment.py`
- ✅ DVC metrics and DAG visualization work
- ❌ DVC cache commands fail on Windows (known issue)

**Recommendation:**
Use Git for version control and DVC for metrics/pipeline definition only. This gives you:
- Full reproducibility
- Experiment tracking
- Version control
- No Windows compatibility issues

**Bottom Line:**
Don't use `dvc commit`, `dvc repro`, or `dvc exp run`. Use `python run_experiment.py` + Git instead! 🎯

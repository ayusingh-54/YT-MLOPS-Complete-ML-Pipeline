# ML Pipeline Commands Guide

## Pipeline Overview

This spam classification ML pipeline consists of 5 stages:

1. **Data Ingestion** - Downloads and splits data
2. **Data Preprocessing** - Text cleaning and encoding
3. **Feature Engineering** - TF-IDF vectorization
4. **Model Building** - Random Forest training
5. **Model Evaluation** - Performance metrics

## Quick Start - Running the Pipeline

### Option 1: Run Complete Pipeline with Python Script (RECOMMENDED for Windows)

```powershell
python run_pipeline.py
```

This will execute all 5 stages sequentially and provide clear status updates.

### Option 2: Run Individual Stages Manually

```powershell
# Stage 1: Data Ingestion
python src/data_ingestion.py

# Stage 2: Data Preprocessing
python src/data_preprocessing.py

# Stage 3: Feature Engineering
python src/feature_engineering.py

# Stage 4: Model Building
python src/model_building.py

# Stage 5: Model Evaluation
python src/model_evaluation.py
```

### Option 3: Run with DVC (if DVC cache issue is resolved)

```powershell
# Initialize DVC (first time only)
dvc init --no-scm

# Run the complete pipeline
dvc repro

# Or run up to a specific stage
dvc repro data_ingestion
dvc repro data_preprocessing
dvc repro feature_engineering
dvc repro model_building
dvc repro model_evaluation
```

## Known Issues

### Windows DVC Cache Issue

There's a known issue with DVC on Windows systems with long path names that causes the error:

```
ERROR: failed to reproduce 'data_ingestion': [WinError 3] The system cannot find the path specified
```

**Workaround**: Use `run_pipeline.py` script or run individual Python scripts manually.

## DVC Commands Reference

### Check Pipeline Status

```powershell
dvc status
```

### View Pipeline DAG (Directed Acyclic Graph)

```powershell
dvc dag
```

### Show Metrics

```powershell
dvc metrics show
```

### Show Metrics Difference

```powershell
dvc metrics diff
```

### Show Plots

```powershell
dvc plots show
```

### List Experiments

```powershell
dvc exp show
```

### View Specific Metrics

```powershell
# View metrics from reports
type reports\metrics.json

# View DVCLive metrics
type dvclive\metrics.json
```

## Parameter Tuning

Edit `params.yaml` to change hyperparameters:

```yaml
data_ingestion:
  test_size: 0.20 # Test set proportion

feature_engineering:
  max_features: 35 # Max TF-IDF features

model_building:
  n_estimators: 22 # Number of trees in Random Forest
  random_state: 2 # Random seed for reproducibility
```

After changing parameters:

1. Run: `python run_pipeline.py`
2. Or run: `dvc repro` (if DVC works)

## Output Directories

- `data/raw/` - Raw train/test CSV files
- `data/interim/` - Preprocessed text data
- `data/processed/` - TF-IDF vectorized features
- `models/` - Trained model (model.pkl)
- `reports/` - Evaluation metrics (metrics.json)
- `dvclive/` - DVCLive experiment tracking data
- `logs/` - Execution logs for each stage

## Viewing Results

### Metrics

```powershell
# JSON format
type reports\metrics.json

# DVCLive metrics
type dvclive\metrics.json
```

### Logs

```powershell
type logs\data_ingestion.log
type logs\data_preprocessing.log
type logs\feature_engineering.log
type logs\model_building.log
type logs\model_evaluation.log
```

### Model

The trained model is saved as `models/model.pkl` and can be loaded with:

```python
import pickle
with open('models/model.pkl', 'rb') as f:
    model = pickle.load(f)
```

## Troubleshooting

### Issue: DVC reproduction fails

**Solution**: Use `python run_pipeline.py` instead

### Issue: Module not found

**Solution**: Install dependencies

```powershell
pip install dvc dvclive pandas scikit-learn nltk pyyaml
```

### Issue: NLTK data not found

**Solution**: Run any script once - NLTK data downloads automatically

### Issue: Permission denied

**Solution**: Run PowerShell as administrator or check folder permissions

## Clean Up

### Remove Generated Data

```powershell
Remove-Item -Recurse -Force data\raw\*, data\interim\*, data\processed\*
Remove-Item -Recurse -Force models\*, reports\*, dvclive\*
```

### Reset DVC

```powershell
Remove-Item -Recurse -Force .dvc
dvc init --no-scm
```

## Git Integration (Optional)

To use DVC with Git:

```powershell
# Initialize Git repo
git init

# Add DVC files
git add .dvc .dvcignore dvc.yaml

# Add source code
git add src/ params.yaml run_pipeline.py

# Commit
git commit -m "Initial commit with DVC pipeline"
```

## Performance Notes

- Data Preprocessing takes ~30-40 seconds (NLTK stemming)
- Model Training takes ~1 second (Random Forest with 22 trees)
- Complete pipeline takes ~1-2 minutes

## Next Steps

1. ✅ Run the pipeline: `python run_pipeline.py`
2. ✅ Check metrics: `type reports\metrics.json`
3. ✅ Modify parameters in `params.yaml`
4. ✅ Re-run to compare results
5. ✅ Track experiments with DVCLive

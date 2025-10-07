"""
Run the complete ML pipeline
"""
import subprocess
import sys

def run_stage(stage_name, script_path):
    """Run a single stage of the pipeline"""
    print(f"\n{'='*60}")
    print(f"Running Stage: {stage_name}")
    print(f"{'='*60}\n")
    
    result = subprocess.run([sys.executable, script_path], capture_output=False)
    
    if result.returncode != 0:
        print(f"\n❌ Error: Stage '{stage_name}' failed with exit code {result.returncode}")
        sys.exit(result.returncode)
    else:
        print(f"\n✅ Stage '{stage_name}' completed successfully")
    
    return result.returncode

def main():
    """Main function to run the entire pipeline"""
    print("\n" + "="*60)
    print("Starting ML Pipeline Execution")
    print("="*60)
    
    stages = [
        ("Data Ingestion", "src/data_ingestion.py"),
        ("Data Preprocessing", "src/data_preprocessing.py"),
        ("Feature Engineering", "src/feature_engineering.py"),
        ("Model Building", "src/model_building.py"),
        ("Model Evaluation", "src/model_evaluation.py")
    ]
    
    for stage_name, script_path in stages:
        run_stage(stage_name, script_path)
    
    print("\n" + "="*60)
    print("✅ Pipeline Execution Completed Successfully!")
    print("="*60)
    print("\nNext Steps:")
    print("1. Check metrics: dvc metrics show")
    print("2. View plots: dvc plots show")
    print("3. Check outputs in:")
    print("   - data/raw/")
    print("   - data/interim/")
    print("   - data/processed/")
    print("   - models/")
    print("   - reports/")
    print("   - dvclive/")

if __name__ == "__main__":
    main()

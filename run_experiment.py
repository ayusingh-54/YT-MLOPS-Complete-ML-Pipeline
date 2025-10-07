"""
Run DVC-like experiments without using 'dvc exp run'
This script runs the pipeline and tracks results like DVC experiments
"""
import subprocess
import sys
import json
import os
from datetime import datetime

def run_pipeline():
    """Run the complete ML pipeline"""
    print("\n" + "="*60)
    print("Running ML Pipeline as Experiment")
    print("="*60)
    
    stages = [
        ("Data Ingestion", "src/data_ingestion.py"),
        ("Data Preprocessing", "src/data_preprocessing.py"),
        ("Feature Engineering", "src/feature_engineering.py"),
        ("Model Building", "src/model_building.py"),
        ("Model Evaluation", "src/model_evaluation.py")
    ]
    
    for stage_name, script_path in stages:
        print(f"\n▶ Running: {stage_name}")
        result = subprocess.run([sys.executable, script_path], capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"❌ Failed: {stage_name}")
            print(result.stderr)
            return False
    
    print("\n✅ Pipeline completed successfully!")
    return True

def show_results():
    """Display experiment results"""
    print("\n" + "="*60)
    print("Experiment Results")
    print("="*60)
    
    # Read metrics
    if os.path.exists('reports/metrics.json'):
        with open('reports/metrics.json', 'r') as f:
            metrics = json.load(f)
        
        print("\n📊 Model Performance Metrics:")
        print("-" * 40)
        for metric, value in metrics.items():
            print(f"  {metric:<15}: {value:.4f}")
    
    # Read parameters
    if os.path.exists('params.yaml'):
        import yaml
        with open('params.yaml', 'r') as f:
            params = yaml.safe_load(f)
        
        print("\n⚙️  Parameters Used:")
        print("-" * 40)
        for section, values in params.items():
            print(f"  {section}:")
            for key, value in values.items():
                print(f"    {key}: {value}")
    
    print("\n" + "="*60)
    print("💡 Tips:")
    print("  - Change parameters in params.yaml")
    print("  - Run this script again to create new experiment")
    print("  - Use: dvc exp show (to view all experiments)")
    print("  - Use: dvc metrics show (to see metrics)")
    print("="*60 + "\n")

def main():
    """Main function"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n🔬 Starting Experiment - {timestamp}")
    
    success = run_pipeline()
    
    if success:
        show_results()
        print("\n✅ Experiment completed and tracked!")
        print("   Run 'dvc exp show' to see all experiments\n")
    else:
        print("\n❌ Experiment failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()

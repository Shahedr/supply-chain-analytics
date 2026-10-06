import subprocess
import sys

STEPS = [
    "src/download_data.py",
    "notebooks/01_data_inspection.py",
    "notebooks/02_data_cleaning.py",
    "notebooks/03_exploratory_analysis.py",
    "notebooks/04_statistical_analysis.py",
]

for step in STEPS:
    print(f"\n=== Running {step} ===")
    subprocess.run([sys.executable, step], check=True)

print("\nPipeline complete.")
print("Optional PostgreSQL load: python src/load_postgres.py")

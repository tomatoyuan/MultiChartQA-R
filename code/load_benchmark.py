from pathlib import Path

from data_utils import load_main_benchmark

if __name__ == "__main__":
    repo_root = Path(__file__).resolve().parents[1]
    benchmark = load_main_benchmark(language="en", benchmark_root=repo_root / "benchmark")
    print("Main benchmark example:")
    for task_id in range(1, 5):
        print(f"task{task_id}:")
        print(benchmark[task_id][0])

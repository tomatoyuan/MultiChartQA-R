from pathlib import Path

from data_utils import load_extended_benchmark, split_extended_by_chart_count

if __name__ == "__main__":
    repo_root = Path(__file__).resolve().parents[1]
    benchmark = load_extended_benchmark(repo_root / "benchmark-extended")
    print("Extended benchmark example:")
    for subset_name, qa_pairs in benchmark.items():
        split_2c, split_3c, split_4c = split_extended_by_chart_count(qa_pairs)
        print(subset_name)
        print("  2-chart:", split_2c[0])
        print("  3-chart:", split_3c[0])
        print("  4-chart:", split_4c[0])

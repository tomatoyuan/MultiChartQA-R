from utils import GetBenchmarkData

if __name__ == "__main__":
    benchmarkData = GetBenchmarkData()
    '''MultiChartQA-X benchmark qa list'''
    task1_qa_list, task2_qa_list, task3_qa_list, task4_qa_list = benchmarkData.get_benchmark_data("en")
    print("benchmark example: ")
    print("task1: ")
    print(task1_qa_list[0])
    print("task2: ")
    print(task2_qa_list[0])
    print("task3: ")
    print(task3_qa_list[0])
    print("task4: ")
    print(task4_qa_list[0])
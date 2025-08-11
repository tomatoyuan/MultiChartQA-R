from utils import GetBenchmarkData

if __name__ == "__main__":

    '''extended-benchmark qa list'''
    benchmarkData = GetBenchmarkData()
    parallel_pcpc_list, parallel_pcmc_list, union_pcpc_list, union_pcmc_list = benchmarkData.get_benchmark_extended_data()
    parallel_pcpc_2c_list, parallel_pcpc_3c_list, parallel_pcpc_4c_list = benchmarkData.split_qa_pairs(parallel_pcpc_list)
    parallel_pcmc_2c_list, parallel_pcmc_3c_list, parallel_pcmc_4c_list = benchmarkData.split_qa_pairs(parallel_pcmc_list)
    union_pcpc_2c_list, union_pcpc_3c_list, union_pcpc_4c_list = benchmarkData.split_qa_pairs(union_pcpc_list)
    union_pcmc_2c_list, union_pcmc_3c_list, union_pcmc_4c_list = benchmarkData.split_qa_pairs(union_pcmc_list)
    print("extended-benchmark example: ")
    print("parallel-pcpc: ")
    print(parallel_pcpc_2c_list[0])
    print(parallel_pcpc_3c_list[0])
    print(parallel_pcpc_4c_list[0])
    print("parallel-pcmc: ")
    print(parallel_pcmc_2c_list[0])
    print(parallel_pcmc_3c_list[0])
    print(parallel_pcmc_4c_list[0])
    print("union-pcpc: ")
    print(union_pcpc_2c_list[0])
    print(union_pcpc_3c_list[0])
    print(union_pcpc_4c_list[0])
    print("union-pcmc: ")
    print(union_pcmc_2c_list[0])
    print(union_pcmc_3c_list[0])
    print(union_pcmc_4c_list[0])

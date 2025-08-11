from utils import Evaluation

if __name__ == "__main__":
    evaluation = Evaluation()

    # task1
    gt = "1.0"
    mllm_ans = "1.01"
    result = evaluation.evaluation_task1(gt, mllm_ans)
    print("task1:", result) # True

    # task2
    language_type = "en"
    gt = "1.0"
    mllm_rationale = "a = 10.0, b = 10.01, c = a / b, result = c"
    result = evaluation.evaluation_task2(language_type, gt, mllm_rationale)
    print("task2:", result) # True

    # task3
    gt = "['A', 'B', 'C']"
    mllm_ans = "['A', 'B', 'C']"
    result = evaluation.evaluation_task3(gt, mllm_ans)
    print("task3:", result) # 1.0

    # task4
    gt = "['A', 'B', 'C']"
    mllm_ans = "['A', 'B', 'D']"
    result = evaluation.evaluation_task4(gt, mllm_ans)
    print("task4:", result) # 0.0


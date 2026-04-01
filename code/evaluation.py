from eval_task1_accuracy import normalize_binary_answer
from eval_task2_accuracy import validate_value
from eval_task34_strict_risk_aware import evaluate_question_strict_risk_aware

if __name__ == "__main__":
    # Task 1
    gt = "Yes"
    pred = "yes"
    result = normalize_binary_answer(gt) == normalize_binary_answer(pred)
    print("task1:", result)

    # Task 2
    gt = "1.0"
    pred = "1.01"
    result = validate_value(gt, pred)
    print("task2:", result)

    # Task 3 / 4
    result = evaluate_question_strict_risk_aware(
        pred_answer=["A", "B", "D"],
        label=["A", "B", "C"],
        easy_error=["E"],
        hard_error=["D", "F"],
    )
    print("task3/4 strict risk-aware:", result)

import os
import re
import sys
import json
import subprocess
from deepseek_api import myDeepSeekAPI

class GetBenchmarkData:
    def __init__(self):
        self.benchmark_path = "../benchmark"
        self.exbenchmark_path = "../benchmark-extended"
    def get_chart_path(self, benchmark_images_path, chart_prefix_list):
        chart_path_list = []
        for chart_prefix in chart_prefix_list:
            chart_path = chart_prefix + ".png"
            chart_path = os.path.join(benchmark_images_path, chart_path)
            chart_path_list.append(chart_path)
        return chart_path_list
    def get_benchmark_data(self, language="en"):
        '''Get benchmark data
            - language: en/cn/es
        '''
        benchmark_path = self.benchmark_path
        benchmark_json_path = os.path.join(benchmark_path, "json", language)
        benchmark_images_path = os.path.join(benchmark_path, "images", language)

        benchmark_data_task1 = []
        benchmark_data_task2 = []
        benchmark_data_task3 = []
        benchmark_data_task4 = []
        start_idx = 1
        end_idx = 180
        for idx in range(start_idx, end_idx+1):
            json_file_path = os.path.join(benchmark_json_path, f"{idx}.json")
            with open(json_file_path, "r") as json_file:
                content = json.load(json_file)
            # print(content["chart"])
            # print(content["qa_pairs"])
            for qa_pair in content["qa_pairs"]:
                chart_list = []
                if qa_pair["type"] == "2":
                    qa_pair["type"] = "1"
                    chart_list = self.get_chart_path(benchmark_images_path, qa_pair["charts_involved"])
                    qa_pair["charts_involved"] = chart_list
                    benchmark_data_task1.append(qa_pair)
                elif qa_pair["type"] == "3":
                    qa_pair["type"] = "2"
                    chart_list = self.get_chart_path(benchmark_images_path, qa_pair["charts_involved"])
                    qa_pair["charts_involved"] = chart_list
                    benchmark_data_task2.append(qa_pair)
                elif qa_pair["type"] == "4":
                    qa_pair["type"] = "3"
                    chart_list = self.get_chart_path(benchmark_images_path, qa_pair["charts_involved"])
                    qa_pair["charts_involved"] = chart_list
                    benchmark_data_task3.append(qa_pair)
                else:
                    qa_pair["type"] = "4"
                    chart_list = self.get_chart_path(benchmark_images_path, qa_pair["charts_involved"])
                    qa_pair["charts_involved"] = chart_list
                    benchmark_data_task4.append(qa_pair)
        return benchmark_data_task1, benchmark_data_task2, benchmark_data_task3, benchmark_data_task4

    def get_exbench_chart_list(self, paper_path, chart_prefix_list):
        chart_list = []
        for chart_prefix in chart_prefix_list:
            chart_prefix = chart_prefix.split("-")[0]
            chart_prefix = chart_prefix.split("_")[-1]
            chart_name = "image_" + chart_prefix + ".png"
            chart_path = os.path.join(paper_path, chart_name)
            chart_list.append(chart_path)
        chart_list = list(set(chart_list))
        return chart_list

    def split_qa_pairs(self, qa_pair_list):
        list_2c = []
        list_3c = []
        list_4c = []
        for qa_pair in qa_pair_list:
            if qa_pair["chart_count"] == "2":
                list_2c.append(qa_pair)
            elif qa_pair["chart_count"] == "3":
                list_3c.append(qa_pair)
            else:
                list_4c.append(qa_pair)
        return list_2c, list_3c, list_4c
    def get_benchmark_extended_data(self):
        '''Get extended benchmark data
        '''
        exbenchmark_path = self.exbenchmark_path

        subfolders = [f for f in os.listdir(exbenchmark_path) 
                if os.path.isdir(os.path.join(exbenchmark_path, f))]
        paper_path_list = [os.path.join(exbenchmark_path, path) for path in subfolders]

        parallel_pcpc_qa_pair_list = []
        parallel_pcmc_qa_pair_list = []
        union_pcpc_qa_pair_list = []
        union_pcmc_qa_pair_list = []
        for paper_path in paper_path_list:
            qa_pair_path = os.path.join(paper_path, "qa_pairs.json")
            with open(qa_pair_path, "r") as f:
                qa_pairs = json.load(f)
            for qa_pair in qa_pairs[0]["qa_pairs"]:
                qa_pair["charts_involved"] = self.get_exbench_chart_list(paper_path, qa_pair["involved_content_sources"])
                parallel_pcpc_qa_pair_list.append(qa_pair)
            
            for qa_pair in qa_pairs[1]["qa_pairs"]:
                qa_pair["charts_involved"] = self.get_exbench_chart_list(paper_path, qa_pair["involved_content_sources"])
                parallel_pcmc_qa_pair_list.append(qa_pair)

            for qa_pair in qa_pairs[2]["qa_pairs"]:
                qa_pair["charts_involved"] = self.get_exbench_chart_list(paper_path, qa_pair["involved_content_sources"])
                union_pcpc_qa_pair_list.append(qa_pair)

            for qa_pair in qa_pairs[3]["qa_pairs"]:
                qa_pair["charts_involved"] = self.get_exbench_chart_list(paper_path, qa_pair["involved_content_sources"])
                union_pcmc_qa_pair_list.append(qa_pair)
        
        return parallel_pcpc_qa_pair_list, parallel_pcmc_qa_pair_list, union_pcpc_qa_pair_list, union_pcmc_qa_pair_list

class Evaluation:
    def get_task2_gen_code_prompt_cn(self):
        gen_code_prompt = '''
        以上是推理过程，由于大模型不擅长计算，所以忽略上面推理过程中的计算结果，将推理过程生成可执行的python代码。
        注意：
        1. 严格按照上面“rationale”的过程生成python代码。
        2. 确保代码正确反映“rationale”的推理，利用变量替代rationale中间步骤的计算结果，因为代码运行结果更加准确，避免使用中间计算步骤的计算结果导致累计误差。
        3. 最终的输出请严格按照要求的格式输出答案，只需要最后一个print的输出，不需要print任何描述性的语句。下面举几个最终的 print 例子供参考：
            a.  输出要求：“答案用整数表示即可。”
                错误的最终输出1：print(f"最终答案为：{answer}。")
                错误的最终输出2：print(f"**{answer}**")
                正确的最终输出：print(f"{answer}")
            b. 用百分数表示，保留4位有效数字。
                错误的最终输出1：print(f"移动端检索占比中，图文占比是 **{answer}%**。")
                正确的最终输出：print(f"{answer}%")
            c. 以美元为单位，保留3位小数。回答：xx美元
                错误的最终答案1：print(f"2023年第一季度，App Store在日本市场手游每次下载能带来{answer}美元的内购收入。")
                正确的最终输出：print(f"{answer}美元")
            d. 回答是或否。
                错误的最终输出1：print("True")
                正确的最终输出：print("是")
            e. 回答：xx 倍。
                错误的最终输出1：print(f"{answer}")
                正确的最终输出：print(f"{answer} 倍")
        4. 注意区分“有效数字”和“保留小数位数”。“有效数字”关注的是从第一个非零数字到末尾的所有数字。“保留小数位数”关注的是仅小数点后的数字个数。
        5. 如果涉及到浮点数计算，请使用 decimal 库，避免浮点数计算出现的精度丢失。
        '''
        return gen_code_prompt

    def get_task2_gen_code_prompt_en(self):
        gen_code_prompt = '''
        The above is the reasoning process. Since large models are not good at calculations, ignore the calculated results in the reasoning process above, and generate executable Python code for the reasoning process.
        Please note:
        1. Strictly generate Python code based on the "rationale" process above.
        2. Ensure the code correctly reflects the reasoning of the "rationale" by using variables to replace the intermediate calculation results in the rationale, as the code execution is more accurate and avoids cumulative errors caused by using intermediate calculation results.
        3. The final output should strictly follow the required format, only printing the last output from the final `print` statement, without any descriptive print statements. Below are some examples of the final print outputs for reference:
            a. Output format: “The answer should be presented as an integer.”
                Incorrect final output 1: print(f"The final answer is: {answer}.")
                Incorrect final output 2: print(f"**{answer}**")
                Correct final output: print(f"{answer}")
            b. Output in percentage, rounded to 4 significant digits.
                Incorrect final output 1: print(f"In mobile search, the proportion of images is **{answer}%**.")
                Correct final output: print(f"{answer}%")
            c. Output in dollars, rounded to 3 decimal places. Answer: xx dollars.
                Incorrect final output 1: print(f"In Q1 2023, the in-app purchase revenue per download for mobile games on the App Store in Japan is {answer} USD.")
                Correct final output: print(f"{answer} USD")
            d. Output "Yes" or "No".
                Incorrect final output 1: print("True")
                Correct final output: print("Yes")
            e. Answer: xx times.
                Incorrect final output 1: print(f"{answer}")
                Correct final output: print(f"{answer} times")
        4. Be sure to distinguish between "significant digits" and "decimal places." "Significant digits" refer to all digits from the first non-zero digit to the last digit. "Decimal places" refer to the number of digits after the decimal point.
        5. If floating-point calculations are involved, please use the `decimal` library to avoid precision loss from floating-point operations.
        '''
        return gen_code_prompt

    def get_task2_gen_code_prompt_es(self):
        gen_code_prompt = '''
        Lo anterior es el proceso de razonamiento. Dado que los modelos grandes no son buenos en cálculos, ignore los resultados calculados en el proceso de razonamiento anterior y genere un código Python ejecutable para el proceso de razonamiento.
        Tenga en cuenta lo siguiente:
        1. Genere el código Python estrictamente según el proceso de "razonamiento" anterior.
        2. Asegúrese de que el código refleje correctamente el razonamiento del "razonamiento" utilizando variables para reemplazar los resultados intermedios de cálculo en el razonamiento, ya que la ejecución del código es más precisa y evita errores acumulativos causados por el uso de resultados intermedios.
        3. La salida final debe seguir estrictamente el formato requerido, imprimiendo solo el último resultado de la declaración `print`, sin declaraciones descriptivas. A continuación, se presentan algunos ejemplos de salidas finales para referencia:
            a. Formato de salida: “La respuesta debe presentarse como un número entero.”
                Salida final incorrecta 1: print(f"La respuesta final es: {answer}.")
                Salida final incorrecta 2: print(f"**{answer}**")
                Salida final correcta: print(f"{answer}")
            b. Salida en porcentaje, redondeada a 4 cifras significativas.
                Salida final incorrecta 1: print(f"En la búsqueda móvil, la proporción de imágenes es **{answer}%**.")
                Salida final correcta: print(f"{answer}%")
            c. Salida en dólares, redondeada a 3 decimales. Respuesta: xx dólares.
                Salida final incorrecta 1: print(f"En el primer trimestre de 2023, los ingresos por compras dentro de la aplicación por descarga para juegos móviles en la App Store en Japón son {answer} USD.")
                Salida final correcta: print(f"{answer} USD")
            d. Responder "Sí" o "No".
                Salida final incorrecta 1: print("True")
                Salida final correcta: print("Sí")
            e. Respuesta: xx veces.
                Salida final incorrecta 1: print(f"{answer}")
                Salida final correcta: print(f"{answer} veces")
        4. Asegúrese de distinguir entre "cifras significativas" y "decimales." Las "cifras significativas" se refieren a todos los dígitos desde el primer dígito no cero hasta el último dígito. Los "decimales" se refieren a la cantidad de dígitos después del punto decimal.
        5. Si se realizan cálculos con números flotantes, utilice la biblioteca `decimal` para evitar la pérdida de precisión de las operaciones con números flotantes.
        '''
        return gen_code_prompt

    def get_task2_gen_code_prompt(self, language_type):

        if language_type == "cn":
            return self.get_task2_gen_code_prompt_cn()
        elif language_type == "en":
            return self.get_task2_gen_code_prompt_en()
        elif language_type == "es":
            return self.get_task2_gen_code_prompt_es()
        else:
            print("unkonwn language type!")

    def relaxed_accuracy(self, expected, actual):
        """
        Validate if the input values match the expected ones, supporting both string and numeric types.
        :param expected: The expected value
        :param actual: The actual value
        :return: A boolean indicating whether the validation passed
        """
        # Numeric validation (allows a 5% margin of error)
        try:
            # Try to convert the expected value to a number
            if isinstance(expected, str):
                # Remove spaces, full-width spaces, and percentage signs
                expected_str = expected.replace(' ', '').replace('　', '').strip('%')
                expected_num = float(expected_str)
            else:
                expected_num = float(expected)
            
            # Try to convert the actual value to a number
            if isinstance(actual, str):
                # Remove spaces, full-width spaces, and percentage signs
                actual_str = actual.replace(' ', '').replace('　', '').strip('%')
                actual_num = float(actual_str)
            else:
                actual_num = float(actual)
            
            # Calculate the allowed margin of error
            error_margin = expected_num * 0.05
            return abs(expected_num - actual_num) <= error_margin
        
        except (ValueError, TypeError):
            # String validation (ignores case, spaces, and full-width spaces)
            if isinstance(expected, str) and isinstance(actual, str):
                # Remove spaces and full-width spaces
                expected_clean = expected.replace(' ', '').replace('　', '').lower()
                actual_clean = actual.replace(' ', '').replace('　', '').lower()
                return expected_clean == actual_clean
            else:
                # If conversion to a number fails or types don't match, return False
                return False

    def extract_python_code(self, python_str):
        # Step 1: Extract the code block content (handling possible newlines and delimiters)
        match = re.search(r'```python\s*([\s\S]*?)\s*```', python_str)
        if match:
            python_str = match.group(1)
        else:
            # If no code block markers are found, try to use the remaining content
            print("No python code block found, using raw content")
        return python_str

    def gen_code(self, language_type, mllm_rationale):
        '''Generate executable Python code based on the MLLM inference process'''
        gen_code_prompt = self.get_task2_gen_code_prompt(language_type)

        text_prompt = "rationale: " + mllm_rationale + "\n\n" + gen_code_prompt
        # print(text_prompt)

        deepseek = myDeepSeekAPI()
        response = deepseek.call_deepseek_V3(text_prompt)
        python_code = self.extract_python_code(response)

        code_path = "./result.py"
        with open(code_path, "w", encoding='utf-8') as f:
            f.write(python_code)

        return code_path
    def excu_code(self, code_path):
        '''Get the execution result of the Python code'''

        # Use subprocess to run the Python script and capture the output
        result = subprocess.run(
            [sys.executable, code_path],
            capture_output=True,
            text=True,
            timeout=10  # Set a timeout of 10 seconds to prevent infinite running
        )
        
        return result.stdout.strip()

    def get_multi_choice_accuracy(self, predict_answer, label):
        """
        Calculate the accuracy for multiple choice questions
        :param predict_answer: The predicted answer list -> [choice1, choice2, ...]
        :param label: The correct answer list -> [choice1, choice2, ...]
        """

        # If the prediction list is empty, continue
        if not predict_answer:
            print("Empty predict answer, skipping...")
            return 0
        # print(f"Label: {label}\nPredict Answer: {predict_answer}")
        right_count = 0
        for choice in predict_answer:
            if choice in label:
                # Count the number of correct choices
                right_count += 1
            else:
                # If there is one incorrect choice, consider it as incorrect, score = 0
                right_count = 0
                break
        acc = right_count * 1.0 / len(label)

        return acc

    def evaluation_task1(self, gt, mllm_ans):
        return self.relaxed_accuracy(gt, mllm_ans)

    def evaluation_task2(self, language_type, gt, mllm_rationale):
        code_path = self.gen_code(language_type, mllm_rationale)
        mllm_ans = self.excu_code(code_path)
        return self.relaxed_accuracy(gt, mllm_ans)

    def evaluation_task3(self, gt, mllm_ans):
        return self.get_multi_choice_accuracy(mllm_ans, gt)

    def evaluation_task4(self, gt, mllm_ans):
        return self.get_multi_choice_accuracy(mllm_ans, gt)


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

    '''extended-benchmark qa list'''
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

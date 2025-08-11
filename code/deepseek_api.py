# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI

class myDeepSeekAPI():
    def __init__(self):
        self.api_key = "sk-xx"
    def call_deepseek_R1(self, prompt):
        client = OpenAI(api_key=self.api_key, base_url="https://api.deepseek.com")

        response = client.chat.completions.create(
            model="deepseek-reasoner",
            messages=[
                {"role": "system", "content": "You are a master of data analysis."},
                {"role": "user", "content": prompt},
            ],
            stream=False
        )

        return response.choices[0].message.content
    
    def call_deepseek_V3(self, prompt):
        client = OpenAI(api_key=self.api_key, base_url="https://api.deepseek.com")

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a master of data analysis."},
                {"role": "user", "content": prompt},
            ],
            stream=False
        )

        return response.choices[0].message.content

if __name__ == "__main__":
    prompt = "I want to know the meaning of life."
    deepseek = myDeepSeekAPI()
    # response = deepseek.call_deepseek_R1(prompt)
    # print(response)
    response = deepseek.call_deepseek_V3(prompt)
    print(response)
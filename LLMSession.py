# Copyright 2024 Google

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from prompts.JsonGenPrompts import JsonGenPrompts
from function_decl.extract_title_metadesc import json_extract_functions

import vertexai
from vertexai.preview.generative_models import GenerativeModel, Tool
from vertexai.language_models import TextGenerationModel


class LLMSession:
    def __init__(self, model_name: str):
        vertexai.init(project="poerschmann-sandbox-363314",
                      location="us-central1")

        self.model_name = model_name

    def llm_prediction(
        self,
        prompt_str: str, 
        max_output_tokens: int = 1024,
        temperature: float = 0.2,
        top_p: float = 0.8,
        top_k: int = 40,
    ) -> dict:

        parameters = {
            "max_output_tokens": max_output_tokens,
            "stop_sequences": ["} "],
            "temperature": temperature,
            "top_p": top_p,
            "top_k": top_k,
            "candidate_count": 1
        }

        if self.model_name == "gemini-pro":
            model = GenerativeModel("gemini-pro")
            responses = model.generate_content(
                prompt_str,
                generation_config=parameters,
                stream=False
            )

            response = {"text": responses.text}
        else:
            model = TextGenerationModel.from_pretrained(self.model_name)
            response = model.predict(prompt_str, **parameters)
            response = {"text": response.text}

        return response

    def llm_function_call(self, prompt_str):
        if self.model_name != "gemini-pro":
            raise ValueError("Input value cannot be negative.", self.model_name)
        else: 
            pass
        
        model = GenerativeModel(self.model_name)
        tools = Tool(function_declarations=[json_extract_functions().get_title_and_description])

        model_response = model.generate_content(
            prompt_str, generation_config={"temperature": 0}, tools=[tools]
        )

        try:
            return model_response.text
        except:
            return self._extract_arguments_from_model_response(model_response)

    def _extract_arguments_from_model_response(self, model_response) -> dict:
        """
        Extract the raw function name and function calling arguments from the model response.
        """
        res = model_response.candidates[0].content.parts[0].function_call.args

        func_arguments = {
            "function_name": model_response.candidates[0]
            .content.parts[0]
            .function_call.name,
            "function_arguments": {i: res[i] for i in res},
        }

        return func_arguments


if __name__ == "__main__":
    # prompt = "Which is the city with the most bridges?"

    prompt = constuct_prompt(product_name="dilli bazaaar Bellies, Corporate Casuals, Casuals",
                                                     product_description="Key Features of dilli bazaaar Bellies, Corporate Casuals, Casuals Material: Fabric Occasion: Ethnic, Casual, Party, Formal Color: Pink Heel Height: 0,Specifications of dilli bazaaar Bellies, Corporate Casuals, Casuals General Occasion Ethnic, Casual, Party, Formal Ideal For Women Shoe Details Weight 200 g (per single Shoe) - Weight of the product may vary depending on size. Heel Height 0 inch Outer Material Fabric Color Pink")

    llm_palm = LLMSession(model_name="text-unicorn@001")
    llm_gemini = LLMSession(model_name="gemini-pro")

    print("#### PaLM Test ####")
    response = llm_palm.llm_prediction(prompt_str=prompt)
    print(response)

    # print("#### Gemini Test ####")
    # response = llm_gemini.llm_prediction(prompt_str=prompt)
    # print(response)

    print("#### Gemini Function Calling Test ####")
    response = llm_gemini.llm_function_call(prompt_str=response['text'])
    print(response)

    print("Hello World!")

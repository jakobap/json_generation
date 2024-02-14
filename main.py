from LLMSession import LLMSession
from prompts.JsonGenPrompts import JsonGenPrompts
from function_decl.extract_title_metadesc import json_extract_functions

if __name__ == "__main__":
    product_name = "dilli bazaaar Bellies, Corporate Casuals, Casuals"
    product_description = "Key Features of dilli bazaaar Bellies, Corporate Casuals, Casuals Material: Fabric Occasion: Ethnic, Casual, Party, Formal Color: Pink Heel Height: 0,Specifications of dilli bazaaar Bellies, Corporate Casuals, Casuals General Occasion Ethnic, Casual, Party, Formal Ideal For Women Shoe Details Weight 200 g (per single Shoe) - Weight of the product may vary depending on size. Heel Height 0 inch Outer Material Fabric Color Pink"
    prompts = JsonGenPrompts(product_name=product_name, product_description=product_description)

    llm_palm = LLMSession(model_name="gemini-pro")
    llm_gemini = LLMSession(model_name="gemini-pro")

    print("#### Zero Shot simple ####")
    zero_shot_prompt = prompts.gen_and_extr_instruction + prompts.user_query
    response = llm_palm.llm_prediction(prompt_str=zero_shot_prompt, temperature=0.9)
    print(response['text'])
    

    print("####################")
    print("#### Zero Shot with function calling ####")
    text_response = llm_palm.llm_prediction(prompt_str=zero_shot_prompt, temperature=0.9)
    fc_response = llm_gemini.llm_function_call(prompt_str=response['text'])
    print(fc_response)

    print("####################")
    print("#### Multi shot simple ####")
    multi_shot_prompt = prompts.gen_and_extr_instruction + prompts.multi_shot_examples + prompts.user_query
    
    text_response = llm_palm.llm_prediction(prompt_str=multi_shot_prompt, temperature=0.9)
    print(response['text'])

    print("####################")
    print("#### Multi shot with function calling ####")
    text_response = llm_palm.llm_prediction(prompt_str=multi_shot_prompt, temperature=0.9)
    fc_response = llm_gemini.llm_function_call(prompt_str=text_response['text'])
    print(fc_response)

    print("Hello World!")
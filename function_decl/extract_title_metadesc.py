import inspect
from vertexai.preview import generative_models


class json_extract_functions:
    def __init__(self):
        pass

    @property
    def get_title_and_description(self):
        return generative_models.FunctionDeclaration(
            name="get_title_and_description",
            description="Extract the page title and meta description from.",
            parameters={
                "type": "object",
                "properties": {
                    "pageTitle": {
                        "type": "string",
                        "description": "The short title of the website to advertise"
                    },
                    "metaDescription": {
                        "type": "string",
                        "description": "The actionable meta description to use for page advertising"
                    }
                },
                "required": [
                    "pageTitle",
                    "metaDescription"
                ]
            },
        )

    def list_func_declararation(self, as_string: bool=False) -> list:
        func_decl_prefix = "func"
        func_decl_names = [attr for attr in dir(self) if inspect.isdatadescriptor(getattr(self.__class__, attr)) and attr.startswith(func_decl_prefix)]

        if as_string:
            func_decl_strings = [getattr(self, d)._raw_function_declaration for d in func_decl_names]
            return func_decl_strings
        else:
            func_decls = [getattr(self, d) for d in func_decl_names]
            return func_decls

    def list_required_parameters(self, property_name: str) -> list:
        return getattr(self, property_name)._raw_function_declaration.parameters.required


if __name__ == "__main__":

    func = json_extract_functions()
    print(func.get_title_and_description)

    declaration_strings= func.list_func_declararation(as_string=True)
    print(declaration_strings)

    declarations = func.list_func_declararation(as_string=False)
    print(declarations)

    required_params = func.list_required_parameters('get_title_and_description')
    print('get_title_and_description', required_params)
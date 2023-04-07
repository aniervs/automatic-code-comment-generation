import ast 
import torch 
from utils.tokenizer import python_tokenizer

def generate_python(code):
    model = torch.load('models/model_python.pt')
    tree = ast.parse(code)
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            code = ast.unparse(node)
            tokenized_code = python_tokenizer(code)
            comment = model(tokenized_code)[0]['summary_text']
            node.body.insert(0, ast.Expr(ast.Str(comment)))
        elif isinstance(node, ast.ClassDef):
            code = ast.unparse(node)
            tokenized_code = python_tokenizer(code)
            comment = model(tokenized_code)[0]['summary_text']
            node.body.insert(0, ast.Expr(ast.Str(comment)))
            for method in node.body:
                if isinstance(method, ast.FunctionDef):
                    code = ast.unparse(method)
                    tokenized_code = python_tokenizer(code)
                    comment = model(tokenized_code)[0]['summary_text']
                    method.body.insert(0, ast.Expr(ast.Str(comment)))
    return ast.unparse(tree)

def generate_sql(code):
    model = torch.load('models/model_sql.pt')
    comment = model(code)[0]['summary_text']    
    return '/*\n' + comment + '\n*/\n' + code 

def generate_comment(code, language):
    if language.lower() == 'python':
        return generate_python(code)
    if language.lower() == "sql":
        return generate_sql(code)
    return code 

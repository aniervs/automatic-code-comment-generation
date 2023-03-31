import tokenize
import io
import javalang

def python_tokenizer(line):
    result= []
    line = io.StringIO(line) 
    
    for toktype, tok, start, end, line in tokenize.generate_tokens(line.readline):
        if (not toktype == tokenize.COMMENT):
            if toktype == tokenize.STRING:
                result.append("CODE_STRING")
            elif toktype == tokenize.NUMBER:
                result.append("CODE_INTEGER")
            elif (not tok=="\n") and (not tok=="    "):
                result.append(str(tok))
    return ' '.join(result)


def java_tokenizer(code):
    token_list = []
    tokens = list(javalang.tokenizer.tokenize(code))
    for token in tokens:
        token_list.append(token.value)
    
    return ' '.join(token_list)

tokenizers = {
    'python' : python_tokenizer,
    'java': java_tokenizer
}
    
def general_tokenizer(code, language):
    token = tokenizers[language]
    return token(code)

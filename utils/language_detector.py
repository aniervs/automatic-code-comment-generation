import re

def detect_language(code):
    code = re.sub(r'#.*', '', code)
    code = re.sub(r'\s+', ' ', code).strip()
    
    patterns = {
        'Python': {
            'keywords': ['def', 'class', 'import', 'from', 'if', 'else', 'while'],
            'syntax': r'def\s|\sclass\s|\sif\s|\selse\s|\swhile\s'
        },
        'SQL': {
            'keywords': ['SELECT', 'FROM', 'WHERE', 'JOIN', 'ON', 'GROUP BY', 'HAVING', 'ORDER BY', 'LIMIT'],
            'syntax': r'^\s*(SELECT|INSERT|UPDATE|DELETE|CREATE|ALTER|DROP|GRANT|REVOKE)\b'
        }
    }
    
    
    for lang, pattern in patterns.items():
        if any(keyword in code for keyword in pattern['keywords']) or re.search(pattern['syntax'], code, re.IGNORECASE|re.MULTILINE):
            return lang
    
    return None

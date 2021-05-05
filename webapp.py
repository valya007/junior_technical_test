import nltk


def nouns_transform(sentence): 
    tokenized = nltk.word_tokenize(sentence)

    def is_noun (pos):
        return pos[:2] == 'NN'
    return [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]

def render_template(template_name='html pages/home.html', context={}):
    html_str = ""
    with open(template_name, 'r') as f:
        html_str = f.read()
        html_str = html_str.format(**context)
    return html_str
    
def main(environ, start_response):    
    query = environ.get("QUERY_STRING")
    path = environ.get("PATH_INFO")
    
    if len(query) > len("text="):
       sentence = query[5:].replace("+"," ").replace("%27","'")
       nouns = nouns_transform(sentence)
       data = render_template(template_name='html pages/nouns.html', context={"nouns_key": nouns}) 

    elif path == "/":
        data = render_template()
    else: 
        data = render_template(template_name='html pages/404.html')
 
    data = data.encode("utf-8")
    start_response(
        f"200 OK", [           
            ("Content-Type", "text/html"),
            ("Content-Length", str(len(data)))
        ]        
    )
    return iter([data])


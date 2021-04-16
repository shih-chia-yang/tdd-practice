class Element:
    def __init__(self,_tag,_text=None,_subnode=None):
        self.tag=_tag
        self.text=_text
        self.subnode=_subnode
    
    def __str__(self):
        content_text=self.text if self.text else ""
        subnode= self.subnode if self.subnode else ""
        value=f'<{self.tag}>{content_text}{subnode}</{self.tag}>'
        return value

class Html(Element):
    def __init__(self,_text=None,_subnode=None):
        super().__init__("html",_text,_subnode)
    
    def __str__(self):
        return super().__str__()

class Body(Element):
    def __init__(self,_text,_subnode=None):
        self.tag="body"
        super().__init__(self.tag,_text,_subnode)
    
    def __str__(self):
        return super().__str__()

class P(Element):
    def __init__(self,_text,_subnode=None):
        self.tag="p"
        super().__init__(self.tag,_text,_subnode)
    
    def __str__(self):
        return super().__str__()

def main():
    p=P("this is a p")
    body=Body("this is a body",p)
    html=Html(body)
    print(html)

if __name__=="__main__":
    main()
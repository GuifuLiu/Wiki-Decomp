class Template:
    def __init__(self, mode, item, context=""):
        self.mode = mode
        self.template = ""
        if self.mode == "zero-shot":
             self.template = f"Enumerate all possible parts of {item}:"
        elif self.mode == "zero-shot-qa":
             self.template = f"Q: What are all parts of {item}?\n\n A:"
        elif self.mode == "zero-shot-context":
             self.template = f"{item} is the {context}.\n Enumerate all possible parts of {item}:"
        else:
            pass

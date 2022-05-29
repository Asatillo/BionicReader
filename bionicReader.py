import webbrowser

class bionicRead:
    bold_tag = "<b>letters</b>"
    font_size = 40
    template_html = """<!DOCTYPE html>
    <html>
    <head>
        <meta charset='utf-8'>
        <meta http-equiv='X-UA-Compatible' content='IE=edge'>
        <title>Page Title</title>
        <meta name='viewport' content='width=device-width, initial-scale=1'>
        <link rel='stylesheet' type='text/css' media='screen' href='main.css'>
    </head>
    <body>
        <p>
            add_text
        </p>
    </body>
    </html>
    """
    template_css = """p{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    text-align: left;
    font-size: <font>px;
    margin-left: 30%;
    margin-right: 30%;
    padding-top: 10px;
    }
    """

    def __init__(self, filename):
        self.filename = filename
        self.create()

    def create(self):
        self.create_css()
        self.create_html()

    def create_html(self):
        read = open(self.filename, "r")
        file = open("BionicReader.html", "w")
        text = ""
        for line in read:
            words = line.split()
            for word in words:
                length = len(word)
                if("," in word or "." in word):
                    length -= 1
                cnt = round(length/2)
                text += self.bold_tag.replace("letters", word[0:cnt])
                text += word[cnt::]
                text += " "
        read.close()
        
        file.write(self.template_html.replace("add_text", text))
        file.close()

        webbrowser.open_new_tab("BionicReader.html")

    def create_css(self):
        file = open("main.css", "w")
        file.write(self.template_css.replace("<font>", str(self.font_size)))
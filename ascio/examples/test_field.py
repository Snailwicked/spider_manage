from ascio.aspider import AttrField,TextField,REField
from lxml import etree



def test_attr_field():
    html = ''''<body>
        <title>WODEDEEE</title>
        <div class="brand">
            <h1><a href="https://github.com">Github</a></h1>
        </div>
            <p>
                <a class="test_link" href="https://github.com/howie6879/ruia">hello github.</a>
                <a class="test_link" href="https://github.com/howie6879/ruia1">hello1 github.</a>
            </p>        <p>
                <a class="test_link" href="https://github.com/howie6879/ruia2">hello2 github.</a>
            </p>        <p>
                <a class="test_link" href="https://github.com/howie6879/ruia3">hello3 github.</a>
            </p>        <p>
                <a class="test_link" href="https://github.com/howie6879/ruia4">hello4 github.</a>
            </p>        <p>
                <a class="test_link" href="https://github.com/howie6879/ruia5">hello5 github.</a>
            </p>
    </body>'''
    field = REField(re_select='<title>(.*?)</title>')

    # html = etree.HTML(html)
    # field = TextField(css_select="h1>a")
    # href = field.extract_value(html=HTML)
    # value = field.extract_value(html)
    value = field.extract_value(html)


    # attr_field = AttrField(css_select="p a.test_link", attr='href')
    # # attr_field = AttrField(css_select="div.brand a", attr='href')
    # value = attr_field.extract_value(html)
    print(value)
test_attr_field()
from ehp import *

doc = '''<html>
<head>Heading</head>
<body attr1='val1'>
    <div class='container'>
        <div id='class'>Something here</div>
        <div>Something else</div>
    </div>
</body>
</html>
'''

html = Html()
dom = html.feed(doc)
for ind in dom.find('div', ('class', 'container')):
    print(ind.text())
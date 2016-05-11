<html>
<head>
  <title>Simple Models of Climate - {{title}}</title>
  <link rel="Stylesheet" type="text/css" href="/static/style.css" />
</head>
<body>

<h3>Menu</h3>
% from helper.menuhelper import render_menu
% from menu import menu_code
{{!render_menu(menu_code, url_params)}}

<h2>{{title}}</h2>
{{!base}}

</body>
</html>

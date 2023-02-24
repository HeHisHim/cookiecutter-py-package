# {{ cookiecutter.project_name }}

--- 

{{ cookiecutter.project_short_description}}


* windows: set FLASK_APP={{cookiecutter.project_slug}}.manager:app && flask run -p 10111 -h 0.0.0.0
* linux/macOS: export FLASK_APP={{cookiecutter.project_slug}}.manager:app && flask run -p 10111 -h 0.0.0.0
## Features

---

#### pip-compile
```
前置: pip install pip-tools
项目依赖在requirements.in文件中. 使用pip-compile -v -o requirements.txt来生成requirements.txt
请勿直接修改requirements.txt, pip-compile会根据依赖选择合适的版本写入requirements.txt
```

#### 运行
```
安装依赖: pip install -r requirements.txt
安装{{cookiecutter.project_slug}}命令行: pip install -e .
验证是否安装成功: {{cookiecutter.project_slug}} --help
```

* TODO

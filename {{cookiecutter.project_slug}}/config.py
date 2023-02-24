import yaml
import os
from urllib import parse
import re


class Config:
    def __init__(self):
        config_path = "{{cookiecutter.project_slug}}/conf/{{cookiecutter.project_slug}}.yaml"
        if not os.path.exists(config_path):
            raise ValueError("Could not find config file - <{}>".format(config_path))
        with open(config_path, "r", encoding="utf8") as obj:
            entries = yaml.safe_load(obj)
            if entries.get("SQLALCHEMY_DATABASE_URI"):
                entries["SQLALCHEMY_DATABASE_URI"] = self.quote_password(entries["SQLALCHEMY_DATABASE_URI"])
            self.__dict__.update(entries)

        for k, v in self.__dict__.items():
            print("{} = {}".format(k, v))
        print("Configuration initialization complete - <{}>\n".format(config_path))

    def quote_password(self, db_url):
        m = re.match(r"^(.*?)://(.*?):(.*)@(.*)$", db_url)
        driver, user, password, other = m.groups()
        return f"{driver}://{user}:{parse.quote_plus(password)}@{other}"

    def get(self, key, default=None):
        try:
            elements = key.split(".")
            data = self.__dict__
            for i in range(len(elements)):
                data = data[elements[i]]
            return data
        except KeyError:
            return default


config = Config()

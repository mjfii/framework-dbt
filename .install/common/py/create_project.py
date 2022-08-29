#!/usr/bin/env python3
import sys
import os
import yaml
from jinja2 import Template

_pwd = sys.argv[1]
_config_file = f"{_pwd}/.install/config/setup.yml"
_template_file = f"{_pwd}/.install/templates/dbt_project.yml"
_project_file = f"{_pwd}/dbt_project.yml"

with open(_template_file, "r") as _config:
    _template = Template(_config.read())

with open(_config_file, "r") as _config:
    try:
        _yaml = yaml.safe_load(_config)
        _profile = _yaml.get('config', {}).get('profile')
        _project = _yaml.get('config', {}).get('project')
        _adapter = _yaml.get('config', {}).get('adapter')
    except yaml.YAMLError as _excep:
        print(_excep)

if os.stat(_project_file).st_size == 0:
    with open(_project_file, "w") as _config:
        _config.write(_template.render(profile=f"{_profile}-{_adapter}", project=_project))

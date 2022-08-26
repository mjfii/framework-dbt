#!/usr/bin/env python3
import sys
import yaml
from jinja2 import Template

_pwd = sys.argv[1]
_active_profiles = sys.argv[2]
_config_file = f"{_pwd}/.install/config/setup.yml"
_template_file = f"{_pwd}/.install/templates/profiles.yml"

with open(_template_file, "r") as _config:
    _template = Template(_config.read())

with open(_config_file, "r") as _config:
    try:
        _yaml = yaml.safe_load(_config)
        _profile = _yaml.get('config', {}).get('profile')
        _database = _yaml.get('config', {}).get('database')
        _user = _yaml.get('config', {}).get('user')
        _target = _yaml.get('config', {}).get('target')
        _adapter = _yaml.get('config', {}).get('adapter')
        _composite_profile = f"{_profile}-{_adapter}"
    except yaml.YAMLError as _exception:
        print(_exception)

_render = _template.render(profile=_composite_profile, database=_database, user=_user, target=_target, adapter=_adapter)
print(_render)

_append = False
with open(_active_profiles, "r") as _config:
    try:
        _yaml = yaml.safe_load(_config)
        if _composite_profile not in _yaml:
            _append = True
    except yaml.YAMLError as _exception:
        print(_exception)

if _append:
    with open(_active_profiles, "a") as _config:
        _config.write("\n")
        _config.write(_render)
        _config.write("\n")

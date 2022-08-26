#!/usr/bin/env python3
import sys
import yaml

_pwd = sys.argv[1]
_pylibs_file = f"{_pwd}/.install/config/pylibs.yml"
_config_file = f"{_pwd}/.install/config/setup.yml"

with open(_pylibs_file, "r") as _file:
    try:
        _baselibs = yaml.safe_load(_file).get('base')
        print(f"# base libraries")
        for _baselib in _baselibs:
            print(_baselib)
    except yaml.YAMLError as _excep:
        print(_excep)

with open(_config_file, "r") as _config:
    try:
        _adapter = yaml.safe_load(_config).get('config').get('adapter')
    except yaml.YAMLError as _excep:
        print(_excep)

with open(_pylibs_file, "r") as _file:
    try:
        _dbtlibs = yaml.safe_load(_file).get(_adapter, "z")
        print(f"")
        print(f"# \"{_adapter}\" libraries")
        for _dbtlib in _dbtlibs:
            print(_dbtlib)
    except yaml.YAMLError as _excep:
        print(_excep)

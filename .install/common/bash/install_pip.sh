function install_pip() {
  cd "$1" || exit
  cd .venv || exit
  python3 -m pip install --upgrade pip --quiet
  pip3 install PyYAML --quiet
}

function install_libs() {
  cd "$1" || exit
  pip3 install -r requirements.txt --upgrade --quiet
}

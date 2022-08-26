function define_libs() {
  cd "$1" || exit
  python3 ./.install/common/py/define_libs.py "$1" > requirements.txt
}

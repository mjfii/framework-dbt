function build_venv() {
  cd "$1" || exit
  python3 -m venv ./.venv
  source .venv/bin/activate
}

function append_profile() {
  cd "$1" || exit
  mkdir -p ~/.dbt
  PROFILES_DIR="$HOME/.dbt/profiles.yml"
  touch "$PROFILES_DIR"
  python3 ./.install/common/py/append_profile.py "$1" "$PROFILES_DIR" >> ./.install/install.log
}

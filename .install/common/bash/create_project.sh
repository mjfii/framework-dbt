function create_project() {
  cd "$1" || exit
  python3 ./.install/common/py/create_project.py "$1" > dbt_project.yml
}

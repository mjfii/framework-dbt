function initialize() {
  tput civis
  task="${2-$1}"
  $1 & progress_spinner "$task" "[IN PROGRESS]"
  tput cnorm
}

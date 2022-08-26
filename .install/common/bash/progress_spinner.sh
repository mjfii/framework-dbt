function progress_spinner() {
  CL="\e[2K"
  SPINNER="⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
  task=$1
  msg=$2
  while :; do
    jobs %1 > /dev/null 2>&1
    [ $? = 0 ] || {
      printf "${CL}✓ ${task} [COMPLETE]\n"
      break
    }
    for (( i=0; i<${#SPINNER}; i++ )); do
      sleep 0.05
      printf "${CL}${SPINNER:$i:1} ${task} ${msg}\r"
    done
  done
}

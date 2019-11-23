#!/bin/bash

################################################################################
## Value
################################################################################
COMMANDNAME=`basename $0`
DIRECTORY=$(cd $(dirname $0);pwd)
logLevelCriteria=1


################################################################################
## Function
################################################################################
logger(){
    local lvl=$1
    local txt=$2
    case ${lvl} in
        0) local sta="DEBUG" ;;
        1) local sta="INFO" ;;
        2) local sta="ERROR" ;;
    esac
    [ ${lvl} -ge ${logLevelCriteria} ] && echo "[${sta}] ${txt}"
}

usage(){
    echo "USAGE: ${COMMANDNAME} [OPTION] <PLATFORM>"
    echo ""
    echo "OPTIONS"
    echo "  -h,--help       Show this help script"
    echo "  -u,--usage      Synonymous with -h or --help"
    echo "  -d,--debug      Show debug logs"    
    echo ""
    exit 0
}

abort(){
    local evt=$1
    case ${evt} in
        "ExceededCommand") local message="Input commands were exceeded !!" ;;
        "InvalidCommand")  local message="Invalid input command !!" ;;
        "InvalidOption")   local message="Invalid input option !!" ;;
        *)                 local message="Abort !!" ;;
    esac
    logger 2 "${message}"
    exit 1
}

################################################################################
## OPTION
################################################################################
FLG_S=0
FLG_B=0

GETOPT=`getopt -q -o husd --long help,usage,setup,debug -- "$@"` ; [ $? != 0 ] && abort InvalidOption

# echo $@ ##DEBUG

eval set -- "$GETOPT"

# echo $@ ## DEBUG

while true ;do
    case $1 in
        -h|--help|-u|--usage) usage ;;
        -s|--setup) FLG_S=1; shift  ;;
        -d|--debug) logLevelCriteria=0; FLG_B=1; shift;;
        --) shift ; break ;;
        *) abort InvalidOption ;;
    esac
done

logger 0 "\$@=$@"
logger 0 "\$#=$#"

if [ $# -gt 1 ];then
    abort ExceededCommand
else
    input=$@
    logger 0 "input=${input}"
    cd ${DIRECTORY}
    if [ ${FLG_S} -eq 1 ];then
        which pandoc
        if [ $? -eq 0 ];then
            [ -e README.md ] && pandoc --from markdown --to rst README.md -o README.rst
        else
            logger 2 "The \"pandoc\" comand is needed."
            abort
        fi
        if [[ ${input} = build ]]||[[ ${input} = install ]]||[[ ${input} = test ]]||[[ ${input} = clean ]]||[[ ${input} = check ]]||[[ ${input} = sdist ]];then
            if [ ${FLG_B} -ne 1 ];then
                python3 ./setup.py ${input}
                rm -rf README.rst
            else
                logger 0 "valid input for setup = ${input}"
            fi
        else
            abort InvalidCommand
        fi
    else
        if [ ${FLG_B} -ne 1 ];then
            python3 ./main.py "$@"
        else
            logger 0 "main.py is run"
        fi
    fi
fi

# EOF
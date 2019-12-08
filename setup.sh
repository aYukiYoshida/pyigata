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
    echo "USAGE: ${COMMANDNAME} [OPTION] <COMMAND>"
    echo ""
    echo "OPTIONS"
    echo "  -h,--help       Show this help script"
    echo "  -u,--usage      Synonymous with -h or --help"
    echo "  -d,--debug      Show debug logs"    
    echo ""
    echo "COMMANDS"
    echo "  build            build the target"
    echo "  install          install the target"
    echo "  test             run the unit-test"
    echo "  clean            clean the target"
    echo "  check            check the target"
    echo "  rename <NAME>    rename the target"
    exit 0
}

abort(){
    local evt=$1
    case ${evt} in
        "ExceededCommand") local message="Input commands were exceeded !!" ;;
        "LackingCommand")  local message="Input command was lacking !!" ;;
        "InvalidCommand")  local message="Invalid input command !!" ;;
        "InvalidOption")   local message="Invalid input option !!" ;;
        *)                 local message="Abort !!" ;;
    esac
    logger 2 "${message}"
    exit 1
}

rename(){
    local FLG_B=$1
    local name=$2

    if [ -z ${name} ];then
        abort LackingCommand
    else
        if [ ${FLG_B} -ne 1 ];then
            logger 1 "Rename target to ${name}"
            mv sample ${name}
            sed -i "/name=/s/sample/${name}/" .setup.py
            sed -i "s/import sample/import ${name}/g;s/sample\./${name}\./g" main.py
            sed -i "/pkg_dir/s/sample/${name}/g" ${name}/core.py
            for test_file in tests/*.py;do
                sed -i "s/import sample/import ${name}/g" ${test_file}
                sed -i "s/sample\./${name}\./g" ${test_file}
            done
        else
            logger 0 "new name = ${name}"
        fi
    fi
}

################################################################################
## OPTION
################################################################################
FLG_B=0

GETOPT=`getopt -q -o husd --long help,usage,setup,debug -- "$@"` ; [ $? != 0 ] && abort InvalidOption

# echo $@ ##DEBUG

eval set -- "$GETOPT"

# echo $@ ## DEBUG

while true ;do
    case $1 in
        -h|--help|-u|--usage) usage ;;
        -d|--debug) logLevelCriteria=0; FLG_B=1; shift;;
        --) shift ; break ;;
        *) abort InvalidOption ;;
    esac
done

logger 0 "\$@=$@"
logger 0 "\$#=$#"

input=$1
logger 0 "input=${input}"
cd ${DIRECTORY}
if [[ ${input} = build ]]||[[ ${input} = install ]]||[[ ${input} = test ]]||[[ ${input} = clean ]]||[[ ${input} = check ]]||[[ ${input} = sdist ]]||[[ ${input} = rename ]];then
    if [[ ${input} = rename ]];then
        name=$2
        logger 0 "name=${name}"
        logger 0 "length of name = ${#name}"
        rename ${FLG_B} ${name}
    else
        if [ $# -gt 1 ];then
            abort ExceededCommand
        else
            if [ ${FLG_B} -ne 1 ];then
                which pandoc 2>&1 > /dev/null
                if [ $? -eq 0 ];then
                    [ -e README.md ] && pandoc --from markdown --to rst README.md -o README.rst
                else
                    logger 2 "The \"pandoc\" comand is needed."
                    abort
                fi
                python3 ./.setup.py ${input}
                rm -rf README.rst
            else
                logger 0 "valid input for setup = ${input}"
            fi
        fi
    fi
else
    abort InvalidCommand
fi

# EOF
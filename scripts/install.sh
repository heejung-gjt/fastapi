# pip install -e ".[dev]"

# 실행 방식 :sh ./scripts/install.sh dev
if [[ $1 ]];
then
    pip install -e ".[$1]"
else
    pip install -e .
fi

mypy --install-types --non-interactive
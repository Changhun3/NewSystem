# -*- coding:utf-8 -*-

import sys
from behave import __main__ as Runner


if __name__ == '__main__':
    sys.stdout.flush()
    #RunnerOption = ''
    Runner.main('-k --no-capture --no-capture-stderr --tags=@aging -f plain')

    #Runner.main('-k --no-capture --no-capture-stderr --tags=@aging -f plain')
    # Runner.main('--no-capture --no-capture-stderr -f plain --tags=@E1.1_자원등록관리_스테이션등록')

# module => a file containing python code. May contain functions, classes, etc.
# used with modular programming, which is ri separate a program into parts

import for_test_modules as ftm # as yordamida alias beriladi

from for_test_modules import hello, bye # bu usul bilan moduldan faqat kerakli "narsa"larni import qilib olish mumkin
# from for_test_modules import *  # moduldagi barcha "narsa"ni import qilib olish
hello()
bye()

ftm.hello()
ftm.bye()

help("modules") # available
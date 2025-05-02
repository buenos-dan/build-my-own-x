#!/bin/zsh

# https://en.wikipedia.org/wiki/ANSI_escape_code

echo "==== Test prefixed ===="
echo -e "[1;31mHello, Red!\e[0m"
echo -e "\e[1;31mHello, Red!\e[0m"
echo -e "\033[1;31mHello, Red!\e[0m"           # 🌟 Recommended
echo -e "\u001b[1;31mHello, Red!\e[0m"
echo -e "\x1B[1;31mHello, Red!\e[0m"

echo "\n==== Test font style ===="
echo -e "\033[1;31mRed Bold\033[0m and \033[4;34mBlue Underline\033[0m"
echo -e "\033[1;3;31;5mBold Italic Red Blink\033[0m"

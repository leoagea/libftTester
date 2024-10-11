# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    tester.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lagea <lagea@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/10/10 15:55:47 by lagea             #+#    #+#              #
#    Updated: 2024/10/11 17:44:44 by lagea            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import subprocess
import sys

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"

BINDIR = "bin/"

def run_test(numtest, command, expected_output):
	command[0] = BINDIR + command[0]
	result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output = result.stdout.decode('utf-8').strip()  # get the output and remove whitespaces
	print(f"{numtest}.", end="")
	# print(f"return code : {result.returncode}")
	# print(f"output : {output}")
	if result.returncode == -11 and expected_output == "null":  # -11 => segfault
		print(f"{GREEN} OK {RESET}", end="")
	elif expected_output != "null" :
		if output == expected_output:
			print(f"{GREEN} OK {RESET}", end="")
		else:
			print(f"{RED} KO {RESET}", end="")

def test_ft_strlen():
	print("strlen : ", end="")
	run_test(1, ["./test_ft_strlen", ""], "0")
	run_test(2, ["./test_ft_strlen", "42"], "2")
	run_test(3, ["./test_ft_strlen", "hello"], "5")
	run_test(4, ["./test_ft_strlen", "test_ft_strlen"], "14")
	run_test(5, ["./test_ft_strlen", "null"], "null")
	print("")

def test_ft_isalpha():
	print("isalpha : ", end="")
	run_test(1, ["./test_ft_isalpha", "0"], "0") #nul
	run_test(2, ["./test_ft_isalpha", "42"], "0") #*
	run_test(3, ["./test_ft_isalpha", "65"], "1") #A
	run_test(4, ["./test_ft_isalpha", "90"], "1") #Z
	run_test(5, ["./test_ft_isalpha", "97"], "1") #a
	run_test(6, ["./test_ft_isalpha", "122"], "1") #z
	run_test(7, ["./test_ft_isalpha", "48"], "0") #0
	run_test(8, ["./test_ft_isalpha", "-1"], "0") #0
	print("")

def test_ft_isdigit():
	print("isdigit : ", end="")
	run_test(1, ["./test_ft_isdigit", "0"], "0") #nul
	run_test(2, ["./test_ft_isdigit", "42"], "0") #*
	run_test(3, ["./test_ft_isdigit", "48"], "1") #0
	run_test(4, ["./test_ft_isdigit", "53"], "1") #5
	run_test(5, ["./test_ft_isdigit", "57"], "1") #9
	run_test(6, ["./test_ft_isdigit", "82"], "0") #R
	run_test(7, ["./test_ft_isdigit", "126"], "0") #~
	run_test(8, ["./test_ft_isdigit", "-1"], "0") #0
	print("")

def test_ft_isalnum():
	print("isalnum : ", end="")
	run_test(1, ["./test_ft_isalnum", "0"], "0") #nul
	run_test(2, ["./test_ft_isalnum", "42"], "0") #*
	run_test(3, ["./test_ft_isalnum", "48"], "1") #0
	run_test(4, ["./test_ft_isalnum", "57"], "1") #5
	run_test(5, ["./test_ft_isalnum", "65"], "1") #A
	run_test(6, ["./test_ft_isalnum", "90"], "1") #Z
	run_test(7, ["./test_ft_isalnum", "97"], "1") #a
	run_test(8, ["./test_ft_isalnum", "122"], "1") #z
	run_test(9, ["./test_ft_isalnum", "126"], "0") #~
	run_test(10, ["./test_ft_isalnum", "-1"], "0") #0
	print("")

def test_ft_isascii():
	print("isascii : ", end="")
	run_test(1, ["./test_ft_isascii", "0"], "1") #nul
	run_test(2, ["./test_ft_isascii", "42"], "1") #*
	run_test(3, ["./test_ft_isascii", "48"], "1") #0
	run_test(4, ["./test_ft_isascii", "57"], "1") #5
	run_test(5, ["./test_ft_isascii", "65"], "1") #A
	run_test(6, ["./test_ft_isascii", "90"], "1") #Z
	run_test(7, ["./test_ft_isascii", "97"], "1") #a
	run_test(8, ["./test_ft_isascii", "122"], "1") #z
	run_test(9, ["./test_ft_isascii", "126"], "1") #~
	run_test(10, ["./test_ft_isascii", "-1"], "0") #0
	run_test(11, ["./test_ft_isascii", "-100"], "0") #0
	run_test(12, ["./test_ft_isascii", "256"], "0") #0
	run_test(13, ["./test_ft_isascii", "1024"], "0") #0
	print("")

def test_ft_isprint():
	print("isprint : ", end="")
	run_test(1, ["./test_ft_isprint", "0"], "0") #nul
	run_test(2, ["./test_ft_isprint", "10"], "0") #nl
	run_test(3, ["./test_ft_isprint", "27"], "0") #esc
	run_test(4, ["./test_ft_isprint", "32"], "1") #sapce
	run_test(5, ["./test_ft_isprint", "57"], "1") #5
	run_test(6, ["./test_ft_isprint", "65"], "1") #A
	run_test(7, ["./test_ft_isprint", "90"], "1") #Z
	run_test(8, ["./test_ft_isprint", "97"], "1") #a
	run_test(9, ["./test_ft_isprint", "122"], "1") #z
	run_test(10, ["./test_ft_isprint", "126"], "1") #~
	run_test(11, ["./test_ft_isprint", "-1"], "0") #0
	run_test(12, ["./test_ft_isprint", "-100"], "0") #0
	run_test(13, ["./test_ft_isprint", "256"], "0") #0
	run_test(14, ["./test_ft_isprint", "1024"], "0") #0
	print("")

def test_ft_memset():
	print("memset : ", end="")
	run_test(1, ["./test_ft_memset", "s", "0", "5"], "")
	run_test(2, ["./test_ft_memset", "s", "65", "5"], "AAAAA")
	run_test(3, ["./test_ft_memset", "s", "65", "-3"], "null") #segfault
	run_test(4, ["./test_ft_memset", "null", "65", "5"], "null") #segfault
	print("")

def test_ft_bzero():
	print("bzero : ", end="")
	run_test(1, ["./test_ft_bzero", "hello", "5"], "1")
	run_test(2, ["./test_ft_bzero", "hello", "3"], "1")
	run_test(3, ["./test_ft_bzero", "s", "-3"], "null") #segfault
	run_test(4, ["./test_ft_bzero", "null", "65", "5"], "null") #segfault
	print("")

def test_ft_toupper():
	print("toupper : ", end="")
	run_test(1, ["./test_ft_toupper", "0"], "0")
	run_test(2, ["./test_ft_toupper", "1"], "1")
	run_test(4, ["./test_ft_toupper", "42"], "42") 
	run_test(5, ["./test_ft_toupper", "97"], "65") #A
	run_test(6, ["./test_ft_toupper", "122"], "90") #Z
	run_test(7, ["./test_ft_toupper", "127"], "127")
	run_test(8, ["./test_ft_toupper", "255"], "255")
	run_test(9, ["./test_ft_toupper", "-1"], "-1")
	print("")

def test_ft_tolower():
	print("tolower : ", end="")
	run_test(1, ["./test_ft_tolower", "0"], "0")
	run_test(2, ["./test_ft_tolower", "1"], "1")
	run_test(4, ["./test_ft_tolower", "42"], "42") 
	run_test(5, ["./test_ft_tolower", "65"], "97") #A
	run_test(6, ["./test_ft_tolower", "90"], "122") #Z
	run_test(7, ["./test_ft_tolower", "127"], "127")
	run_test(8, ["./test_ft_tolower", "255"], "255")
	run_test(9, ["./test_ft_tolower", "-1"], "-1")
	print("")

def test_ft_strchr():
	print("strchr : ", end="")
	run_test(1, ["./test_ft_strchr", "Hello; World;", "59"], "; World;")
	run_test(2, ["./test_ft_strchr", ";Hello;World", "59"], ";Hello;World")
	run_test(4, ["./test_ft_strchr", "Hello World;", "59"], ";") 
	run_test(5, ["./test_ft_strchr", "Hello World", "59"], "(null)")
	run_test(6, ["./test_ft_strchr", "null", "59"], "null") #segfautl
	print("")

def test_ft_strrchr():
	print("strrchr : ", end="")
	run_test(1, ["./test_ft_strrchr", "Hello; World;", "59"], ";")
	run_test(2, ["./test_ft_strrchr", ";Hello;World", "59"], ";World")
	run_test(4, ["./test_ft_strrchr", ";Hello World", "59"], ";Hello World") 
	run_test(5, ["./test_ft_strrchr", "Hello World", "59"], "(null)")
	run_test(6, ["./test_ft_strrchr", "null", "59"], "null") #segfautl
	print("")

def test_ft_strncmp():
	print("strncmp : ", end="")
	run_test(1, ["./test_ft_strncmp", "hello", "hello", "-1"], "0")
	run_test(2, ["./test_ft_strncmp", "hello", "hello", "3"], "0")
	run_test(3, ["./test_ft_strncmp", "hello", "hello", "10"], "0")
	run_test(4, ["./test_ft_strncmp", "hello", "hello world", "12"], "-32")
	run_test(5, ["./test_ft_strncmp", "hello", "hello world", "10"], "-32")
	run_test(6, ["./test_ft_strncmp", "hello", "hello world", "-1"], "-32")
	run_test(7, ["./test_ft_strncmp", "hello world", "hello", "12"], "32")
	run_test(8, ["./test_ft_strncmp", "hello world", "hello", "10"], "32")
	run_test(9, ["./test_ft_strncmp", "hello world", "hello", "-1"], "32")
	run_test(10, ["./test_ft_strncmp", "hello world", "hello planet", "2147483647"], "7")
	run_test(11, ["./test_ft_strncmp", "hello planet", "hello world", "2147483647"], "-7")
	run_test(12, ["./test_ft_strncmp", "null", "hello world", "12"], "null")
	run_test(13, ["./test_ft_strncmp", "hello world", "null", "12"], "null")
	print("")

def test_all():
	test_ft_strlen()
	test_ft_isalpha()
	test_ft_isdigit()
	test_ft_isalnum()
	test_ft_isascii()
	test_ft_isprint()
	test_ft_memset()
	test_ft_bzero()
	test_ft_toupper()
	test_ft_tolower()
	test_ft_strchr()
	test_ft_strrchr()
	test_ft_strncmp()
	
if __name__ == "__main__":
	if len(sys.argv) > 1:
		if sys.argv[1] == "strlen":
			test_ft_strlen()
		elif sys.argv[1] == "isalpha":
			test_ft_isalpha()
		elif sys.argv[1] == "memset":
			test_ft_memset();
		elif sys.argv[1] == "all":
			test_all()
		else:
			print(f"{RED}Error : Unknown test.{RESET}")
	else:
		print(f"{YELLOW}Usage : python3 tester.py <name_of_test>{RESET}")
		print(f"Exemple : python3 tester.py strlen ou python3 tester.py all")


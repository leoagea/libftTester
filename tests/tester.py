# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    tester.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lagea <lagea@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/10/10 15:55:47 by lagea             #+#    #+#              #
#    Updated: 2024/10/10 18:34:06 by lagea            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import subprocess
import sys

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"

def run_test(numtest, command, expected_output):
	result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output = result.stdout.decode('utf-8').strip()  # get the output and remove whitespaces
	print(f"{numtest}.", end="")
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
	print("")

def test_all():
	test_ft_strlen()
	test_ft_isalpha()

if __name__ == "__main__":
	if len(sys.argv) > 1:
		if sys.argv[1] == "strlen":
			test_ft_strlen()
		elif sys.argv[1] == "isalpha":
			test_ft_isalpha()
		elif sys.argv[1] == "all":
			test_all()
		else:
			print(f"{RED}Error : Unknown test.{RESET}")
	else:
		print(f"{YELLOW}Usage : python3 tester.py <name_of_test>{RESET}")
		print(f"Exemple : python3 tester.py strlen ou python3 tester.py all")


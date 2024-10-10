# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lagea <lagea@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/10/10 17:46:27 by lagea             #+#    #+#              #
#    Updated: 2024/10/10 18:09:01 by lagea            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

CC = gcc
CFLAGS = -Wall -Wextra -Werror
SRCS = $(wildcard *.c)
EXECS = $(SRCS:.c=)

all: $(EXECS) run_all_tests

strlen: test_ft_strlen
	python3 tester.py strlen

isalpha: test_ft_isalpha
	python3 tester.py isalpha
	
%: %.c
	$(CC) $(CFLAGS) -o $@ $< ../libft/libft.a  # On suppose que libft.a est déjà compilée

run_all_tests: $(EXECS)
	python3 tester.py all

clean:
	rm -f $(EXECS)

fclean: clean
	rm -f *.o

re: fclean all

.PHONY : all re clean fclean
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lagea <lagea@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/10/10 17:46:27 by lagea             #+#    #+#              #
#    Updated: 2024/10/11 17:45:53 by lagea            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

CC = gcc
CFLAGS = -Wall -Wextra -Werror
SRCS = $(wildcard *.c)
EXECS = $(SRCS:.c=)

BINDIR = bin

all: $(BINDIR) $(addprefix $(BINDIR)/, $(EXECS)) run_all_tests

$(BINDIR):
	mkdir -p $(BINDIR)
	
strlen: $(BINDIR)/test_ft_strlen
	make -C ../libft
	python3 tester.py strlen

isalpha: $(BINDIR)/test_ft_isalpha
	make -C ../libft
	python3 tester.py isalpha

isdigit: $(BINDIR)/test_ft_isdigit
	make -C ../libft
	python3 tester.py isdigit

memset: $(BINDIR)/test_ft_memset
	make -C ../libft
	python3 tester.py memset

$(BINDIR)/%: %.c
	$(CC) $(CFLAGS) -o $@ $< ../libft/libft.a

run_all_tests: $(addprefix $(BINDIR)/, $(EXECS))
	make -C ../libft
	python3 tester.py all

clean:
	rm -f $(addprefix $(BINDIR)/, $(EXECS))

fclean: clean
	rm -f bin/*.o
	rm -rf bin

re: fclean all

.PHONY : all re clean fclean
/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test_ft_memset.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lagea <lagea@student.42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/10/11 14:27:06 by lagea             #+#    #+#             */
/*   Updated: 2024/10/11 16:10:35 by lagea            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../libft/libft.h"
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int ac, char **av){
	if (ac != 4)
		printf("Usage : ./test_ft_memset <string> <int> <size_t>\n");
	
	char *s;
	if (strcmp(av[1], "null") == 0)
		s = NULL;
	else
		s = malloc(sizeof(char) * (atoi(av[2]) + 1));
	
	// ft_memset(s, atoi(av[2]), (size_t)atoi(av[3]));
	memset(s, atoi(av[2]), (size_t)atoi(av[3]));
	s[atoi(av[2])] = '\0';
	printf("%s", s);
	return 0;
}
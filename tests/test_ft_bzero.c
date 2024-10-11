/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test_ft_bzero.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lagea <lagea@student.42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/10/11 14:27:06 by lagea             #+#    #+#             */
/*   Updated: 2024/10/11 16:52:48 by lagea            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../libft/libft.h"
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

int main(int ac, char **av){
	if (ac != 3)
		printf("Usage : ./test_ft_memset <string> <size_t>\n");
	
	char *s;
	if (strcmp(av[1], "null") == 0)
		s = NULL;
	else
		s = av[1];
	
	ft_bzero(s, atoi(av[2]));
	// bzero(s, atoi(av[2]));
	bool check;
	check = true;
	for (int i=0; i < atoi(av[2]); i++)
		if (s[i] != 0)
			check = false;
	printf("%d", check);
	return 0;
}
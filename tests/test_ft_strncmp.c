/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test_ft_strncmp.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lagea <lagea@student.42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/10/10 17:57:41 by lagea             #+#    #+#             */
/*   Updated: 2024/10/11 17:44:18 by lagea            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../libft/libft.h"
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int ac, char **av){
	if (ac != 4)
		printf("Usage : ./test_ft_strchr <string> <int<\n");
	if (strcmp(av[1], "null") == 0)
		av[1] = NULL;
	if (strcmp(av[2], "null") == 0)
		av[2] = NULL;
	// printf("%d",strncmp(av[1], av[2], atoi(av[3])));
	printf("%d",ft_strncmp(av[1], av[2], atoi(av[3])));
	return 0;
}
/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test_ft_strrchr.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lagea <lagea@student.42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/10/10 17:57:41 by lagea             #+#    #+#             */
/*   Updated: 2024/10/11 17:24:46 by lagea            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../libft/libft.h"
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int ac, char **av){
	if (ac != 3)
		printf("Usage : ./test_ft_strchr <string> <int<\n");
	if (strcmp(av[1], "null") == 0)
		av[1] = NULL;
	// printf("%s",strrchr(av[1], atoi(av[2])));
	printf("%s",ft_strrchr(av[1], atoi(av[2])));
	return 0;
}
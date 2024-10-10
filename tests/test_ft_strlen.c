/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test_ft_strlen.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lagea <lagea@student.42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/10/10 15:29:34 by lagea             #+#    #+#             */
/*   Updated: 2024/10/10 18:32:01 by lagea            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../libft/libft.h"
#include <stdio.h>
#include <string.h>

int main(int ac, char **av){
	if (ac != 2)
		printf("Usage : ./test_ft_strlen <string>\n");
	
	char *s = NULL;
	if (strcmp(av[1], "null") == 0)
		s = NULL;
	else
		s = av[1];
	// printf("%zu",strlen(s));
	printf("%zu",ft_strlen(s));
	return 0;
}
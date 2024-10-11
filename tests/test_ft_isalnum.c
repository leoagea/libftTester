/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test_ft_isalnum.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lagea <lagea@student.42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/10/10 17:57:41 by lagea             #+#    #+#             */
/*   Updated: 2024/10/11 14:32:43 by lagea            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../libft/libft.h"
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int ac, char **av){
	if (ac != 2)
		printf("Usage : ./test_ft_isalnum <int>\n");
	// printf("%d",isalnum(atoi(av[1])));
	printf("%d",ft_isalnum(atoi(av[1])));
	return 0;
}
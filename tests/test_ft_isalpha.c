/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test_ft_isalpha.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lagea <lagea@student.42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/10/10 17:57:41 by lagea             #+#    #+#             */
/*   Updated: 2024/10/10 18:36:10 by lagea            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../libft/libft.h"
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int ac, char **av){
	if (ac != 2)
		printf("Usage : ./test_ft_isalpha <int1>\n");
	// printf("%d",isalpha(atoi(av[1])));
	printf("%d",ft_isalpha(atoi(av[1])));
	return 0;
}
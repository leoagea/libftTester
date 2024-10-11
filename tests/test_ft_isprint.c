/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test_ft_isprint.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lagea <lagea@student.42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/10/11 14:27:06 by lagea             #+#    #+#             */
/*   Updated: 2024/10/11 14:42:49 by lagea            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../libft/libft.h"
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int ac, char **av){
	if (ac != 2)
		printf("Usage : ./test_ft_isprint <int>\n");
	// printf("%d",isprint(atoi(av[1])));
	printf("%d",ft_isprint(atoi(av[1])));
	return 0;
}
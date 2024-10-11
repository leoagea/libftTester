/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test_ft_toupper.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lagea <lagea@student.42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/10/10 17:57:41 by lagea             #+#    #+#             */
/*   Updated: 2024/10/11 17:05:24 by lagea            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../libft/libft.h"
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int ac, char **av){
	if (ac != 2)
		printf("Usage : ./test_ft_toupper <int>\n");
	// printf("%d",toupper(atoi(av[1])));
	printf("%d",ft_toupper(atoi(av[1])));
	return 0;
}
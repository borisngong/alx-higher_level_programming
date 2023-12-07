#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

/**
 * struct dlistint_s - Doubly linked list node structure
 * @n: Integer stored in the node
 * @prev: represents a pointer to the previous element of the list
 * @next: represents a pointer to the next element of the list
 *
 * Description: Doubly linked list node structure for dlistint_t
 */
typedef struct dlistint_s
{
	int n;
	struct dlistint_s *next;
	struct dlistint_s *prev;
} dlistint_t;
size_t print_dlistint(const dlistint_t *h);

#endif /* LISTS_H */

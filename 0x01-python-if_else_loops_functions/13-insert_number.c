#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * insert_node - responsible to insert a num into a sorted singly-linked list.
 * @head: represents a pointer the head of the linked list.
 * @number: represents the number to insert.
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}
	while (node && node->next && node->next->n < number)
	node = node->next;
	new->next = node->next;
	node->next = new;

	return (new);
}

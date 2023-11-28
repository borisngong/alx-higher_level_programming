#include "lists.h"
/**
 * check_cycle - responsible for Checking if a linked list contains a cycle.
 * @list: represents the Linked list to check.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list->next;

	if (list == NULL || list->next == NULL)
		return (0);
	while (fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
			return (1);

		slow = slow->next;
		fast = fast->next->next;
	}

	return (0);
}

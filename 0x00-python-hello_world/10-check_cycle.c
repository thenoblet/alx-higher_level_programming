#include "lists.h"

/**
 * check_cycle - Checks if a linked list has a cycle using Floyd's algorithm.
 * @list: Pointer to the head of the linked list.
 *
 * Description:
 * This function implements Floyd's cycle-finding algorithm also known as
 * the "tortoise and the hare" algorithm, to determine whether a given
 * linked list contains a cycle. It uses two pointers, one moving at
 * twice the speed of the other. If there's a cycle, the faster
 * pointer will eventually catch up to the slower one.
 *
 * Return: 1 if a cycle is detected, 0 otherwise.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	/* Check if the list is empty or has only one node */
	if (list == NULL || list->next == NULL)
		return (0);

	 /* Initialize pointers */
	slow = list;
	fast = list->next;

	/* Traverse the list using Floyd's cycle-finding algorithm */
	while (fast != NULL && fast->next != NULL && slow != NULL)
	{
		/* Check if fast has caught up to slow, indicating a cycle */
		if (fast == slow)
			return (1);

		/* Move pointers: slow advances one step, fast advances two steps */
		fast = fast->next->next;
		slow = slow->next;
	}

	return (0); /* No cycle detected */
}


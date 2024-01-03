#include "lists.h"

/**
 * insert_node - Inserts a new node with a specified number into
 * a sorted linked list.
 * @head: Pointer to the head of the linked list.
 * @number: The number to be inserted into the linked list.
 *
 * Description:
 * This function adds a new node to a linked list while ensuring
 * the list remains sorted.
 * It takes a pointer to the head of the list and the number for
 * the new node.
 * The function handles cases such as an empty list,insertion
 * at the beginning, and finding the correct position for insertion
 * to maintain sorted order.
 *
 * Return: Pointer to the newly inserted node or NULL on failure.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new_node;

	/* Allocate memory for the new node */
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	/* Initialize the new node with the given number */
	new_node->n = number;
	current = *head; /* Set 'current' to the head of the list */

	/* is the list empty? insert! */
	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}

	if (new_node->n < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	/* Traverse the list to find the correct position for insertion. */
	while (current->next != NULL && new_node->n > current->next->n)
		current = current->next;

	/* Insert the new node in the middle or at the end of the list. */
	new_node->next = current->next;
	current->next = new_node;

	return (new_node); /* Return the newly inserted node. */
}


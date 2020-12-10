#include "lists.h"

/**
 * *insert_node - inserts a new node in a sorted linked list
 * @number: integer in struct
 * @head: pointer to head
 * Return: the address of the new node or NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *act = *head;
	listint_t *sig = NULL;
	listint_t *new;

	if (*head == NULL || number <= act->n)
	{
		new = malloc(sizeof(listint_t));
		if (new == NULL)
			return (NULL);
		new->n = number;
		*head = new;
		new->next = act;
		return (new);
	}
	while (act != NULL)
	{
		sig = act->next;
		if (act->next != NULL)
		{
			if (number >= act->n && number <= sig->n)
			{
				new = malloc(sizeof(listint_t));
				if (new == NULL)
					return (NULL);
				new->n = number;
				new->next = act->next;
				act->next = new;
				return (new);
			}
			act = act->next;
			continue;
		}
		else
		{
			new = malloc(sizeof(listint_t));
			if (new == NULL)
				return (NULL);
			new->n = number;
			new->next = act->next;
			act->next = new;
			return (new);
		}
	}
	return (NULL);
}

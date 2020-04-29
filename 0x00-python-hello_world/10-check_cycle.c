#include "lists.h"
/**
*check_cycle - check if there is a cycle
* @list: list
* Return: return 1 or 0
*/
int check_cycle(listint_t *list)
{
listint_t *one, *two;
if (list == NULL || list->next == NULL )
return (0);
one = list;
two = one->next;
while ((two != NULL) & (two->next != NULL) & (one != NULL))
{
one = one->next;
two = two->next->next;
if (one == two)
return (1);
}
return (0);
}

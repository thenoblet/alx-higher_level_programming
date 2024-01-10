#include <stdio.h>
#include <Python.h>
#include <string.h>
#include <object.h>
#include <listobject.h>

/**
 * Description: Prints information about a Python list, including its size,
 * allocated space, and information about each element.
 *
 * @p: Pointer to a PyObject representing a Python list
 */
void print_python_list_info(PyObject *p)
{
	int i;

	printf("[*] Size of the Python List = %d\n", (int)PyList_Size(p));
	printf("[*] Allocated = %d\n", (int)(((PyListObject *)p)->allocated));

	for (i = 0; i < (int)PyList_Size(p); i++)
	{
		printf("Element %d: %s\n", i, PyList_GetItem(p, i)->ob_type->tp_name);
	}

}

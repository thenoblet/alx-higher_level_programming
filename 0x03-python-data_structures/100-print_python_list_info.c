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
	PyListObject *obj = (PyListObject *)p;
	ssize_t i, size = PyList_Size(p);

	/* Print the size of the Python list */
	printf("[*] Size of the Python List = %ld\n", size);

	/* Print the allocated space for the list */
	printf("[*] Allocated = %ld\n", obj->allocated);

	/* Iterate through the elements of the list */
	for (i = 0; i < size; i++)
	{
		/* Print the type name of each element */
		printf("Element %ld: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
	}
}

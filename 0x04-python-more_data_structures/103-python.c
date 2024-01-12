# include <Python.h>
# include <stdio.h>
# include <stdlib.h>

/**
 * print_python_list - function that prints basic info
 * on python list
 * @p: arbitrary Python object
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t size, alloc, i;
	PyObject *item;

	printf("[*] Python list info\n");
	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}

/**
 * print_python_bytes - function that prints basic info
 * on python byte objects
 * @p: arbitrary Python object
 */

void print_python_bytes(PyObject *p)
{
	char *str;
	Py_ssize_t size, i;
	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);
	printf("  first %ld bytes: ", size < 10 ? size + 1 : 10);

	for (i = 0; i < size + 1 && i < 10; i++)
		printf("%02hhx%s", str[i], i < 9 && i < size ? " " : "\n");
}

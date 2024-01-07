# include <Python.h>

/**
 * print_python_list_info - Prints some basic info about Python lists
 * @p: PyObject
 */

void print_python_list_info(PyObject *p)
{
	if (PyList_Check(p))
	{
		printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
		printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
		for (int i = 0; i < PyList_Size(p); i++)
			printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
	else
		printf("PyObject isn't a Python List\n");
}

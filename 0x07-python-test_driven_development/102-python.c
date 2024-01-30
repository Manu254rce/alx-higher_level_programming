# define PY_SIZE_T_CLEAN /* for Python 3.10 and later */
# include <stdio.h>
# include <Python.h>

/**
 * print_python_string - functin that prints out Python string
 * objects
 * @p: pointer variable to the Python object
 */

void print_python_string(PyObject *p)
{
	Py_ssize_t size;
	const char *string;

	if (!PyUnicode_Check(p))
	{
		printf(" [ERROR] Invalid String Object\n");
		return;
	}

	string = PyUnicode_AsUTF8AndSize(p, &size);

	if (string == NULL)
	{
		printf(" [ERROR] Invalid UTF-8 String \n");
		return;
	}
	
	printf("[.] string object info\n");
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf(" type: compact ascii\n");
	else
		printf(" type: compact unicode object\n");
	printf(" length: %ld\n", PyUnicode_GET_LENGTH(p));
	printf(" value: %s\n", string);

}

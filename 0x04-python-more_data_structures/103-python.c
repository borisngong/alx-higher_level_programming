#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_bytes(PyObject *p)
{
	long int size;
    int i;
    char *data = NULL;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    PyBytes_AsStringAndSize(p, &data, &size);

    printf("  size: %li\n", size);
    printf("  trying string: %s\n", data);

    if (size < 10)
        printf("  first %li bytes:", size + 1);
    else
        printf("  first 10 bytes:");

    for (i = 0; i <= size && i < 10; i++)
        printf(" %02hhx", data[i]);

    printf("\n");
}

void print_python_list(PyObject *p)
{
    long int size = PyList_Size(p);
    int i;
    PyListObject *list_obj = (PyListObject *)p;
    const char *obj_type;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %li\n", size);
    printf("[*] Allocated = %li\n", list_obj->allocated);

    for (i = 0; i < size; i++)
    {
        obj_type = (list_obj->ob_item[i])->ob_type->tp_name;
        printf("Element %i: %s\n", i, obj_type);

        if (!strcmp(obj_type, "bytes"))
            print_python_bytes(list_obj->ob_item[i]);
    }
}
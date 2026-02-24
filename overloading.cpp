#include <iostream>
using namespace std;

class sampleclass
{
    public: void add (int a,int b)
    {
        cout<< "\n add is:" << a+b << endl;
    }
    public: void add (int a,int b, int c)
     {
        cout<< "\n add is:" << a+b+c << endl;
    }
     public: void add (float a,float b)
     {
        cout<< "\n add is:" << a+b << endl;
    }
};

int main()
    sampleclass obj;
    obj.add (10,20);
    obj.add (100,200);
    obj.add (1.1f,2.30f);
    return 0;
    
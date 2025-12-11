#include <iostream>
#include <limits>
using namespace std;

int main() {
    cout << "=== Razmery tipov dannyh ===" << endl;
    cout << "int: " << sizeof(int) << " bajt(a)" << endl;
    cout << "long long: " << sizeof(long long) << " bajt(a)" << endl;
    
    cout << "\n=== Diapazony tipov ===" << endl;
    cout << "int min: " << numeric_limits<int>::min() << endl;
    cout << "int max: " << numeric_limits<int>::max() << endl;
    cout << "long long min: " << numeric_limits<long long>::min() << endl;
    cout << "long long max: " << numeric_limits<long long>::max() << endl;
    
    cout << "\n=== Primer perepolneniya int ===" << endl;
    int x = 1000000000;
    int y = 1000000000;
    cout << "int x = 1000000000" << endl;
    cout << "int y = 1000000000" << endl;
    cout << "x + y = " << (x + y) << " (perepolnenie!)" << endl;
    
    cout << "\n=== Pravilnoe reshenie s long long ===" << endl;
    long long a = 1000000000;
    long long b = 1000000000;
    cout << "long long a = 1000000000" << endl;
    cout << "long long b = 1000000000" << endl;
    cout << "a + b = " << (a + b) << " (pravilno!)" << endl;
    
    cout << "\n=== Test chteniya vvoda ===" << endl;
    cout << "Vvedite dva chisla: ";
    long long num1, num2;
    cin >> num1 >> num2;
    cout << "Vy vveli: " << num1 << " i " << num2 << endl;
    cout << "Ih summa: " << (num1 + num2) << endl;
    
    return 0;
}

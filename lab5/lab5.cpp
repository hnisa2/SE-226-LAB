#include <iostream>
using namespace std;

double geometricSeries(int n, double r) {
    if (n==0) {
        return 1;
    }
    return (r*geometricSeries(n-1, r))+1 ;
}

int main() {
    int n;
    double r;
    cout<< "Enter n: ";
    cin>> n;
    cout << "Enter r: ";
    cin >> r;
    cout<< "Geometric series result= "<<geometricSeries(n, r)<<endl;
    return 0;
}
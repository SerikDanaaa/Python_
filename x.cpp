#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    double x, y, z;
    cout <<setw(10)<<"x"<<setw(10)<<"y"<<setw(10)<< "z" << endl;
    x = -1.0;
    y = 5.0;
    while(x <= 0.5){
        while(y <= 15){
            if(x*y < 1){
                z = x+y;
            }
            else{
                x = x-y;
            }
            cout <<setw(10)<< x <<setw(10)<< y <<setw(10) << z << endl;
            y++;          
        }
        x += 0.5;
    }
    return 0;
}
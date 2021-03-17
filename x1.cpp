#include <iostream>
#include <iomanip>
using namespace std;
int main(){
        double x, y, z;
        cout<<setw(10)<<"x"<<setw(10)<<"y"<<setw(10)<<"z"<<endl;
        for(x=-1; x<=0.5; x=x+0.5){
               for(y=5; y<=15; y=y+1){
                       if(x*y<1){
                               z=x+y; }
                       else{
                               z=x-y;
                       }
                       cout<<setw(10)<<x<<setw(10)<<y<<setw(10)<<z<<endl;
        }
        return 0;
        }
}
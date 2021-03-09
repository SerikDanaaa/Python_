#include <iostream>
using namespace std;

int main(){
    int a,b,c;
    cin>>a>>b>>c;
    if(!(((a ^ b) && (a || c))) != 0){
        cout<<"naqty x1,x2,dx sandaryn enqiziniz: "<<endl;
        float x1,x2,dx;
        cin >> x1 >> x2 >> dx;
            for(int x = x1; x <= x2; x += dx){
                if(x == 0 and b != 0){
                   cout << a*(x+c)*(x+c) - b << endl;
                }
                else if(x == 0 and b == 0){
                    cout<< (x-a) / (-c) << endl;
                }
                else{
                    cout << a + (x/c) << endl;
                }
            }
        }
    else{
        cout<<"butin x1,x2,dx sandaryn enqiziniz: "<<endl;
        int x1,x2,dx;
        cin >> x1 >> x2 >> dx;
        for(int x = x1; x <= x2; x += dx){
            if(x == 0 and b != 0){
                cout << a*(x+c)*(x+c) - b << endl;
            }
            else if(x == 0 and b == 0){
                cout<< (x-a) / (-c) << endl;
            }
            else{
                cout << a + (x/c) << endl;
            }
        }
    }
}
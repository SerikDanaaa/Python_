#include <iostream>
using namespace std;

int main(){
    int n,m;
    cin>>n>>m;
    int** a = new int* [n];

    for(int i = 0; i < n ; i++){
        a[i] = new int[m];
    }
    for(int i = 0; i < n ; i++){
        for(int j = 0; j < m; j++){
            cin>>a[i][j];
        }
    }
    bool ok = true;
    int cnt = 0; 
    for(int i = 0; i < n ; i++){
        ok = true;
        for(int j = 1; j < m; j++){
            if(a[i][0] != a[i][j]){
                ok = false;
            }
        }
        if(ok){
            cnt++;
        }
    }
    cout << cnt;   
}
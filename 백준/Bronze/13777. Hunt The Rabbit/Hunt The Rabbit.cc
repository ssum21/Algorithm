#include <iostream>

using namespace std;

void binary_search(int left, int right, int mid, int x){
    cout << mid << " ";
    if(mid==x){
        {};
    }
    else if(mid > x){
        binary_search(left, mid-1, (left+mid-1)/2, x);}
    else{
        binary_search(mid+1, right, (mid+right+1)/2, x);
    }
}


int main(){
    int n;
    while(true){
        cin >> n;
        if(n==0){
            break;
        }
        binary_search(1, 50, 25, n);
    }
    return 0;
    
}
#include<bits/stdc++.h>
#include<iostream>
using namespace std;
int main()
{
    int n;
    cout << "Enter number of elements : ";
    cin >> n;
    vector<int> v(n);
    int avg =0,k;
    for(int i=0 ; i<n ; i++)
    {
        cin >> k;
        avg += k;
    }
    cout << "average is : " << avg/n << endl;
}

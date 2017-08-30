//dp,二维数组
#include<iostream>
using namespace std;
long long Knap(int n, int m, long long **arr){
    for(int i=2; i<=n; i++){
        for(int j=1; j<=m; j++){
            if(i>j)
                arr[i][j] = arr[i-1][j];
            else if(i==j)
                arr[i][j] = arr[i-1][j] + 1;
            else
                arr[i][j] = arr[i-1][j] + arr[i-1][j-i];
        }
    }
    return arr[n][m];
}

int main(){

    int N;

        cin >> N;
        //不能等分
        if((N+1)*N%4 != 0){
            cout << 0 << endl;
            return 0;
        }
        int half = (1+N)*N / 4;
        //N+1 二维数组的纵向长，代表有N个元素
        long long **arr = new long long *[N+1];
        for(int i=1; i<=N; i++){
            //二维数组的横向长，代表背包的容量
            arr[i] = new long long [half+1];
        }
        for(int j=2; j<=half; j++){
            arr[1][j] = 0;
        }
        arr[1][1] = 1;
        //因为子集的两边会重复，因此除2
        cout << Knap(N, half, arr)/2 << endl;
    return 0;
}

===============================================================================
//dp,备忘录
#include<iostream>
using namespace std;

long long Knap(int i, int j, long long **arr){

    if(arr[i][j] != -1){
        return arr[i][j];
    }
    if(i > j)
        arr[i][j] = Knap(i-1,j,arr);
    else if(i == j)
        arr[i][j] = Knap(i-1,j,arr)+1;
    else
        arr[i][j] = Knap(i-1,j,arr) + Knap(i-1,j-i,arr);

    return arr[i][j];
}

int main(){

    int N;
    cin >> N;
    if((1+N)*N%4 != 0){
        cout << 0 << endl;
        return 0;
    }
    int half = (1+N)*N/4;
    long long **arr = new long long *[N+1];
    for(int i=1; i<=N; i++){
        arr[i] = new long long[half+1];
    }
    for(int i=2; i<=N; i++){
        for(int j=1; j<=half; j++){
            arr[i][j] = -1;
        }
    }
    for(int i=1; i<=half; i++){
        arr[1][i] = 0;
    }
    arr[1][1] = 1;
    cout << Knap(N,half,arr)/2 << endl;
    return 0;
}
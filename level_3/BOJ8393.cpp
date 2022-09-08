#include<iostream>
using namespace std;
int N;
int main() {
	cin >> N;
	int T = 0;
	for (int i = 1; i <= N; i++) {
		T = T+i;
	}
	cout << T;
	return 0;
}
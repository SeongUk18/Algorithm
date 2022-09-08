#include<iostream>
using namespace std;
int X,N,a,b;
int main() {
	int price = 0;
	cin >> X;
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> a >> b;
		price = price + a * b;
	}
	if (X - price == 0)
		cout << "Yes";
	else
		cout << "No";
	return 0;
}
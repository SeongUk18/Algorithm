#include<iostream>
using namespace std;
int A,B;
int main() {
	cin >> A;
	cin >> B;
	if (A > 0) {
		if (B > 0)
			cout << 1;
		else
			cout << 4;
	}
	else if(A < 0) {
		if (B > 0)
			cout << 2;
		else
			cout << 3;
	}
	return 0;
}
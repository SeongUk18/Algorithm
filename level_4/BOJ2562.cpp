#include<iostream>
#include<vector>
using namespace std;
int N, maxNumber,line;
vector<int> numbers;
int main() {

	line,maxNumber = 0;
	for (int i = 0; i < 9; i++) {
		cin >> N;
		numbers.push_back(N);
	}
	for (int i = 0; i < numbers.size(); i++) {
		if (numbers[i] > maxNumber) {
			maxNumber = numbers[i];
			line=i+1;
		}
	}

	cout << maxNumber << "\n";
	cout << line;

	return 0;
}
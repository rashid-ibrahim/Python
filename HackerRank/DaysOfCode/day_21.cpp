/**
The problem for day 21 could only be done in specific languages.
C++, C, C#, Java, Lua, or Swift.

I've opted to do this one in C++
Problem Statement found at: https://www.hackerrank.com/challenges/30-generics/problem
**/
#include <iostream>
#include <vector>
#include <string>

using namespace std;

template <class T>
void printArray(vector<T> t) {
    for (int i=0; i < t.size(); ++i) {
        std::cout << t[i] << std::endl;
    }
};

// ###Begin Auto Generated Code from problem statement###
int main() {
	int n;

	cin >> n;
	vector<int> int_vector(n);
	for (int i = 0; i < n; i++) {
		int value;
		cin >> value;
		int_vector[i] = value;
	}

	cin >> n;
	vector<string> string_vector(n);
	for (int i = 0; i < n; i++) {
		string value;
		cin >> value;
		string_vector[i] = value;
	}

	printArray<int>(int_vector);
	printArray<string>(string_vector);

	return 0;
}
// ###End Auto Generated Code from problem statement###
//
// Created by alexconlima on 01/12/2024.
//

#include <vector>
#include <string>
#include <fstream>
#include <iostream>
#include <algorithm>
using namespace std;

int part1(vector<int>& c1, vector<int>& c2){
    sort(c1.begin(), c1.end());
    sort(c2.begin(), c2.end());
    int sum = 0;

    for (int i = 0 ; i < c1.size(); i++){
        sum += abs(c1[i] - c2[i]);
    }

    return sum;
}

int part2(vector<int>& c1, vector<int>& c2){
    int sum = 0;
    for (int i : c1)
        sum += i * count(c2.begin(), c2.end(), i);
    return sum;
}

int main(){
    ifstream file;
    vector<int> col1;
    vector<int> col2;

    file.open("day1.txt");
    while(!file.eof()){
        int c1;
        int c2;

        file >> c1 >> c2;
        col1.push_back(c1);
        col2.push_back(c2);
    }
    file.close();

    cout << "Part 1: " << part1(col1, col2) << endl;
    cout << "Part 2: " << part2(col1, col2) << endl;

    return 0;
}



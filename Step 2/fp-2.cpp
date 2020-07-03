//////////////////////////////////////////////////////////////////////////////////////////////////
// Task - check existed numbers of range [0..10] in array
//////////////////////////////////////////////////////////////////////////////////////////////////

#include <iostream>
#include <string>

using namespace std;

const int N = 1E3, M = 11;
int m[N];



// imperative mutable algorythm

bool r[M];

void proc_iter(int n) { for (int i=0; i<n; i++) r[m[i]] = 1; }

void show_iter() {
    for (int i=0; i<M; i++)
        cout << i << "\t" << (r[i] ? "YES" : "-") << "\n";
}



// immutable data structure with interface

typedef int acc_t;

acc_t empty_acc = 0;

acc_t set(acc_t a, int i) { return a | (1 << i); }

bool  get(acc_t a, int i) { return a & (1 << i); }



// tail recursion immutable algorythm

acc_t f(int n, acc_t a) { return (n<0) ? a : f(n-1, set(a, m[n])); }

string row(acc_t a, int i) {
    return to_string(i) + "\t" + (get(a, i) ? "YES" : "-");
}

string st(acc_t a, int i, string s) {
    string s_new = s + "\n" + row(a, i);
    return (i>=M) ? s : st(a, i+1, s_new);
}



// non-tail recursion immutable algorythm

acc_t g(int n) { return (n<0) ? empty_acc : set(g(n-1), m[n]); }

string sr(acc_t a, int i) {
    string s = "\n" + row(a, i);
    return (i>=M) ? "" : s + sr(a, i+1);
}


int main() {
    int x, n = 0; while (cin >> x) m[n++] = x;
    
    proc_iter(n);
    show_iter();
    
    acc_t a0 = f(n-1, empty_acc);
    cout << st(a0, 0, "") << "\n";
    
    acc_t a1 = g(n-1);
    cout << sr(a1, 0) << "\n";
}

// input
// 2 3 3 3 3 3 3 2 2 2 7 3 3 1